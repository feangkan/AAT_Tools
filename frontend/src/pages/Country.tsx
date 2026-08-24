import { useEffect, useState } from "react";
import { api } from "../api";
import { A3Preview } from "../components/A3Preview";

export default function Country() {
  const [data, setData] = useState<Record<string, unknown> | null>(null);

  useEffect(() => {
    api.landscape().then(setData).catch(console.error);
  }, []);

  const palette = (data?.palette as Array<Record<string, string>>) || [];

  return (
    <div className="mx-auto max-w-6xl space-y-6">
      <header>
        <p className="text-xs tracking-[0.2em] text-[#1f4b66] uppercase">PC36 · open space</p>
        <h2 className="text-3xl font-semibold">Designing with Country</h2>
        <p className="mt-1 max-w-3xl text-sm text-neutral-600">
          {String(data?.country ?? "Kulin Nation / Wurundjeri Country")} — indigenous planting
          palette for Melbourne west open space (≥50% ground).
        </p>
      </header>

      <div className="grid gap-4 lg:grid-cols-2">
        <A3Preview
          title="Indigenous landscape palette"
          subtitle={String(data?.region ?? "")}
        >
          <div className="grid grid-cols-2 gap-2 text-[10px]">
            {palette.slice(0, 8).map((p) => (
              <div key={p.scientific} className="rounded border border-neutral-200 p-2">
                <div className="font-semibold">{p.common}</div>
                <div className="italic text-neutral-500">{p.scientific}</div>
                <div className="mt-1">{p.where}</div>
              </div>
            ))}
          </div>
        </A3Preview>
        <div className="rounded-lg border border-[#d9d2c5] bg-white p-4 text-sm">
          <h3 className="font-semibold">Notes</h3>
          <ul className="mt-2 list-disc space-y-1 pl-4 text-neutral-700">
            {((data?.notes as string[]) || []).map((n) => (
              <li key={n}>{n}</li>
            ))}
          </ul>
          <h3 className="mt-4 font-semibold">Sources</h3>
          <ul className="mt-2 list-disc space-y-1 pl-4 text-xs text-neutral-500">
            {((data?.sources as string[]) || []).map((n) => (
              <li key={n}>{n}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}
