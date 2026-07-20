import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api";
import { A3Preview } from "../components/A3Preview";

export default function Dashboard() {
  const [summary, setSummary] = useState<Record<string, unknown> | null>(null);
  const [score, setScore] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    (async () => {
      try {
        const b = await api.brief();
        setSummary(b.summary);
        const rep = await api.inspect();
        setScore(rep.score as number);
      } catch (e) {
        setError(String(e));
      }
    })();
  }, []);

  return (
    <div className="mx-auto max-w-6xl space-y-6">
      <header>
        <p className="text-xs tracking-[0.2em] text-[#1f4b66] uppercase">Overview</p>
        <h2 className="mt-1 text-3xl font-semibold">Studio cockpit</h2>
        <p className="mt-2 max-w-3xl text-sm text-neutral-600">
          Tools for the RMIT ARCH3372 speculative student accommodation + retail project
          at 63–67 Nicholson Street, Footscray. Plan work, check compliance, generate
          massing/plans, and export A3 landscape folios.
        </p>
      </header>

      {error ? (
        <div className="rounded-md border border-red-300 bg-red-50 p-3 text-sm text-red-800">
          Backend not reachable. Start API with{" "}
          <code>./scripts/run_backend.sh</code> — {error}
        </div>
      ) : null}

      <div className="grid gap-4 md:grid-cols-4">
        {(
          [
            ["Units min", summary?.min_units ?? "—"],
            ["Zone", summary?.zone ?? "—"],
            ["A3 pages (min)", summary?.total_min_a3 ?? "—"],
            ["Compliance", score != null ? `${score}%` : "—"],
          ] as Array<[string, string | number]>
        ).map(([k, v]) => (
          <div key={k} className="rounded-lg border border-[#d9d2c5] bg-white p-4">
            <div className="text-[11px] tracking-wide text-neutral-500 uppercase">{k}</div>
            <div className="mt-1 text-2xl font-semibold">{String(v)}</div>
          </div>
        ))}
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <A3Preview
          title="Project brief snapshot"
          subtitle="Machine-readable requirements registry"
        >
          <ul className="space-y-1 text-xs">
            <li>• ≥200 studios (15–25 m²) + DDA 1/20 per floor (30–35 m²)</li>
            <li>• FTC ≥ 2.7 m · 5% services · 10% fire/ducts</li>
            <li>• ≥50% ground public open space + native vegetation</li>
            <li>• Communal: kitchen 120–150 · gym 80–100 · study 100</li>
            <li>• Class 2 / 6 / 3 · NCC D1 F2 J · Clause 58 · LHD</li>
          </ul>
        </A3Preview>
        <div className="rounded-lg border border-[#d9d2c5] bg-white p-5">
          <h3 className="font-semibold">Start here</h3>
          <ol className="mt-3 list-decimal space-y-2 pl-5 text-sm text-neutral-700">
            <li>
              <Link className="text-[#1f4b66] underline" to="/planner">
                Split work
              </Link>{" "}
              across 3 members
            </li>
            <li>
              Pull{" "}
              <Link className="text-[#1f4b66] underline" to="/site">
                Vicmap + solar
              </Link>
            </li>
            <li>
              Generate{" "}
              <Link className="text-[#1f4b66] underline" to="/generate">
                massing & plans
              </Link>
            </li>
            <li>
              Run the{" "}
              <Link className="text-[#1f4b66] underline" to="/inspector">
                Inspector loop
              </Link>
            </li>
            <li>
              Ask the{" "}
              <Link className="text-[#1f4b66] underline" to="/chat">
                presentation agent
              </Link>
            </li>
          </ol>
        </div>
      </div>
    </div>
  );
}
