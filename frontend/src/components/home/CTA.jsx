import { motion, useReducedMotion } from "framer-motion";
import Button from "../ui/Button";
import SectionLabel from "./SectionLabel";

export default function FinalCTA() {
  const reduce = useReducedMotion();
  const markers = [
    { n: 1, cls: "left-[8%] top-[18%]" },
    { n: 2, cls: "right-[10%] top-[26%]" },
    { n: 3, cls: "right-[22%] bottom-[14%]" },
  ];
  return (
    <section className="grain relative overflow-hidden bg-[var(--primary-dark)] py-28 text-[var(--background)] sm:py-40">
      {/* decorative investigation markers + thread */}
      <svg className="pointer-events-none absolute inset-0 h-full w-full opacity-40" viewBox="0 0 100 100" preserveAspectRatio="none" fill="none" aria-hidden="true">
        <motion.path
          d="M10 22 C 40 8, 70 40, 88 30 S 80 80, 76 86"
          stroke="var(--accent)"
          strokeWidth="0.4"
          strokeDasharray="1.2 1.2"
          vectorEffect="non-scaling-stroke"
          initial={reduce ? false : { pathLength: 0 }}
          whileInView={{ pathLength: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 2.2, ease: "easeInOut" }}
        />
      </svg>
      {markers.map((m, i) => (
        <motion.span
          key={m.n}
          aria-hidden="true"
          initial={reduce ? false : { opacity: 0, scale: 0 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
          transition={{ delay: 0.6 + i * 0.25, type: "spring", stiffness: 200, damping: 12 }}
          className={`absolute hidden h-9 w-9 place-items-center rounded-full border-[1.5px] border-[var(--accent)] text-[13px] font-semibold text-[var(--accent)] sm:grid ${m.cls}`}
        >
          {m.n}
        </motion.span>
      ))}

      <div className="relative mx-auto max-w-[1320px] px-5 sm:px-8">
        <SectionLabel light>YOUR TURN</SectionLabel>
        <motion.h2
          initial={reduce ? false : { opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 1, ease: [0.22, 1, 0.36, 1] }}
          className="font-playfair mt-8 max-w-5xl text-[clamp(2.8rem,8vw,7.2rem)] font-medium leading-[0.98] tracking-[-0.03em]"
        >
          Every unanswered question is an <em className="text-[var(--accent)]">invitation.</em>
        </motion.h2>

        <div className="mt-12 grid gap-10 lg:grid-cols-12">
          <p className="max-w-xl text-[18px] leading-[1.7] text-[var(--background)]/80 lg:col-span-6">
            Find your next investigation. Bring your perspective. Discover what happens when curious
            minds come together.
          </p>
          <div className="flex flex-col gap-4 sm:flex-row sm:items-center lg:col-span-6 lg:justify-end">
            <Button to="/register" variant="accent" arrow className="w-full sm:w-auto">
              Start Exploring
            </Button>
            <Button to="/cases" variant="outlineLight" className="w-full sm:w-auto">
              Browse Open Cases
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
}