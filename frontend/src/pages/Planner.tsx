import { useState } from "react";
import { api } from "../api";
import { A3Preview } from "../components/A3Preview";

export default function Planner() {
  const [members, setMembers] = useState(["Alex", "Blair", "Casey"]);
  const [plan, setPlan] = useState<Record<string, unknown> | null>(null);
  const [exportPath, setExportPath] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function run() {
    setBusy(true);
    try {
      const p = await api.planner(members);
      setPlan(p);
    } finally {
      setBusy(false);
    }
  }

  async function exportA3() {
    if (!plan) return;
    const assignments = (plan.assignments as Array<Record<string, unknown>>) || [];
    const sheets = [
      {
        title: "Group work plan",
        body: `Members: ${members.join(", ")}. Total min A3 pages: ${plan.total_a3}.`,
        bullets: (plan.notes as string[]) || [],
      },
      ...members.map((m) => ({
        title: `Lead: ${m}`,
        body: `Workload: ${JSON.stringify((plan.workload as Record<string, unknown>)[m])}`,
        bullets: assignments
          .filter((a) => a.lead === m)
          .map((a) => `${a.id} ${a.name} (W${a.week}, ${a.min_a3_pages}×A3)`),
      })),
    ];
    const res = await api.exportA3({
      title: "AAT Group Planner",
      subtitle: "ARCH3372 deliverables split",
      members,
      sheets,
      filename: "group_planner.pdf",
    });
    setExportPath(res.path);
  }

  const assignments = (plan?.assignments as Array<Record<string, unknown>>) || [];

  return (
    <div className="mx-auto max-w-6xl space-y-6">
      <header>
        <p className="text-xs tracking-[0.2em] text-[#1f4b66] uppercase">AT deliverables</p>
        <h2 className="text-3xl font-semibold">Group planner</h2>
      </header>

      <div className="grid gap-3 rounded-lg border border-[#d9d2c5] bg-white p-4 md:grid-cols-4">
        {members.map((m, i) => (
          <label key={i} className="text-sm">
            Member {i + 1}
            <input
              className="mt-1 w-full rounded border border-[#d9d2c5] px-2 py-1.5"
              value={m}
              onChange={(e) => {
                const next = [...members];
                next[i] = e.target.value;
                setMembers(next);
              }}
            />
          </label>
        ))}
        <div className="flex items-end gap-2">
          <button
            onClick={run}
            disabled={busy}
            className="rounded bg-[#1f4b66] px-4 py-2 text-sm font-medium text-white"
          >
            {busy ? "Planning…" : "Build plan"}
          </button>
          <button
            onClick={exportA3}
            disabled={!plan}
            className="rounded border border-[#1f4b66] px-4 py-2 text-sm text-[#1f4b66]"
          >
            Export A3
          </button>
        </div>
      </div>

      {exportPath ? (
        <p className="text-sm text-green-800">Exported → {exportPath}</p>
      ) : null}

      {plan ? (
        <div className="grid gap-4 lg:grid-cols-2">
          <div className="overflow-hidden rounded-lg border border-[#d9d2c5] bg-white">
            <table className="w-full text-left text-sm">
              <thead className="bg-[#f4f1ea] text-xs uppercase tracking-wide text-neutral-500">
                <tr>
                  <th className="px-3 py-2">ID</th>
                  <th className="px-3 py-2">Task</th>
                  <th className="px-3 py-2">Week</th>
                  <th className="px-3 py-2">A3</th>
                  <th className="px-3 py-2">Lead</th>
                </tr>
              </thead>
              <tbody>
                {assignments.map((a) => (
                  <tr key={String(a.id)} className="border-t border-[#eee]">
                    <td className="px-3 py-2 font-mono text-xs">{String(a.id)}</td>
                    <td className="px-3 py-2">{String(a.name)}</td>
                    <td className="px-3 py-2">{String(a.week)}</td>
                    <td className="px-3 py-2">{String(a.min_a3_pages)}</td>
                    <td className="px-3 py-2">{String(a.lead)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <A3Preview title="Workload balance" subtitle="Equal presentation participation">
            <div className="space-y-2 text-xs">
              {members.map((m) => {
                const w = (plan.workload as Record<string, { tasks: number; a3_pages: number }>)[m];
                return (
                  <div key={m} className="flex justify-between border-b border-neutral-200 py-1">
                    <span className="font-medium">{m}</span>
                    <span>
                      {w?.tasks ?? 0} tasks · {w?.a3_pages ?? 0} A3
                    </span>
                  </div>
                );
              })}
            </div>
          </A3Preview>
        </div>
      ) : null}
    </div>
  );
}
