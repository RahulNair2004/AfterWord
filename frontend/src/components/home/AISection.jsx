import { Info } from "lucide-react";
import Reveal from "../ui/Reveal";
import SectionLabel from "./SectionLabel";
import AIWorkspacePreview from "./AIWorkspacePreview";

const capabilities = [
  { title: "Case summaries", copy: "Understand complex investigations through structured summaries." },
  { title: "Evidence analysis", copy: "Explore important observations, inconsistencies, and potential implications." },
  { title: "Theory analysis", copy: "Examine the strengths and weaknesses of proposed explanations." },
  { title: "Investigation assistant", copy: "Ask contextual questions about a case and explore its evidence and theories." },
];

export default function AISection() {
  return (
    <section id="ai" className="scroll-mt-20 bg-[var(--background)] py-24 sm:py-32">
      <div className="mx-auto max-w-[1320px] px-5 sm:px-8">
        <div className="grid gap-12 lg:grid-cols-12">
          <div className="lg:col-span-6">
            <Reveal>
              <SectionLabel>AI INVESTIGATION TOOLS</SectionLabel>
            </Reveal>
            <Reveal delay={0.08}>
              <h2 className="font-playfair mt-6 text-[clamp(2.3rem,4.8vw,4.2rem)] font-medium leading-[1.05] tracking-[-0.02em] text-[var(--text-primary)]">
                A little more insight. <em className="text-[var(--accent)]">A lot more to explore.</em>
              </h2>
            </Reveal>
          </div>
          <Reveal delay={0.15} className="lg:col-span-5 lg:col-start-8 lg:self-end">
            <p className="text-[17px] leading-[1.7] text-[var(--text-secondary)]">
              Curiosity leads the investigation. Intelligent tools help you examine the details,
              organize information, and consider possibilities.
            </p>
          </Reveal>
        </div>

        {/* capabilities as an indexed list, not cards */}
        <dl className="mt-14 grid border-y border-[var(--border)] sm:grid-cols-2 lg:grid-cols-4">
          {capabilities.map((c, i) => (
            <Reveal
              key={c.title}
              delay={i * 0.08}
              y={14}
              className="border-b border-[var(--border)] py-6 last:border-b-0 sm:odd:border-r sm:px-6 sm:first:pl-0 lg:border-b-0 lg:border-r lg:last:border-r-0 lg:odd:border-r"
            >
              <dt className="font-playfair text-[1.45rem] font-medium text-[var(--primary-dark)]">{c.title}</dt>
              <dd className="mt-2 text-[15px] leading-[1.65] text-[var(--text-secondary)]">{c.copy}</dd>
            </Reveal>
          ))}
        </dl>

        <div className="mt-14">
          <AIWorkspacePreview />
          <Reveal delay={0.2}>
            <p className="mt-6 flex items-start gap-2 text-[14px] text-[var(--text-secondary)]">
              <Info size={16} className="mt-0.5 shrink-0 text-[var(--accent)]" aria-hidden="true" />
              AI-generated analysis supports critical thinking. It does not establish facts or replace
              independent judgment.
            </p>
          </Reveal>
        </div>
      </div>
    </section>
  );
}