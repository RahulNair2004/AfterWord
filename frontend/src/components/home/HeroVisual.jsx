import { motion, useReducedMotion } from "framer-motion";
import { heroImages } from "../../data/Cases";
import SmartImage from "../ui/SmartImage";

/**
 * Editorial collage. Deliberately lightweight:
 *  - one simple entrance animation per element (opacity / y / rotate), no looping motion
 *  - no CSS filters on photos (tinted with plain overlays instead)
 *  - SVG lines are drawn once with CSS, not animated by JS
 * Everything is positioned in % of one aspect-ratio box, so it scales as a whole.
 */
export default function HeroVisual() {
  const reduce = useReducedMotion();

  const enter = (rotate, delay) => ({
    initial: reduce ? { rotate } : { opacity: 0, y: 30, rotate: rotate * 2 },
    animate: { opacity: 1, y: 0, rotate },
    transition: { duration: 0.9, delay, ease: [0.22, 1, 0.36, 1] },
  });

  return (
    <div className="relative mx-auto aspect-[5/6] w-full max-w-[640px] select-none sm:aspect-[6/6.2]">
      {/* backing sheet */}
      <div
        className="absolute inset-[6%] -rotate-2 border border-[var(--border)] bg-[var(--background-secondary)]"
        aria-hidden="true"
      />

      {/* thread connecting the clues (static, drawn once with CSS) */}
      <svg className="absolute inset-0 h-full w-full" viewBox="0 0 100 100" fill="none" aria-hidden="true">
        <path
          className="draw"
          pathLength="1"
          d="M30 30 C 60 6, 90 18, 86 58 S 52 90, 18 78"
          stroke="var(--accent)"
          strokeWidth="0.4"
          style={{ "--d": "1.2s" }}
        />
      </svg>

      {/* main photograph: the house */}
      <motion.figure
        {...enter(-2, 0.15)}
        className="absolute left-[4%] top-[6%] w-[66%] bg-white p-[2.2%] pb-[7%] shadow-[0_14px_30px_-18px_rgba(36,41,35,0.45)]"
      >
        <div className="relative aspect-[4/5] w-full overflow-hidden">
          <SmartImage
            src={heroImages.house}
            alt="An old house standing alone among tall trees in morning fog"
            className="absolute inset-0"
            tone="linear-gradient(160deg,#52665A,#243229)"
            label="The house in the trees"
          />
          <div className="absolute inset-0 bg-[#7a5a2a]/10" aria-hidden="true" />
        </div>
        <figcaption className="font-hand absolute bottom-[1.5%] left-[6%] text-[clamp(10px,1.6vw,15px)] text-[var(--text-secondary)]">
          Blackwood Manor, north approach
        </figcaption>
      </motion.figure>

      {/* letters */}
      <motion.figure
        {...enter(5, 0.35)}
        className="absolute right-[2%] top-[3%] w-[34%] bg-white p-[1.6%] shadow-[0_12px_26px_-16px_rgba(36,41,35,0.5)]"
      >
        <div className="relative aspect-[4/3] w-full overflow-hidden">
          <SmartImage
            src={heroImages.letters}
            alt="Handwritten letters on aged paper"
            className="absolute inset-0"
            tone="linear-gradient(160deg,#D8C9A8,#B3A27D)"
            label="Handwritten letters"
          />
          <div className="absolute inset-0 bg-[#8a6a30]/20" aria-hidden="true" />
        </div>
        <span
          aria-hidden="true"
          className="absolute -top-[5%] left-[34%] h-[10%] w-[32%] rotate-[-4deg] bg-[var(--accent-soft)]/80"
        />
      </motion.figure>

      {/* newspaper clipping */}
      <motion.figure
        {...enter(-4, 0.5)}
        className="absolute bottom-[10%] right-[4%] w-[40%] bg-[#EFE9D6] p-[1.6%] shadow-[0_12px_26px_-16px_rgba(36,41,35,0.5)]"
      >
        <div className="relative aspect-[5/4] w-full overflow-hidden">
          <SmartImage
            src={heroImages.news}
            alt="An old newspaper clipping"
            className="absolute inset-0"
            tone="linear-gradient(160deg,#D9D2BB,#B7AE92)"
            label="Newspaper clipping"
          />
          <div className="absolute inset-0 bg-[#6b5d3a]/25" aria-hidden="true" />
        </div>
        <p className="font-playfair mt-[4%] text-[clamp(8px,1.4vw,13px)] font-semibold leading-tight text-[var(--text-primary)]">
          Heir Missing; Doors Found Bolted From Within
        </p>
      </motion.figure>

      {/* CASE NO label */}
      <motion.div
        {...enter(-6, 0.7)}
        className="absolute left-[2%] top-[0%] border border-[var(--text-primary)]/20 bg-[#F4EBCF] px-[3%] py-[1.2%] shadow-sm"
      >
        <span className="text-[clamp(8px,1.4vw,12px)] font-semibold tracking-[0.2em] text-[var(--text-primary)]">
          CASE NO. 0248
        </span>
      </motion.div>

      {/* status */}
      <motion.div
        {...enter(0, 0.9)}
        className="absolute bottom-[34%] left-[0%] flex items-center gap-[6px] rounded-full bg-[var(--primary)] px-[3.2%] py-[1.3%] text-[var(--background)] shadow-md"
      >
        <span className="h-[6px] w-[6px] rounded-full bg-[var(--accent)]" />
        <span className="text-[clamp(8px,1.35vw,11.5px)] font-medium tracking-[0.16em]">OPEN INVESTIGATION</span>
      </motion.div>

      {/* note */}
      <motion.div
        {...enter(3, 1)}
        className="absolute bottom-[3%] left-[14%] w-[34%] bg-[#FBF3C6] px-[3%] py-[2.4%] shadow-[0_10px_20px_-14px_rgba(36,41,35,0.6)]"
      >
        <p className="font-hand text-[clamp(11px,2vw,19px)] leading-tight text-[var(--text-primary)]">
          THE DETAILS MATTER
        </p>
      </motion.div>

      {/* numbered markers */}
      {[
        { n: 1, left: "52%", top: "30%" },
        { n: 2, left: "86%", top: "30%" },
        { n: 3, left: "62%", top: "70%" },
      ].map((m, i) => (
        <motion.span
          key={m.n}
          style={{ left: m.left, top: m.top }}
          initial={reduce ? false : { opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.3 + i * 0.15, duration: 0.5 }}
          className="absolute grid h-[6.5%] w-[6.5%] min-h-5 min-w-5 place-items-center rounded-full border-[1.5px] border-[var(--accent)] bg-[var(--background)]/80 text-[clamp(9px,1.4vw,12px)] font-semibold text-[var(--accent)]"
        >
          {m.n}
        </motion.span>
      ))}

      {/* annotation circle + handwritten note (CSS-drawn) */}
      <svg className="absolute left-[34%] top-[16%] h-[16%] w-[18%]" viewBox="0 0 80 60" fill="none" aria-hidden="true">
        <path
          className="draw"
          pathLength="1"
          d="M40 5 C 66 4, 78 20, 70 38 C 62 54, 30 58, 14 44 C 2 32, 8 12, 32 7"
          stroke="var(--accent)"
          strokeWidth="2.2"
          strokeLinecap="round"
          style={{ "--d": "1.5s" }}
        />
      </svg>
      <motion.p
        initial={reduce ? false : { opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 2, duration: 0.6 }}
        className="font-hand absolute left-[48%] top-[13%] hidden rotate-[-4deg] text-[15px] text-[var(--accent)] sm:block"
      >
        light on at 3 a.m.?
      </motion.p>
    </div>
  );
}