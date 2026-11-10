import { Link } from "react-router-dom";
import { ScanSearch } from "lucide-react";

const columns = [
  {
    title: "EXPLORE",
    items: [
      { label: "Home", to: "/" },
      { label: "Discover Cases", to: "/cases" },
      { label: "Community", to: "/#community" },
    ],
  },
  {
    title: "PLATFORM",
    items: [
      { label: "How It Works", to: "/#how-it-works" },
      { label: "AI Investigation", to: "/#ai" },
      { label: "About", to: "/#about" },
    ],
  },
  {
    title: "ACCOUNT",
    items: [
      { label: "Log In", to: "/login" },
      { label: "Get Started", to: "/register" },
    ],
  },
];

export default function Footer() {
  return (
    <footer className="border-t border-[var(--border)] bg-[var(--background)]">
      <div className="mx-auto grid max-w-[1320px] gap-12 px-5 py-16 sm:px-8 md:grid-cols-12">
        <div className="md:col-span-5">
          <Link to="/" className="flex items-center gap-3">
            <span className="grid h-10 w-10 place-items-center rounded-full bg-[var(--primary)] text-[var(--background)]">
              <ScanSearch size={19} strokeWidth={1.6} />
            </span>
            <span className="font-playfair text-2xl font-semibold text-[var(--primary-dark)]">AfterWord</span>
          </Link>
          <p className="mt-6 max-w-sm font-playfair text-[19px] leading-relaxed text-[var(--text-secondary)]">
            A home for curious minds, unanswered questions, and the pursuit of understanding.
          </p>
        </div>

        <div className="grid grid-cols-2 gap-10 sm:grid-cols-3 md:col-span-7 md:pl-10">
          {columns.map((c) => (
            <div key={c.title}>
              <h3 className="text-[11px] font-medium tracking-[0.2em] text-[var(--text-muted)]">{c.title}</h3>
              <ul className="mt-5 space-y-3">
                {c.items.map((i) => (
                  <li key={i.label}>
                    <Link to={i.to} className="nav-link text-[15px] text-[var(--text-primary)] hover:text-[var(--primary)]">
                      {i.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>

      <div className="border-t border-[var(--border)]">
        <div className="mx-auto flex max-w-[1320px] flex-col gap-2 px-5 py-6 text-sm text-[var(--text-muted)] sm:flex-row sm:items-center sm:justify-between sm:px-8">
          <p>Copyright © 2026 AfterWord.</p>
          <p className="font-playfair italic text-[var(--text-secondary)]">Made for the curious.</p>
        </div>
      </div>
    </footer>
  );
}