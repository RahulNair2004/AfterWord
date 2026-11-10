import { Link } from "react-router-dom";
import { cases } from "../../data/cases";
import CaseCard from "./CaseCard";
import SectionLabel from "./SectionLabel";
import Reveal from "../ui/Reveal";

export default function FeaturedCases() {
  const [a, b, c] = cases;
  return (
    <section id="featured-cases" className="paper bg-[var(--background)] py-24 sm:py-32">
      <div className="mx-auto max-w-[1320px] px-5 sm:px-8">
        <div className="grid items-end gap-8 lg:grid-cols-12">
          <div className="lg:col-span-7">
            <Reveal>
              <SectionLabel>FROM THE CASE ARCHIVE</SectionLabel>
            </Reveal>
            <Reveal delay={0.08}>
              <h2 className="font-playfair mt-6 text-[clamp(2.4rem,5vw,4.4rem)] font-medium leading-[1.04] tracking-[-0.02em] text-[var(--text-primary)]">
                Stories waiting to be <em className="text-[var(--primary)]">uncovered.</em>
              </h2>
            </Reveal>
          </div>
          <Reveal delay={0.15} className="lg:col-span-4 lg:col-start-9">
            <p className="text-[17px] leading-[1.7] text-[var(--text-secondary)]">
              Explore investigations that leave more questions than answers.
            </p>
          </Reveal>
        </div>

        {/* Asymmetric grid: one tall feature, two compact cards stacked */}
        <div className="mt-14 grid gap-6 lg:grid-cols-12 lg:gap-8">
          <div className="lg:col-span-7">
            <CaseCard item={a} variant="feature" index={0} />
          </div>
          <div className="flex flex-col gap-6 lg:col-span-5 lg:gap-8">
            <CaseCard item={b} variant="compact" index={1} />
            <CaseCard item={c} variant="compact" index={2} />
          </div>
        </div>

        <Reveal className="mt-12 flex justify-end">
          <Link
            to="/cases"
            className="group inline-flex items-center gap-2 border-b border-[var(--primary)] pb-1 font-medium text-[var(--primary)] transition-colors hover:border-[var(--accent)] hover:text-[var(--accent)]"
          >
            Explore the entire archive
            <span aria-hidden="true" className="transition-transform group-hover:translate-x-1">→</span>
          </Link>
        </Reveal>
      </div>
    </section>
  );
}