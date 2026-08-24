import { NavLink, Route, Routes } from "react-router-dom";
import {
  LayoutDashboard,
  Users,
  ShieldCheck,
  Map,
  Boxes,
  MessageSquare,
  TreePine,
  BookOpen,
  Settings2,
} from "lucide-react";
import Dashboard from "./pages/Dashboard";
import Planner from "./pages/Planner";
import Inspector from "./pages/Inspector";
import SiteSolar from "./pages/SiteSolar";
import Generators from "./pages/Generators";
import Chat from "./pages/Chat";
import Country from "./pages/Country";
import Details from "./pages/Details";

const links = [
  { to: "/", label: "Dashboard", icon: LayoutDashboard },
  { to: "/planner", label: "Group Planner", icon: Users },
  { to: "/inspector", label: "Inspector", icon: ShieldCheck },
  { to: "/site", label: "Site & Solar", icon: Map },
  { to: "/generate", label: "Generators", icon: Boxes },
  { to: "/chat", label: "Chat / Present", icon: MessageSquare },
  { to: "/country", label: "Country", icon: TreePine },
  { to: "/details", label: "Details", icon: BookOpen },
];

export default function App() {
  return (
    <div className="flex min-h-screen bg-[#f4f1ea] text-[#0f1419]">
      <aside className="flex w-64 flex-col border-r border-[#d9d2c5] bg-[#faf8f3] px-4 py-6">
        <div className="mb-8">
          <div className="text-[11px] tracking-[0.25em] text-[#1f4b66] uppercase">
            AAT Studio Tools
          </div>
          <h1 className="mt-1 text-xl font-semibold leading-tight">
            Footscray
            <br />
            Student Housing
          </h1>
          <p className="mt-2 text-xs text-neutral-500">
            ARCH3372 · 3-person studio cockpit · A3 landscape
          </p>
        </div>
        <nav className="flex flex-1 flex-col gap-1">
          {links.map(({ to, label, icon: Icon }) => (
            <NavLink
              key={to}
              to={to}
              end={to === "/"}
              className={({ isActive }) =>
                `flex items-center gap-2 rounded-md px-3 py-2 text-sm transition ${
                  isActive
                    ? "bg-[#1f4b66] text-white"
                    : "text-neutral-700 hover:bg-white"
                }`
              }
            >
              <Icon size={16} />
              {label}
            </NavLink>
          ))}
        </nav>
        <div className="mt-4 flex items-start gap-2 rounded-md border border-[#d9d2c5] bg-white p-3 text-[11px] text-neutral-500">
          <Settings2 size={14} className="mt-0.5 shrink-0" />
          <span>
            Vicmap · NCC 2022 CC BY · Clause 58 · LHD. Revit scripts in{" "}
            <code className="text-[10px]">pyrevit/</code>
          </span>
        </div>
      </aside>
      <main className="flex-1 overflow-auto p-6 md:p-8">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/planner" element={<Planner />} />
          <Route path="/inspector" element={<Inspector />} />
          <Route path="/site" element={<SiteSolar />} />
          <Route path="/generate" element={<Generators />} />
          <Route path="/chat" element={<Chat />} />
          <Route path="/country" element={<Country />} />
          <Route path="/details" element={<Details />} />
        </Routes>
      </main>
    </div>
  );
}
