export const API_BASE = import.meta.env.VITE_API_BASE ?? "";

async function req<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json", ...(init?.headers || {}) },
    ...init,
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || res.statusText);
  }
  return res.json() as Promise<T>;
}

export const api = {
  brief: () => req<{ summary: Record<string, unknown>; raw: unknown }>("/api/brief"),
  landscape: () => req<Record<string, unknown>>("/api/landscape"),
  state: () => req<Record<string, unknown>>("/api/state"),
  putState: (state: Record<string, unknown>) =>
    req("/api/state", { method: "PUT", body: JSON.stringify({ state }) }),
  planner: (members: string[]) =>
    req<Record<string, unknown>>("/api/planner", {
      method: "POST",
      body: JSON.stringify({ members }),
    }),
  inspect: (state?: Record<string, unknown>) =>
    req<Record<string, unknown>>("/api/inspect", {
      method: "POST",
      body: JSON.stringify({ state }),
    }),
  sitePlanning: () => req<Record<string, unknown>>("/api/site/planning"),
  siteContext: () => req<Record<string, unknown>>("/api/site/context"),
  solar: (body: Record<string, unknown>) =>
    req<Record<string, unknown>>("/api/site/solar", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  massing: (body: Record<string, unknown>) =>
    req<Record<string, unknown>>("/api/generate/massing", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  typicalFloor: (body: Record<string, unknown>) =>
    req<Record<string, unknown>>("/api/generate/typical-floor", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  groundFloor: (body: Record<string, unknown>) =>
    req<Record<string, unknown>>("/api/generate/ground-floor", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  coreService: (body: Record<string, unknown>) =>
    req<Record<string, unknown>>("/api/generate/core-service", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  chat: (body: Record<string, unknown>) =>
    req<Record<string, unknown>>("/api/chat", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  search: (q: string) =>
    req<{ hits: unknown[] }>(`/api/knowledge/search?q=${encodeURIComponent(q)}`),
  ingest: () => req("/api/knowledge/ingest", { method: "POST" }),
  structure: () => req<Record<string, unknown>>("/api/details/structure"),
  facade: () => req<Record<string, unknown>>("/api/details/facade"),
  precedents: () => req<Record<string, unknown>>("/api/precedents/template"),
  exportA3: (body: Record<string, unknown>) =>
    req<{ path: string }>("/api/export/a3", {
      method: "POST",
      body: JSON.stringify(body),
    }),
};
