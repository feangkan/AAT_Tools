import { useEffect, useState } from "react";
import { api } from "../api";
import { A3Preview } from "../components/A3Preview";

export default function SiteSolar() {
  const [planning, setPlanning] = useState<Record<string, unknown> | null>(null);
  const [context, setContext] = useState<Record<string, unknown> | null>(null);
  const [solar, setSolar] = useState<Record<string, unknown> | null>(null);
  const [height, setHeight] = useState(32);

  useEffect(() => {
    (async () => {
      setPlanning(await api.sitePlanning());
      setContext(await api.siteContext());
      const footprint = [
        [0, 0],
        [24, 0],
        [24, 18],
        [0, 18],
        [0, 0],
      ];
      setSolar(await api.solar({ footprint, height_m: height, date: "2026-06-22" }));
    })().catch(console.error);
  }, []);

  async function rerunSolar() {
    const footprint = [
      [0, 0],
      [24, 0],
      [24, 18],
      [0, 18],
      [0, 0],
    ];
    setSolar(await api.solar({ footprint, height_m: height, date: "2026-06-22" }));
  }

  const zone = (planning?.zone as Record<string, unknown>) || {};
  const samples = (solar?.samples as Array<Record<string, unknown>>) || [];

  return (
    <div className="mx-auto max-w-6xl space-y-6">
      <header>
        <p className="text-xs tracking-[0.2em] text-[#1f4b66] uppercase">AT1.1 / AT1.2</p>
        <h2 className="text-3xl font-semibold">Site & solar analysis</h2>
        <p className="mt-1 text-sm text-neutral-600">
          Vicmap planning (CC BY 4.0) · OSM context · winter solstice overshadowing (2.5D)
        </p>
      </header>

      <div className="grid gap-4 lg:grid-cols-2">
        <div className="rounded-lg border border-[#d9d2c5] bg-white p-4">
          <h3 className="font-semibold">Planning pack</h3>
          <dl className="mt-3 space-y-2 text-sm">
            <div className="flex justify-between gap-3 border-b border-neutral-100 py-1">
              <dt className="text-neutral-500">Zone</dt>
              <dd className="font-medium">{String(zone.zone_code ?? "—")}</dd>
            </div>
            <div className="flex justify-between gap-3 border-b border-neutral-100 py-1">
              <dt className="text-neutral-500">Description</dt>
              <dd className="text-right">{String(zone.zone_description ?? "—")}</dd>
            </div>
            <div className="flex justify-between gap-3 border-b border-neutral-100 py-1">
              <dt className="text-neutral-500">Overlays</dt>
              <dd>{((planning?.overlays as string[]) || []).join(", ")}</dd>
            </div>
            <div className="flex justify-between gap-3 border-b border-neutral-100 py-1">
              <dt className="text-neutral-500">Source</dt>
              <dd>{String(zone.source ?? "—")}</dd>
            </div>
          </dl>
          <p className="mt-3 text-[11px] text-neutral-500">
            {String(planning?.attribution ?? "")}
          </p>
          <ul className="mt-3 list-disc space-y-1 pl-4 text-xs text-neutral-700">
            {((planning?.guidance as string[]) || []).map((g) => (
              <li key={g}>{g}</li>
            ))}
          </ul>
        </div>

        <A3Preview title="Solar study — 22 Jun" subtitle="Clause 58 communal OS winter sun">
          <div className="mb-2 flex items-center gap-2 text-xs">
            <label>
              Height m{" "}
              <input
                type="number"
                className="ml-1 w-16 rounded border px-1"
                value={height}
                onChange={(e) => setHeight(Number(e.target.value))}
              />
            </label>
            <button onClick={rerunSolar} className="rounded bg-[#1f4b66] px-2 py-1 text-white">
              Recalc
            </button>
          </div>
          <div className="grid grid-cols-4 gap-1 text-[10px]">
            {samples.map((s) => {
              const sun = s.sun as { altitude_deg: number; azimuth_deg: number };
              return (
                <div key={String(s.hour)} className="rounded border border-neutral-200 p-1">
                  <div className="font-semibold">{String(s.hour)}:00</div>
                  <div>alt {sun.altitude_deg}°</div>
                  <div>az {sun.azimuth_deg}°</div>
                </div>
              );
            })}
          </div>
        </A3Preview>
      </div>

      <div className="rounded-lg border border-[#d9d2c5] bg-white p-4">
        <h3 className="font-semibold">Surrounding context</h3>
        <p className="text-xs text-neutral-500">
          {String(context?.source)} · {String(context?.attribution)}
        </p>
        <ul className="mt-2 columns-2 gap-4 text-sm">
          {((context?.buildings as Array<Record<string, unknown>>) || [])
            .slice(0, 12)
            .map((b, i) => (
              <li key={i} className="break-inside-avoid border-b border-neutral-100 py-1">
                {String(b.name || b.building || b.type || "building")}
                {b.levels ? ` · ${b.levels} levels` : ""}
                {b.note ? ` — ${b.note}` : ""}
              </li>
            ))}
        </ul>
      </div>
    </div>
  );
}
