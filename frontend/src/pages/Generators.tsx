import { useState } from "react";
import { api } from "../api";

export default function Generators() {
  const [seed, setSeed] = useState(42);
  const [storeys, setStoreys] = useState(10);
  const [diffRule, setDiffRule] = useState("mirror");
  const [massing, setMassing] = useState<Record<string, unknown> | null>(null);
  const [typical, setTypical] = useState<Record<string, unknown> | null>(null);
  const [ground, setGround] = useState<Record<string, unknown> | null>(null);
  const [core, setCore] = useState<Record<string, unknown> | null>(null);

  async function runAll() {
    const site = [
      [0, 0],
      [50, 0],
      [50, 56],
      [0, 56],
      [0, 0],
    ];
    const m = await api.massing({
      site_footprint_m: site,
      storeys,
      seed,
      height_limit_m: 45,
      podium_storeys: 2,
    });
    setMassing(m);
    const t = await api.typicalFloor({
      seed,
      difference_rule: diffRule,
      hierarchy: "public-communal-private",
      floor_index: 3,
    });
    setTypical(t);
    const g = await api.groundFloor({ seed, open_space_pct_target: 50 });
    setGround(g);
    const units = (t.metrics as { units_total: number }).units_total;
    const c = await api.coreService({
      unit_count: Math.max(200, units * (storeys - 2)),
      storeys,
      units_per_floor: units,
      provide_parking: false,
    });
    setCore(c);
  }

  return (
    <div className="mx-auto max-w-6xl space-y-6">
      <header>
        <p className="text-xs tracking-[0.2em] text-[#1f4b66] uppercase">Automation</p>
        <h2 className="text-3xl font-semibold">Massing · plans · core</h2>
      </header>

      <div className="flex flex-wrap items-end gap-3 rounded-lg border border-[#d9d2c5] bg-white p-4">
        <label className="text-xs">
          Seed
          <input
            type="number"
            className="mt-1 block w-24 rounded border px-2 py-1.5 text-sm"
            value={seed}
            onChange={(e) => setSeed(Number(e.target.value))}
          />
        </label>
        <label className="text-xs">
          Storeys
          <input
            type="number"
            className="mt-1 block w-24 rounded border px-2 py-1.5 text-sm"
            value={storeys}
            onChange={(e) => setStoreys(Number(e.target.value))}
          />
        </label>
        <label className="text-xs">
          Difference rule
          <select
            className="mt-1 block rounded border px-2 py-1.5 text-sm"
            value={diffRule}
            onChange={(e) => setDiffRule(e.target.value)}
          >
            <option value="mirror">mirror</option>
            <option value="shift">shift</option>
            <option value="alternate">alternate</option>
          </select>
        </label>
        <button onClick={runAll} className="rounded bg-[#1f4b66] px-4 py-2 text-sm text-white">
          Generate
        </button>
      </div>

      <div className="grid gap-4 lg:grid-cols-2">
        {massing ? (
          <Panel title="Massing" meta={JSON.stringify(massing.metrics)}>
            <div
              className="overflow-auto rounded bg-[#fafafa]"
              dangerouslySetInnerHTML={{ __html: String(massing.svg) }}
            />
            <p className="mt-2 text-xs text-neutral-600">
              Height {String(massing.height_m)} m · seed {String(massing.seed)}
            </p>
          </Panel>
        ) : null}
        {typical ? (
          <Panel title="Typical floor" meta={JSON.stringify(typical.metrics)}>
            <div
              className="overflow-auto rounded bg-[#fafafa]"
              dangerouslySetInnerHTML={{ __html: String(typical.svg) }}
            />
          </Panel>
        ) : null}
        {ground ? (
          <Panel title="Ground floor" meta={JSON.stringify(ground.metrics)}>
            <div
              className="overflow-auto rounded bg-[#fafafa]"
              dangerouslySetInnerHTML={{ __html: String(ground.svg) }}
            />
          </Panel>
        ) : null}
        {core ? (
          <Panel title="Core & services" meta="">
            <ul className="space-y-1 text-sm">
              <li>Lifts: {(core.lifts as { count: number }).count}</li>
              <li>Stairs/exits: {(core.stairs_exits as { count: number }).count}</li>
              <li>
                Travel est:{" "}
                {(core.stairs_exits as { max_travel_distance_est_m: number })
                  .max_travel_distance_est_m}{" "}
                m
              </li>
              <li>
                Core area ≈ {(core.core as { approx_area_sqm: number }).approx_area_sqm} m²
              </li>
            </ul>
            <ul className="mt-3 list-disc pl-4 text-xs text-neutral-600">
              {((core.suggestions as string[]) || []).map((s) => (
                <li key={s}>{s}</li>
              ))}
            </ul>
          </Panel>
        ) : null}
      </div>
    </div>
  );
}

function Panel({
  title,
  meta,
  children,
}: {
  title: string;
  meta: string;
  children: React.ReactNode;
}) {
  return (
    <div className="rounded-lg border border-[#d9d2c5] bg-white p-4">
      <div className="mb-2 flex items-baseline justify-between gap-2">
        <h3 className="font-semibold">{title}</h3>
        <span className="max-w-[60%] truncate font-mono text-[10px] text-neutral-400">
          {meta}
        </span>
      </div>
      {children}
    </div>
  );
}
