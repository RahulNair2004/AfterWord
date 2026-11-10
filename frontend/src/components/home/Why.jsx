import { Search, Users } from "lucide-react";
import Reveal from "../ui/Reveal";
import SectionLabel from "./SectionLabel";

/** Four feature blocks, each with its own typographic/visual treatment. */
export default function WhyAfterWord() {
  return (
    <section className="bg-[var(--background-secondary)] py-24 sm:py-32">
      <div className="mx-auto grid max-w-[1320px] gap-14 px-5 sm:px-8 lg:grid-cols-12">
        {/* Sticky heading */}
        <div className="lg:col-span-5">
          <div className="lg:sticky lg:top-28">
            <Reveal>
              <SectionLabel>WHY AFTERWORD</SectionLabel>
            </Reveal>
            <Reveal delay={0.08}>
              <h2 className="font-playfair mt-6 text-[clamp(2.4rem,4.8vw,4.3rem)] font-medium leading-[1.04] tracking-[-0.02em] text-[var(--text-primary)]">
                Not just reading the mystery.{" "}
                <em className="text-[var(--accent)]">Being part of it.</em>
              </h2>
            </Reveal>
            <Reveal delay={0.16}>
              <p className="mt-6 max-w-sm text-[16px] leading-[1.7] text-[var(--text-secondary)]">
                Most mysteries are consumed once and forgotten. Here, they stay open.
              </p>
            </Reveal>
          </div>
        </div>

        {/* Blocks */}
        <div className="grid gap-6 sm:grid-cols-2 lg:col-span-7">
          {/* 1 — Look closer: magnified words */}
          <Reveal className="relative overflow-hidden border border-[var(--border)] bg-[var(--surface)] p-8 sm:col-span-2 sm:p-10">
            <span className="font-playfair absolute right-6 top-2 text-[7rem] font-medium italic leading-none text-[var(--primary)]/10" aria-hidden="true">
              1
            </span>
            <div className="relative">
              <h3 className="font-playfair text-[2.2rem] font-medium text-[var(--text-primary)]">Look closer</h3>
              <p className="mt-3 max-w-md text-[16px] leading-[1.7] text-[var(--text-secondary)]">
                Examine the details, explore evidence, and find connections others might overlook.
              </p>
              <p className="mt-8 max-w-lg font-playfair text-[1.15rem] leading-[1.9] text-[var(--text-muted)]">
                The letter was dated the{" "}
                <span className="relative mx-1 inline-block rounded-sm bg-[var(--accent-soft)] px-1 text-[var(--text-primary)] ring-2 ring-[var(--accent)]/70 ring-offset-2 ring-offset-[var(--surface)]">
                  fourteenth
                  <Search size={15} className="absolute -right-2 -top-3 text-[var(--accent)]" aria-hidden="true" />
                </span>
                , but the storm began on the fifteenth.
              </p>
            </div>
          </Reveal>

          {/* 2 — Think differently: green panel */}
          <Reveal delay={0.1} className="relative flex flex-col justify-between bg-[var(--primary)] p-8 text-[var(--background)] sm:p-9">
            <span className="font-playfair text-[3.5rem] font-medium italic leading-none text-[var(--accent)]" aria-hidden="true">2</span>
            <div className="mt-16">
              <h3 className="font-playfair text-[2rem] font-medium">Think differently</h3>
              <p className="mt-3 text-[15.5px] leading-[1.7] text-[var(--background)]/80">
                Build your own explanations and explore alternative interpretations.
              </p>
              <p className="mt-6 flex items-center gap-3 font-playfair text-lg italic text-[var(--accent-soft)]">
                <span className="line-through decoration-[var(--accent)]/80">An accident</span>
                <span aria-hidden="true">→</span>
                <span>Staged?</span>
              </p>
            </div>
          </Reveal>

          {/* 3 — Challenge ideas: paper slip */}
          <Reveal delay={0.2} className="relative flex flex-col justify-between border border-dashed border-[var(--text-primary)]/30 bg-[var(--surface-soft)] p-8 sm:p-9">
            <span className="font-playfair text-[3.5rem] font-medium italic leading-none text-[var(--primary)]" aria-hidden="true">3</span>
            <div className="mt-16">
              <h3 className="font-playfair text-[2rem] font-medium text-[var(--text-primary)]">Challenge ideas</h3>
              <p className="mt-3 text-[15.5px] leading-[1.7] text-[var(--text-secondary)]">
                Question assumptions, discuss competing theories, and make your case.
              </p>
              <p className="font-hand mt-5 -rotate-2 text-[22px] text-[var(--accent)]">“But what about the window?”</p>
            </div>
          </Reveal>

          {/* 4 — Investigate together */}
          <Reveal delay={0.1} className="border border-[var(--border)] bg-[var(--surface)] p-8 sm:col-span-2 sm:flex sm:items-center sm:justify-between sm:gap-8 sm:p-10">
            <div>
              <span className="font-playfair text-[3.5rem] font-medium italic leading-none text-[var(--accent)]" aria-hidden="true">4</span>
              <h3 className="font-playfair mt-6 text-[2.2rem] font-medium text-[var(--text-primary)]">Investigate together</h3>
              <p className="mt-3 max-w-md text-[16px] leading-[1.7] text-[var(--text-secondary)]">
                Join a community where curiosity is encouraged and perspectives matter.
              </p>
            </div>
            <div className="mt-8 flex items-center sm:mt-0" aria-hidden="true">
              {["#244C3B", "#D87548", "#92958B", "#19382B"].map((c, i) => (
                <span
                  key={c}
                  className="-ml-4 grid h-14 w-14 place-items-center rounded-full border-[3px] border-[var(--surface)] first:ml-0"
                  style={{ background: c, zIndex: 4 - i }}
                >
                  <Users size={18} className="text-white/85" />
                </span>
              ))}
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}