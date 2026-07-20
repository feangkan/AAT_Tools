import { useEffect, useState } from "react";
import { api } from "../api";

type Result = {
  id: string;
  title: string;
  status: string;
  message: string;
  suggestion?: string;
};

export default function Inspector() {
  const [state, setState] = useState<Record<string, unknown> | null>(null);
  const [report, setReport] = useState<Record<string, unknown> | null>(null);
  const [exportPath, setExportPath] = useState<string | null>(null);

  async function refresh(s?: Record<string, unknown>) {
    const current = s ?? (await api.state());
    setState(current);
    const rep = await api.inspect(current);
    setReport(rep);
  }

  useEffect(() => {
    refresh().catch(console.error);
  }, []);

  async function updateField(path: string, value: unknown) {
    if (!state) return;
    const next = structuredClone(state);
    if (path.includes(".")) {
      const [a, b] = path.split(".");
      (next[a] as Record<string, unknown>)[b] = value;
    } else {
      next[path] = value;
    }
    await api.putState(next);
    await refresh(next);
  }

  async function exportGap() {
    const results = (report?.results as Result[]) || [];
    const fails = results.filter((r) => r.status === "fail" || r.status === "warn");
    const res = await api.exportA3({
      title: "Inspector Gap Report",
      subtitle: `Score ${report?.score}%`,
      sheets: [
        {
          title: "Compliance summary",
          body: `Passed ${report?.passed} · Failed ${report?.failed} · Warnings ${report?.warnings}`,
          bullets: fails.map(
            (r) => `${r.status.toUpperCase()} ${r.id}: ${r.message}${r.suggestion ? ` → ${r.suggestion}` : ""}`,
          ),
        },
      ],
      filename: "inspector_gap_report.pdf",
    });
    setExportPath(res.path);
  }

  const results = (report?.results as Result[]) || [];
  const color = (s: string) =>
    s === "pass" ? "text-green-800 bg-green-50" : s === "fail" ? "text-red-800 bg-red-50" : s === "warn" ? "text-amber-900 bg-amber-50" : "text-neutral-600 bg-neutral-50";

  return (
    <div className="mx-auto max-w-6xl space-y-6">
      <header className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <p className="text-xs tracking-[0.2em] text-[#1f4b66] uppercase">Compliance loop</p>
          <h2 className="text-3xl font-semibold">Inspector agents</h2>
          <p className="mt-1 text-sm text-neutral-600">
            Recheck brief · VicPlan · NCC / BADS / LHD — then suggest improvements.
          </p>
        </div>
        <div className="flex items-center gap-3">
          <div className="rounded-lg border border-[#d9d2c5] bg-white px-4 py-2 text-center">
            <div className="text-[10px] uppercase text-neutral-500">Score</div>
            <div className="text-2xl font-semibold">{String(report?.score ?? "—")}%</div>
          </div>
          <button onClick={exportGap} className="rounded bg-[#1f4b66] px-4 py-2 text-sm text-white">
            Export A3 gap report
          </button>
        </div>
      </header>

      {exportPath ? <p className="text-sm text-green-800">Exported → {exportPath}</p> : null}

      {state ? (
        <div className="grid gap-3 rounded-lg border border-[#d9d2c5] bg-white p-4 md:grid-cols-4">
          {(
            [
              ["unit_count", "Units"],
              ["ground_open_space_pct", "Open space %"],
              ["exit_count", "Exits"],
              ["max_travel_distance_m", "Travel m"],
              ["floor_to_ceiling_m", "FTC m"],
              ["building_height_m", "Height m"],
              ["dda_per_floor", "DDA / floor"],
              ["communal_os_winter_sun_hours", "Winter sun h"],
            ] as const
          ).map(([key, label]) => (
            <label key={key} className="text-xs">
              {label}
              <input
                type="number"
                className="mt-1 w-full rounded border border-[#d9d2c5] px-2 py-1.5 text-sm"
                value={Number(state[key] ?? 0)}
                onChange={(e) => updateField(key, Number(e.target.value))}
              />
            </label>
          ))}
        </div>
      ) : null}

      <div className="space-y-2">
        {results.map((r) => (
          <div key={r.id} className={`rounded-md border border-[#e8e2d6] p-3 ${color(r.status)}`}>
            <div className="flex flex-wrap items-center justify-between gap-2">
              <div className="font-medium">
                <span className="mr-2 font-mono text-[11px] opacity-70">{r.id}</span>
                {r.title}
              </div>
              <span className="text-[11px] font-bold tracking-wide uppercase">{r.status}</span>
            </div>
            <p className="mt-1 text-sm">{r.message}</p>
            {r.suggestion ? (
              <p className="mt-1 text-sm font-medium">Suggestion: {r.suggestion}</p>
            ) : null}
          </div>
        ))}
      </div>
    </div>
  );
}
