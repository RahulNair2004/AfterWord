import { motion, useReducedMotion } from "framer-motion";
import { ArrowBigUp, MessageSquare, BadgeCheck } from "lucide-react";
import Badge from "../ui/Badge";

const threads = [
  {
    author: "Alex Morgan",
    initials: "AM",
    tint: "var(--primary)",
    time: "2h ago",
    theory: "The east-wing window was used as an exit.",
    votes: 24,
    comments: 8,
    reply: {
      author: "Priya Nair",
      initials: "PN",
      text: "The latch has fresh scratches. That fits, but it doesn't explain the bolted door.",
    },
  },
  {
    author: "Jordan Lee",
    initials: "JL",
    tint: "var(--accent)",
    time: "5h ago",
    theory: "The disappearance was staged before the storm.",
    votes: 17,
    comments: 5,
    supported: true,
  },
];

export default function CommunityPreview() {
  const reduce = useReducedMotion();
  const list = {
    hidden: {},
    show: { transition: { staggerChildren: reduce ? 0 : 0.25, delayChildren: 0.15 } },
  };
  const entry = {
    hidden: reduce ? { opacity: 1 } : { opacity: 0, y: 28 },
    show: { opacity: 1, y: 0, transition: { duration: 0.8, ease: [0.22, 1, 0.36, 1] } },
  };

  return (
    <div className="relative">
      <div className="absolute -inset-3 -z-10 rotate-1 border border-[var(--border)] bg-[var(--background-secondary)]" aria-hidden="true" />
      <div className="border border-[var(--border)] bg-[var(--surface)] shadow-[0_24px_44px_-30px_rgba(36,41,35,0.5)]">
        <div className="flex flex-wrap items-center justify-between gap-2 border-b border-[var(--border)] px-5 py-4">
          <div>
            <p className="text-[11px] font-medium tracking-[0.16em] text-[var(--text-muted)]">DISCUSSING</p>
            <p className="font-playfair text-[1.15rem] text-[var(--text-primary)]">The Vanishing at Blackwood Manor</p>
          </div>
          <Badge tone="orange" dot>Case 0248</Badge>
        </div>

        <motion.ul variants={list} initial="hidden" whileInView="show" viewport={{ once: true, margin: "-80px" }} className="divide-y divide-[var(--border)]">
          {threads.map((t) => (
            <motion.li key={t.author} variants={entry} className="p-5 sm:p-6">
              <div className="flex items-center gap-3">
                <span className="grid h-9 w-9 place-items-center rounded-full text-[12px] font-semibold text-white" style={{ background: t.tint }} aria-hidden="true">
                  {t.initials}
                </span>
                <div className="leading-tight">
                  <p className="text-[14px] font-medium text-[var(--text-primary)]">{t.author}</p>
                  <p className="text-[12px] text-[var(--text-muted)]">{t.time} · Theory</p>
                </div>
                {t.supported && (
                  <span className="ml-auto inline-flex items-center gap-1 rounded-full bg-[var(--primary)] px-2.5 py-1 text-[10px] font-medium tracking-[0.12em] text-[var(--background)]">
                    <BadgeCheck size={12} aria-hidden="true" /> SUPPORTED BY EVIDENCE
                  </span>
                )}
              </div>

              <p className="font-playfair mt-4 text-[1.35rem] leading-snug text-[var(--text-primary)]">“{t.theory}”</p>

              <div className="mt-4 flex items-center gap-5 text-[13.5px] text-[var(--text-secondary)]">
                <span className="inline-flex items-center gap-1 text-[var(--primary)]">
                  <ArrowBigUp size={18} aria-hidden="true" />
                  <b className="font-semibold">{t.votes}</b> upvotes
                </span>
                <span className="inline-flex items-center gap-1.5">
                  <MessageSquare size={15} aria-hidden="true" />
                  {t.comments} comments
                </span>
              </div>

              {t.reply && (
                <div className="mt-4 ml-3 border-l-2 border-[var(--accent)] bg-[var(--surface-soft)] px-4 py-3">
                  <p className="text-[12.5px] font-medium text-[var(--text-primary)]">{t.reply.author}</p>
                  <p className="mt-1 text-[14px] leading-relaxed text-[var(--text-secondary)]">{t.reply.text}</p>
                </div>
              )}
            </motion.li>
          ))}
        </motion.ul>
      </div>
    </div>
  );
}