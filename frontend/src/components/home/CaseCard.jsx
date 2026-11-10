import { Link } from "react-router-dom";
import { motion, useReducedMotion } from "framer-motion";
import { FileText, Lightbulb } from "lucide-react";
import SmartImage from "../ui/SmartImage";
import Badge from "../ui/Badge";

// Different photographic treatment per case.
const treatments = {
  warm: {
    img: "sepia-[.2] saturate-[.9] contrast-[1.05]",
    overlay: "linear-gradient(to top, rgba(216,117,72,0.28), transparent 55%)",
  },
  cool: {
    img: "grayscale-[.55] contrast-[1.05] brightness-[.95]",
    overlay: "linear-gradient(to top, rgba(70,95,120,0.38), rgba(70,95,120,0.1))",
  },
  sepia: {
    img: "sepia-[.7] contrast-[1.02]",
    overlay: "linear-gradient(to top, rgba(120,90,40,0.25), transparent 60%)",
  },
};

/**
 * variant="feature": tall, large image, large title.
 * variant="compact": image beside text on md+, stacked on mobile.
 */
export default function CaseCard({ item, variant = "feature", index = 0 }) {
  const reduce = useReducedMotion();
  const t = treatments[item.treatment];
  const feature = variant === "feature";

  return (
    <motion.article
      initial={reduce ? false : { opacity: 0, y: 40 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-60px" }}
      transition={{ duration: 0.9, delay: index * 0.15, ease: [0.22, 1, 0.36, 1] }}
      whileHover={reduce ? undefined : { y: -4 }}
      className={`group relative flex h-full border border-[var(--border)] bg-[var(--surface)] transition-shadow duration-500 hover:shadow-[0_24px_40px_-30px_rgba(36,41,35,0.45)] ${
        feature ? "flex-col" : "flex-col sm:flex-row"
      }`}
    >
      {/* image */}
      <div
        className={`relative overflow-hidden ${
          feature ? "aspect-[4/3.4] sm:aspect-[4/3.1]" : "aspect-[16/10] sm:aspect-auto sm:w-[44%] sm:shrink-0"
        }`}
      >
        <SmartImage
          src={item.image}
          alt={`${item.title}: ${item.fallbackLabel}`}
          tone={item.tone}
          label={item.fallbackLabel}
          className="h-full w-full"
          imgClassName={`${t.img} transition-transform duration-[1400ms] ease-out group-hover:scale-[1.04]`}
        />
        <div className="pointer-events-none absolute inset-0" style={{ background: t.overlay }} aria-hidden="true" />
        <div className="absolute left-4 top-4 flex items-center gap-2">
          <span className="bg-[var(--background)] px-2.5 py-1 text-[11px] font-semibold tracking-[0.16em] text-[var(--primary-dark)]">
            CASE NO. {item.caseNo}
          </span>
        </div>
        <span
          aria-hidden="true"
          className="font-playfair absolute bottom-3 right-5 text-6xl font-medium italic text-white/80 drop-shadow"
        >
          {item.number}
        </span>
      </div>

      {/* text */}
      <div className={`flex flex-1 flex-col ${feature ? "p-7 sm:p-9" : "p-6 sm:p-7"}`}>
        <div className="flex flex-wrap items-center gap-x-3 gap-y-2">
          <span className="flex items-center gap-2 text-[12px] font-medium tracking-[0.14em] text-[var(--text-secondary)] uppercase">
            <span className="h-2 w-2 rounded-full bg-[var(--accent)]" aria-hidden="true" />
            {item.category}
          </span>
          <Badge tone="green" dot>
            {item.status}
          </Badge>
        </div>

        <h3
          className={`font-playfair mt-5 font-medium leading-[1.1] tracking-[-0.01em] text-[var(--text-primary)] ${
            feature ? "text-[clamp(1.9rem,3.2vw,2.9rem)]" : "text-[clamp(1.5rem,2.2vw,1.9rem)]"
          }`}
        >
          {item.title}
        </h3>
        <p className="mb-7 mt-4 max-w-[34rem] text-[15.5px] leading-[1.7] text-[var(--text-secondary)]">
          {item.description}
        </p>

        <div className="mt-auto flex items-center justify-between gap-4 border-t border-[var(--border)] pt-5">
          <dl className="flex items-center gap-5 text-[14px] text-[var(--text-secondary)]">
            <div className="flex items-center gap-1.5">
              <FileText size={15} className="text-[var(--primary)]" aria-hidden="true" />
              <dt className="sr-only">Evidence</dt>
              <dd>
                <b className="font-semibold text-[var(--text-primary)]">{item.evidence}</b> evidence
              </dd>
            </div>
            <div className="flex items-center gap-1.5">
              <Lightbulb size={15} className="text-[var(--primary)]" aria-hidden="true" />
              <dt className="sr-only">Theories</dt>
              <dd>
                <b className="font-semibold text-[var(--text-primary)]">{item.theories}</b> theories
              </dd>
            </div>
          </dl>
          <Link
            to={`/cases/${item.id}`}
            className="nav-link shrink-0 text-[14.5px] font-medium text-[var(--primary)] after:absolute after:inset-0 focus-visible:outline-none"
          >
            View investigation →
          </Link>
        </div>
      </div>
    </motion.article>
  );
}