import { motion, useReducedMotion } from "framer-motion";
import { Search, FileText, MessageSquare, ThumbsUp } from "lucide-react";
import Reveal from "../ui/Reveal";

/* ---------- Three miniature illustrations ---------- */

function ArchiveMini() {
  const rows = [
    ["0248", "Blackwood Manor", true],
    ["0251", "The Last Signal", false],
    ["0262", "The Ashford Letters", false],
  ];
  return (
    <div className="border border-[var(--border)] bg-[var(--surface)] p-4 shadow-[0_12px_24px_-20px_rgba(36,41,35,0.5)]" aria-hidden="true">
      <div className="flex items-center gap-2 border border-[var(--border)] bg-[var(--background)] px-3 py-2 text-[12px] text-[var(--text-muted)]">
        <Search size={13} /> Search the archive
      </div>
      <ul className="mt-3 space-y-2">
        {rows.map(([n, t, on]) => (
          <li
            key={n}
            className={`flex items-center justify-between border px-3 py-2.5 text-[13px] ${
              on ? "border-[var(--primary)] bg-[var(--primary)]/[0.06]" : "border-[var(--border)]"
            }`}
          >
            <span className="font-playfair text-[var(--text-primary)]">{t}</span>
            <span className="text-[11px] tracking-widest text-[var(--text-muted)]">{n}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

function BoardMini() {
  return (
    <div className="relative h-[200px] border border-[var(--border)] bg-[#E7DFC9] p-4 shadow-[0_12px_24px_-20px_rgba(36,41,35,0.5)]" aria-hidden="true">
      <svg className="absolute inset-0 h-full w-full" viewBox="0 0 100 100" preserveAspectRatio="none" fill="none">
        <path d="M24 30 L58 24 L72 68 L30 70 Z" stroke="var(--accent)" strokeWidth="0.5" strokeDasharray="1.5 1.5" vectorEffect="non-scaling-stroke" />
      </svg>
      {[
        { l: "6%", t: "10%", r: -3, c: "#FBF3C6", txt: "Note, 9:40pm" },
        { l: "50%", t: "6%", r: 3, c: "#FFFFFF", txt: "Letter" },
        { l: "56%", t: "58%", r: -2, c: "#F2DCCF", txt: "Photo" },
        { l: "8%", t: "58%", r: 2, c: "#FFFFFF", txt: "Receipt" },
      ].map((d) => (
        <div
          key={d.txt}
          className="absolute w-[34%] px-2 py-3 text-center font-playfair text-[12px] text-[var(--text-primary)] shadow"
          style={{ left: d.l, top: d.t, background: d.c, transform: `rotate(${d.r}deg)` }}
        >
          <span className="absolute -top-1 left-1/2 h-2 w-2 -translate-x-1/2 rounded-full bg-[var(--accent)]" />
          {d.txt}
        </div>
      ))}
    </div>
  );
}

function DiscussionMini() {
  return (
    <div className="space-y-3 border border-[var(--border)] bg-[var(--surface)] p-4 shadow-[0_12px_24px_-20px_rgba(36,41,35,0.5)]" aria-hidden="true">
      <div className="border border-[var(--border)] p-3">
        <p className="font-playfair text-[13.5px] text-[var(--text-primary)]">“The window was the exit.”</p>
        <div className="mt-2 flex items-center gap-4 text-[11.5px] text-[var(--text-secondary)]">
          <span className="flex items-center gap-1"><ThumbsUp size={12} /> 24</span>
          <span className="flex items-center gap-1"><MessageSquare size={12} /> 8</span>
        </div>
      </div>
      <div className="ml-6 border-l-2 border-[var(--accent)] pl-3 text-[12.5px] text-[var(--text-secondary)]">
        But the latch was bolted from inside…
      </div>
      <div className="ml-6 border-l-2 border-[var(--primary)] pl-3 text-[12.5px] text-[var(--text-secondary)]">
        Unless it was replaced later.
      </div>
    </div>
  );
}

const steps = [
  {
    n: "01",
    title: "Discover",
    copy: "Find investigations that spark your curiosity. Explore their backgrounds, questions, and unanswered details.",
    visual: <ArchiveMini />,
    color: "var(--primary)",
  },
  {
    n: "02",
    title: "Investigate",
    copy: "Examine evidence, connect observations, and create theories that explain what might have happened.",
    visual: <BoardMini />,
    color: "var(--accent)",
  },
  {
    n: "03",
    title: "Challenge",
    copy: "Share your conclusions, explore opposing theories, and work with other investigators to examine the possibilities.",
    visual: <DiscussionMini />,
    color: "var(--primary)",
  },
];

export default function InvestigationSteps() {
  const reduce = useReducedMotion();
  return (
    <div className="relative mt-20">
      {/* connecting line (desktop) */}
      <div className="absolute left-0 right-0 top-[3.1rem] hidden h-px lg:block" aria-hidden="true">
        <motion.div
          className="h-px origin-left bg-[var(--text-primary)]/25"
          initial={reduce ? false : { scaleX: 0 }}
          whileInView={{ scaleX: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 1.6, ease: "easeInOut" }}
        />
      </div>
      {/* connecting line (mobile) */}
      <div className="absolute bottom-0 left-[1.1rem] top-0 w-px bg-[var(--text-primary)]/20 lg:hidden" aria-hidden="true" />

      <ol className="grid gap-14 lg:grid-cols-3 lg:gap-10">
        {steps.map((s, i) => (
          <Reveal as="li" key={s.n} delay={i * 0.18} className="relative pl-12 lg:pl-0">
            <span
              className="absolute left-[0.6rem] top-3 h-3 w-3 rounded-full ring-4 ring-[var(--background)] lg:left-0 lg:top-[2.85rem]"
              style={{ background: s.color }}
              aria-hidden="true"
            />
            <span
              className="font-playfair block text-[clamp(4.5rem,8vw,7rem)] font-medium italic leading-none lg:pb-3"
              style={{ color: s.color }}
              aria-hidden="true"
            >
              {s.n}
            </span>
            <h3 className="font-playfair mt-4 text-[2rem] font-medium text-[var(--text-primary)]">
              <span className="sr-only">Step {i + 1}: </span>
              {s.title}
            </h3>
            <p className="mt-3 max-w-sm text-[16px] leading-[1.7] text-[var(--text-secondary)]">{s.copy}</p>
            <div className="mt-8">{s.visual}</div>
          </Reveal>
        ))}
      </ol>
    </div>
  );
}