import type { ReactNode } from "react";

export function A3Preview({
  title,
  subtitle,
  children,
  sheetNo = 1,
  total = 1,
}: {
  title: string;
  subtitle?: string;
  children?: ReactNode;
  sheetNo?: number;
  total?: number;
}) {
  return (
    <div className="a3-sheet relative w-full overflow-hidden bg-white text-left">
      <div className="absolute inset-2 border border-neutral-800" />
      <div className="relative flex h-full flex-col p-5">
        <div className="border-b border-neutral-300 pb-2">
          <div className="text-[10px] tracking-[0.2em] text-[#1f4b66] uppercase">
            AAT Studio Tools · ARCH3372 · A3 Landscape
          </div>
          <h3 className="mt-1 text-lg font-semibold text-neutral-900">{title}</h3>
          {subtitle ? (
            <p className="text-xs text-neutral-500">{subtitle}</p>
          ) : null}
        </div>
        <div className="min-h-0 flex-1 overflow-hidden py-3 text-sm text-neutral-800">
          {children}
        </div>
        <div className="mt-auto flex items-end justify-between gap-3 border-t border-neutral-800 pt-2">
          <div className="text-[10px] text-neutral-500">
            63–67 Nicholson St, Footscray · ACZ1 · Wurundjeri Country
          </div>
          <div className="min-w-[140px] border border-neutral-800 p-2 text-[10px]">
            <div className="bg-[#1f4b66] px-1 py-0.5 font-semibold tracking-wide text-white">
              TITLE BLOCK
            </div>
            <div className="mt-1 font-medium">{title.slice(0, 28)}</div>
            <div className="text-right text-sm font-bold">
              {sheetNo} / {total}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
