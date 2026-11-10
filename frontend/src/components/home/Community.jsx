import { Check } from "lucide-react";
import Button from "../ui/Button";
import Reveal from "../ui/Reveal";
import SectionLabel from "./SectionLabel";
import CommunityPreview from "./CommunityPreview";

const points = [
  "Publish your theories.",
  "Discuss evidence.",
  "Challenge assumptions.",
  "Vote on compelling explanations.",
  "Learn from other perspectives.",
];

export default function CommunitySection() {
  return (
    <section id="community" className="paper scroll-mt-20 bg-[var(--surface-soft)] py-24 sm:py-32">
      <div className="mx-auto grid max-w-[1320px] items-center gap-16 px-5 sm:px-8 lg:grid-cols-12">
        <div className="lg:col-span-5">
          <Reveal>
            <SectionLabel>BETTER QUESTIONS. BETTER TOGETHER.</SectionLabel>
          </Reveal>
          <Reveal delay={0.08}>
            <h2 className="font-playfair mt-6 text-[clamp(2.2rem,4.4vw,3.9rem)] font-medium leading-[1.06] tracking-[-0.02em] text-[var(--text-primary)]">
              The best discoveries happen when{" "}
              <em className="text-[var(--primary)]">perspectives meet.</em>
            </h2>
          </Reveal>
          <Reveal delay={0.16}>
            <p className="mt-6 text-[17px] leading-[1.7] text-[var(--text-secondary)]">
              Everyone notices something different. Share your theories, challenge other
              interpretations, and collaborate with curious minds who see the world a little
              differently.
            </p>
          </Reveal>
          <ul className="mt-8 divide-y divide-[var(--border)] border-y border-[var(--border)]">
            {points.map((p, i) => (
              <Reveal as="li" key={p} delay={0.2 + i * 0.07} y={12} className="flex items-center gap-3 py-3.5 text-[16px] text-[var(--text-primary)]">
                <span className="grid h-5 w-5 place-items-center rounded-full bg-[var(--primary)] text-[var(--background)]" aria-hidden="true">
                  <Check size={12} strokeWidth={3} />
                </span>
                {p}
              </Reveal>
            ))}
          </ul>
          <Reveal delay={0.5} className="mt-9">
            <Button to="/register" arrow className="w-full sm:w-auto">
              Join the Community
            </Button>
          </Reveal>
        </div>

        <div className="lg:col-span-7 lg:pl-8">
          <CommunityPreview />
        </div>
      </div>
    </section>
  );
}