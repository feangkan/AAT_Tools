import { useState } from "react";
import { api } from "../api";
import { A3Preview } from "../components/A3Preview";

export default function Chat() {
  const [message, setMessage] = useState(
    "What do we need for the NCC D1 egress report and how should we present it on A3?",
  );
  const [provider, setProvider] = useState("offline");
  const [apiKey, setApiKey] = useState("");
  const [reply, setReply] = useState<Record<string, unknown> | null>(null);
  const [exportPath, setExportPath] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function send() {
    setBusy(true);
    try {
      const r = await api.chat({
        message,
        provider,
        api_key: apiKey || null,
      });
      setReply(r);
    } finally {
      setBusy(false);
    }
  }

  async function exportPresentation() {
    if (!reply) return;
    const bullets = (reply.presentation_bullets as string[]) || [];
    const res = await api.exportA3({
      title: "Presentation pull",
      subtitle: message.slice(0, 80),
      sheets: [
        {
          title: "Agent response",
          body: String(reply.answer || "").slice(0, 1800),
          bullets,
        },
      ],
      filename: "presentation_pull.pdf",
    });
    setExportPath(res.path);
  }

  return (
    <div className="mx-auto max-w-6xl space-y-6">
      <header>
        <p className="text-xs tracking-[0.2em] text-[#1f4b66] uppercase">BYOK agents</p>
        <h2 className="text-3xl font-semibold">Chat · presentation agent</h2>
      </header>

      <div className="grid gap-3 rounded-lg border border-[#d9d2c5] bg-white p-4 md:grid-cols-3">
        <label className="text-xs md:col-span-1">
          Provider
          <select
            className="mt-1 w-full rounded border px-2 py-1.5 text-sm"
            value={provider}
            onChange={(e) => setProvider(e.target.value)}
          >
            <option value="offline">offline (RAG)</option>
            <option value="openai">openai</option>
            <option value="anthropic">anthropic</option>
            <option value="ollama">ollama local</option>
          </select>
        </label>
        <label className="text-xs md:col-span-2">
          API key (optional)
          <input
            className="mt-1 w-full rounded border px-2 py-1.5 text-sm"
            type="password"
            value={apiKey}
            onChange={(e) => setApiKey(e.target.value)}
            placeholder="Leave blank for offline rule/RAG answers"
          />
        </label>
        <label className="text-xs md:col-span-3">
          Ask
          <textarea
            className="mt-1 w-full rounded border px-3 py-2 text-sm"
            rows={3}
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
        </label>
        <div className="flex gap-2 md:col-span-3">
          <button
            onClick={send}
            disabled={busy}
            className="rounded bg-[#1f4b66] px-4 py-2 text-sm text-white"
          >
            {busy ? "Thinking…" : "Ask"}
          </button>
          <button
            onClick={exportPresentation}
            disabled={!reply}
            className="rounded border border-[#1f4b66] px-4 py-2 text-sm text-[#1f4b66]"
          >
            Lay out on A3
          </button>
        </div>
      </div>

      {exportPath ? <p className="text-sm text-green-800">Exported → {exportPath}</p> : null}

      {reply ? (
        <div className="grid gap-4 lg:grid-cols-2">
          <div className="rounded-lg border border-[#d9d2c5] bg-white p-4">
            <div className="text-[11px] uppercase tracking-wide text-neutral-500">
              Provider: {String(reply.provider)}
            </div>
            <div className="prose-Tight mt-3 text-sm">{String(reply.answer)}</div>
          </div>
          <A3Preview title="Presentation sheet" subtitle="Pulled for A3 folio">
            <ul className="space-y-1 text-xs">
              {((reply.presentation_bullets as string[]) || []).map((b) => (
                <li key={b}>• {b}</li>
              ))}
            </ul>
          </A3Preview>
        </div>
      ) : null}
    </div>
  );
}
