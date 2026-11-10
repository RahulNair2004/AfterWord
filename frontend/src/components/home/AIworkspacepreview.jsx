import { motion, useReducedMotion } from "framer-motion";
import { BookOpen, FileText, Lightbulb, Sparkles, Info, Link2 } from "lucide-react";

const nav = [
  { label: "Case Overview", icon: BookOpen },
  { label: "Evidence", icon: FileText },
  { label: "Theories", icon: Lightbulb },
  { label: "Investigation Assistant", icon: Sparkles, active: true },
];

export default function AIWorkspacePreview() {
  const reduce = useReducedMotion();
  return (
    <motion.div
      initial={reduce ? false : { opacity: 0, y: 40, scale: 0.98 }}
      whileInView={{ opacity: 1, y: 0, scale: 1 }}
      viewport={{ once: true, margin: "-80px" }}
      transition={{ duration: 1, ease: [0.22, 1, 0.36, 1] }}
      className="overflow-hidden border border-[var(--border)] bg-[var(--surface)] shadow-[0_30px_60px_-36px_rgba(36,41,35,0.55)]"
      role="img"
      aria-label="Preview of the AfterWord Investigation Assistant workspace"
    >
      {/* top bar */}
      <div className="flex items-center gap-3 border-b border-[var(--border)] bg-[var(--background)] px-4 py-3">
        <span className="flex gap-1.5" aria-hidden="true">
          <i className="h-2.5 w-2.5 rounded-full bg-[var(--border)]" />
          <i className="h-2.5 w-2.5 rounded-full bg-[var(--border)]" />
          <i className="h-2.5 w-2.5 rounded-full bg-[var(--border)]" />
        </span>
        <span className="font-playfair truncate text-[14px] text-[var(--text-secondary)]">
          Case 0248 · The Vanishing at Blackwood Manor
        </span>
      </div>

      <div className="grid md:grid-cols-[210px_1fr]">
        {/* left nav */}
        <ul className="flex gap-1 overflow-x-auto border-b border-[var(--border)] bg-[var(--surface-soft)] p-3 md:flex-col md:border-b-0 md:border-r md:p-4">
          {nav.map(({ label, icon: Icon, active }) => (
            <li
              key={label}
              className={`flex shrink-0 items-center gap-2.5 px-3 py-2.5 text-[13.5px] ${
                active
                  ? "bg-[var(--primary)] text-[var(--background)]"
                  : "text-[var(--text-secondary)]"
              }`}
            >
              <Icon size={15} aria-hidden="true" />
              {label}
            </li>
          ))}
        </ul>

        {/* main */}
        <div className="p-5 sm:p-8">
          <p className="text-[11px] font-medium tracking-[0.2em] text-[var(--accent)]">ASK THE INVESTIGATION ASSISTANT</p>

          <div className="mt-5 border border-[var(--border)] bg-[var(--background)] px-4 py-3">
            <p className="font-playfair text-[1.15rem] text-[var(--text-primary)]">
              What evidence contradicts the current timeline?
            </p>
          </div>

          <motion.div
            initial={reduce ? false : { opacity: 0, y: 14 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.6, duration: 0.8 }}
            className="mt-5 border-l-[3px] border-[var(--primary)] bg-[var(--surface-soft)] p-5"
          >
            <p className="flex items-center gap-2 text-[12px] font-medium text-[var(--primary)]">
              <Sparkles size={14} aria-hidden="true" /> Assistant
            </p>
            <p className="mt-2 text-[15.5px] leading-[1.7] text-[var(--text-primary)]">
              The recovered note is dated two hours before the reported power outage. If its
              timestamp is accurate, the current timeline may need reconsideration.
            </p>
          </motion.div>

          <div className="mt-5 flex flex-wrap items-center gap-3">
            <span className="inline-flex items-center gap-1.5 border border-[var(--border)] px-3 py-1.5 text-[13px] text-[var(--text-secondary)]">
              <Link2 size={13} className="text-[var(--accent)]" aria-hidden="true" /> Related Evidence: <b className="text-[var(--text-primary)]">#03</b>
            </span>
            <span className="inline-flex items-center gap-1.5 border border-[var(--border)] px-3 py-1.5 text-[13px] text-[var(--text-secondary)]">
              <Link2 size={13} className="text-[var(--accent)]" aria-hidden="true" /> Related Theory: <b className="text-[var(--text-primary)]">#08</b>
            </span>
          </div>

          <p className="mt-5 flex items-start gap-2 text-[12.5px] text-[var(--text-muted)]">
            <Info size={14} className="mt-0.5 shrink-0" aria-hidden="true" />
            Answers draw only on this case’s 12 evidence items and 8 theories.
          </p>
        </div>
      </div>
    </motion.div>
  );
}