/** Small status / category marker. tone: "green" | "orange" | "paper" | "light" */
const tones = {
  green: "bg-[var(--primary)] text-[var(--background)]",
  orange: "bg-[var(--accent-soft)] text-[#8F441F]",
  paper: "bg-[var(--surface-soft)] text-[var(--text-secondary)] border border-[var(--border)]",
  light: "bg-white/90 text-[var(--primary-dark)]",
};

export default function Badge({ tone = "paper", dot = false, className = "", children }) {
  return (
    <span
      className={`inline-flex items-center gap-1.5 rounded-full px-2.5 py-1 text-[11px] font-medium tracking-[0.08em] uppercase ${tones[tone]} ${className}`}
    >
      {dot && <span className="h-1.5 w-1.5 rounded-full bg-[var(--accent)]" aria-hidden="true" />}
      {children}
    </span>
  );
}