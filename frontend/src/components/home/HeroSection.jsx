import { motion, useReducedMotion } from "framer-motion";
import Button from "../ui/Button";
import SectionLabel from "./SectionLabel";
import HeroVisual from "./HeroVisual";

export default function HeroSection() {
  const reduce = useReducedMotion();
  const container = {
    hidden: {},
    show: { transition: { staggerChildren: reduce ? 0 : 0.12, delayChildren: 0.1 } },
  };
  const item = {
    hidden: reduce ? { opacity: 1 } : { opacity: 0, y: 30 },
    show: { opacity: 1, y: 0, transition: { duration: 0.9, ease: [0.22, 1, 0.36, 1] } },
  };

  return (
    <section className="paper relative overflow-hidden">
      <div className="mx-auto grid max-w-330x items-center gap-12 px-5 pb-20 pt-12 sm:px-8 lg:min-h-[calc(100vh-78px)] lg:grid-cols-12 lg:gap-8 lg:pb-24 lg:pt-10">
        {/* Left */}
        <motion.div
          variants={container}
          initial="hidden"
          animate="show"
          className="relative z-10 lg:col-span-6"
        >
          <motion.div variants={item}>
            <SectionLabel>FOR THE CURIOUS MINDS</SectionLabel>
          </motion.div>

          <motion.h1
            variants={item}
            className="font-playfair mt-7 text-[clamp(2.6rem,6.2vw,5.4rem)] font-semibold leading-[1.02] tracking-[-0.02em] text-(--text-primary)"
          >
            Some stories are{" "}
            <span className="relative inline-block whitespace-nowrap italic text-(--primary)">
              never finished.
              <svg
                className="absolute -bottom-2 left-0 w-full"
                viewBox="0 0 300 14"
                fill="none"
                preserveAspectRatio="none"
                aria-hidden="true"
              >
                <path
                  className="draw"
                  pathLength="1"
                  d="M2 9 C 60 2, 110 13, 170 6 S 260 4, 298 9"
                  stroke="var(--accent)"
                  strokeWidth="3"
                  strokeLinecap="round"
                  style={{ "--d": "1.1s" }}
                />
              </svg>
            </span>
          </motion.h1>

          <motion.p
            variants={item}
            className="font-dmserif mt-5 text-[clamp(1.6rem,3.2vw,2.7rem)] leading-[1.12] text-(--text-primary)/90"
          >
            Some questions deserve to be{" "}
            <span className="text-(--accent)]">investigated.</span>
          </motion.p>

          <motion.p
            variants={item}
            className="mt-7 max-w-136 text-[17.5px] leading-[1.7] text-(--text-secondary)"
          >
            Step into a world of unanswered questions. Discover mysteries, examine evidence,
            challenge theories, and uncover perspectives you might have missed.
          </motion.p>

          <motion.div variants={item} className="mt-9 flex flex-col gap-3 sm:flex-row sm:items-center sm:gap-4">
            <Button to="/cases" arrow className="w-full sm:w-auto">
              Explore Investigations
            </Button>
            <Button href="#how-it-works" variant="outline" className="w-full sm:w-auto">
              How AfterWord Works
            </Button>
          </motion.div>

          <motion.div variants={item} className="mt-10 flex items-center gap-4">
            <svg width="54" height="30" viewBox="0 0 54 30" fill="none" aria-hidden="true">
              <path d="M2 22 C 14 4, 32 2, 48 14" stroke="var(--accent)" strokeWidth="1.6" strokeLinecap="round" />
              <path d="M40 8 L49 15 L38 20" stroke="var(--accent)" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
            <p className="font-playfair text-[17px] italic text-(--text-secondary)">
              Discover. Question. Connect. Investigate.
            </p>
          </motion.div>
        </motion.div>

        {/* Right */}
        <div className="relative lg:col-span-6">
          {/* <HeroVisual /> */}
        </div>
      </div>
    </section>
  );
}