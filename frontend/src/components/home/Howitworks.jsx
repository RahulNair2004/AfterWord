import SectionLabel from "./SectionLabel";
import Reveal from "../ui/Reveal";
import InvestigationSteps from "./InvestigationSteps";

export default function HowItWorks() {
  return (
    <section id="how-it-works" className="scroll-mt-20 bg-[var(--background)] py-24 sm:py-32">
      <div className="mx-auto max-w-[1320px] px-5 sm:px-8">
        <Reveal>
          <SectionLabel>HOW IT WORKS</SectionLabel>
        </Reveal>
        <Reveal delay={0.08}>
          <h2 className="font-playfair mt-6 max-w-3xl text-[clamp(2.4rem,5vw,4.4rem)] font-medium leading-[1.04] tracking-[-0.02em] text-[var(--text-primary)]">
            Three steps. <em className="text-[var(--primary)]">Endless possibilities.</em>
          </h2>
        </Reveal>
        <InvestigationSteps />
      </div>
    </section>
  );
}