import { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { motion, AnimatePresence } from "framer-motion";
import { ScanSearch, Menu, X } from "lucide-react";

const links = [
  { label: "Discover", to: "/cases" },
  { label: "Investigate", to: "/#how-it-works", hash: "#how-it-works" },
  { label: "Community", to: "/#community", hash: "#community" },
  { label: "About", to: "/#about", hash: "#about" },
];

export default function Navbar() {
  const [open, setOpen] = useState(false);
  const { pathname, hash } = useLocation();

  useEffect(() => setOpen(false), [pathname, hash]);

  const isActive = (l) => (l.hash ? pathname === "/" && hash === l.hash : pathname.startsWith(l.to));

  return (
    <header className="sticky top-0 z-50 border-b border-[var(--border)] bg-[var(--background)]/95 backdrop-blur supports-[backdrop-filter]:bg-[var(--background)]/85">
      <nav
        aria-label="Primary"
        className="mx-auto flex h-[78px] max-w-[1320px] items-center justify-between px-5 sm:px-8"
      >
        {/* Logo */}
        <Link to="/" className="group flex items-center gap-3" aria-label="AfterWord home">
          <span className="grid h-10 w-10 place-items-center rounded-full bg-[var(--primary)] text-[var(--background)] transition-transform duration-500 group-hover:rotate-[-8deg]">
            <ScanSearch size={19} strokeWidth={1.6} />
          </span>
          <span className="leading-none">
            <span className="block font-playfair text-[24px] font-semibold tracking-tight text-[var(--primary-dark)]">
              AfterWord
            </span>
            <span className="mt-1 hidden text-[8.5px] font-medium tracking-[0.22em] text-[var(--text-muted)] sm:block">
              A WORLD OF UNANSWERED QUESTIONS
            </span>
          </span>
        </Link>

        {/* Center links */}
        <ul className="hidden items-center gap-9 lg:flex">
          {links.map((l) => (
            <li key={l.label}>
              <Link
                to={l.to}
                aria-current={isActive(l) ? "page" : undefined}
                className={`nav-link text-[15px] ${
                  isActive(l) ? "is-active text-[var(--primary)]" : "text-[var(--text-primary)]"
                }`}
              >
                {l.label}
              </Link>
            </li>
          ))}
        </ul>

        {/* Right */}
        <div className="hidden items-center gap-6 lg:flex">
          <Link
            to="/login"
            className="text-[15px] text-[var(--text-secondary)] transition-colors hover:text-[var(--primary)]"
          >
            Log In
          </Link>
          <Link
            to="/register"
            className="rounded-full bg-[var(--primary)] px-6 py-2.5 text-[14.5px] font-medium text-[var(--background)] transition-all duration-300 hover:-translate-y-0.5 hover:bg-[var(--primary-dark)]"
          >
            Start Exploring
          </Link>
        </div>

        {/* Mobile toggle */}
        <button
          className="grid h-11 w-11 place-items-center rounded-full border border-[var(--border)] text-[var(--primary-dark)] lg:hidden"
          onClick={() => setOpen((o) => !o)}
          aria-expanded={open}
          aria-controls="mobile-menu"
          aria-label={open ? "Close menu" : "Open menu"}
        >
          {open ? <X size={20} /> : <Menu size={20} />}
        </button>
      </nav>

      <AnimatePresence>
        {open && (
          <motion.div
            id="mobile-menu"
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.35, ease: [0.22, 1, 0.36, 1] }}
            className="overflow-hidden border-t border-[var(--border)] bg-[var(--background)] lg:hidden"
          >
            <ul className="mx-auto max-w-[1320px] px-5 py-4 sm:px-8">
              {links.map((l, i) => (
                <motion.li
                  key={l.label}
                  initial={{ opacity: 0, x: -12 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.05 * i + 0.1 }}
                  className="border-b border-[var(--border)]"
                >
                  <Link to={l.to} className="flex items-baseline justify-between py-4 font-playfair text-2xl text-[var(--primary-dark)]">
                    {l.label}
                    <span className="text-sm text-[var(--accent)]">0{i + 1}</span>
                  </Link>
                </motion.li>
              ))}
              <li className="flex flex-col gap-3 pb-4 pt-6">
                <Link to="/register" className="rounded-full bg-[var(--primary)] px-6 py-3.5 text-center font-medium text-[var(--background)]">
                  Start Exploring
                </Link>
                <Link to="/login" className="rounded-full border border-[var(--border)] px-6 py-3.5 text-center text-[var(--text-primary)]">
                  Log In
                </Link>
              </li>
            </ul>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}