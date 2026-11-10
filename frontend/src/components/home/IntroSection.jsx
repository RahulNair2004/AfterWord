import { Link } from "react-router-dom";
import { motion, useReducedMotion } from "framer-motion";
import SectionLabel from "./SectionLabel";
import Reveal from "../ui/Reveal";

/** "The AfterWord idea" — spacious editorial statement on deep-leaning green-cream. */
export default function IntroSection() {
  const reduce = useReducedMotion();
  return (
    <section id="about" className="relative overflow-hidden bg-[var(--accent-soft)]/45 py-24 sm:py-32">
      {/* oversized quotation mark */}
      <motion.span
        aria-hidden="true"
        initial={reduce ? false : { opacity: 0, y: 40 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 1.2, ease: [0.22, 1, 0.36, 1] }}
        className="font-dmserif pointer-events-none absolute -left-4 -top-10 select-none text-[clamp(16rem,38vw,34rem)] leading-none text-[var(--primary)]/[0.08]"
      >
        “
      </motion.span>

      <div className="relative mx-auto grid max-w-[1320px] gap-12 px-5 sm:px-8 lg:grid-cols-12">
        <div className="lg:col-span-3">
          <Reveal>
            <SectionLabel>THE AFTERWORD IDEA</SectionLabel>
          </Reveal>
        </div>

        <div className="lg:col-span-8 lg:col-start-4">
          <Reveal delay={0.1}>
            <h2 className="font-playfair text-[clamp(2.4rem,5.6vw,5rem)] font-medium leading-[1.05] tracking-[-0.02em] text-[var(--primary-dark)]">
              A mystery is never <br className="hidden sm:block" />
              just <em className="text-[var(--accent)]">one</em> story.
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="mt-10 max-w-[42rem] font-playfair text-[clamp(1.15rem,1.9vw,1.5rem)] leading-[1.65] text-[var(--text-primary)]/85">
              One piece of evidence can change an entire narrative. One overlooked detail can
              challenge everything we thought we knew. AfterWord brings curious minds together to
              explore what lies between the facts.
            </p>
          </Reveal>
          <Reveal delay={0.3}>
            <Link
              to="/#how-it-works"
              className="group mt-9 inline-flex items-center gap-2 border-b border-[var(--primary)] pb-1 font-medium text-[var(--primary)] transition-colors hover:border-[var(--accent)] hover:text-[var(--accent)]"
            >
              Discover our approach
              <span aria-hidden="true" className="transition-transform group-hover:translate-x-1">→</span>
            </Link>
          </Reveal>
        </div>
      </div>
    </section>
  );
}