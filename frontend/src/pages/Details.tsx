import { useEffect, useState } from "react";
import { api } from "../api";

export default function Details() {
  const [structure, setStructure] = useState<Record<string, unknown> | null>(null);
  const [facade, setFacade] = useState<Record<string, unknown> | null>(null);
  const [precedents, setPrecedents] = useState<Record<string, unknown> | null>(null);

  useEffect(() => {
    (async () => {
      setStructure(await api.structure());
      setFacade(await api.facade());
      setPrecedents(await api.precedents());
    })().catch(console.error);
  }, []);

  return (
    <div className="mx-auto max-w-6xl space-y-6">
      <header>
        <p className="text-xs tracking-[0.2em] text-[#1f4b66] uppercase">AT1.3–1.5 · AT3</p>
        <h2 className="text-3xl font-semibold">Structure · facade · precedents</h2>
      </header>

      <section className="rounded-lg border border-[#d9d2c5] bg-white p-4">
        <h3 className="font-semibold">Structural options</h3>
        <p className="text-sm text-neutral-600">{String(structure?.recommendation ?? "")}</p>
        <div className="mt-3 grid gap-3 md:grid-cols-3">
          {((structure?.options as Array<Record<string, unknown>>) || []).map((o) => (
            <div key={String(o.id)} className="rounded border border-[#eee] p-3 text-sm">
              <div className="font-medium">{String(o.name)}</div>
              <div className="mt-2 text-xs text-neutral-500">
                Grid {(o.grid_m as number[])?.join(" / ")} m
              </div>
              <ul className="mt-2 list-disc pl-4 text-xs">
                {((o.pros as string[]) || []).map((p) => (
                  <li key={p}>{p}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </section>

      <section className="rounded-lg border border-[#d9d2c5] bg-white p-4">
        <h3 className="font-semibold">Facade bay templates</h3>
        <div className="mt-3 grid gap-3 md:grid-cols-3">
          {((facade?.bay_types as Array<Record<string, unknown>>) || []).map((b) => (
            <div key={String(b.id)} className="rounded border border-[#eee] p-3 text-sm">
              <div className="font-medium">{String(b.id)}</div>
              <div className="text-xs text-neutral-500">
                {String(b.width_m)} × {String(b.height_m)} m · WFR {String(b.window_to_floor_pct)}%
              </div>
              <p className="mt-2 text-xs">{String(b.notes)}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="rounded-lg border border-[#d9d2c5] bg-white p-4">
        <h3 className="font-semibold">Precedent slots (AT1.3)</h3>
        <p className="text-xs text-neutral-500">
          {String(precedents?.required_buildings)} buildings × {String(precedents?.a3_per_building)}{" "}
          A3 · present best {String(precedents?.present_best)}
        </p>
        <div className="mt-3 grid gap-2 md:grid-cols-2">
          {((precedents?.slots as Array<Record<string, unknown>>) || []).map((s) => (
            <div key={String(s.id)} className="rounded border border-dashed border-neutral-300 p-3 text-sm">
              <div className="font-mono text-xs text-neutral-400">Precedent {String(s.id)}</div>
              <div className="text-neutral-500">Name / location / structure / facade / core…</div>
            </div>
          ))}
        </div>
        <ul className="mt-3 flex flex-wrap gap-2 text-[11px]">
          {((precedents?.analysis_lenses as string[]) || []).map((l) => (
            <li key={l} className="rounded-full bg-[#f4f1ea] px-2 py-1">
              {l}
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
