import { Link } from "react-router-dom";
import { motion } from "framer-motion";

const MotionLink = motion.create(Link);

const base =
  "group inline-flex items-center justify-center gap-2 font-medium text-[15px] transition-colors duration-300 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--accent)]";

const variants = {
  primary:
    "bg-[var(--primary)] text-[var(--background)] hover:bg-[var(--primary-dark)] rounded-full px-7 py-3.5",
  accent: "bg-[var(--accent)] text-white hover:brightness-95 rounded-full px-7 py-3.5",
  light: "bg-[var(--background)] text-[var(--primary-dark)] hover:bg-white rounded-full px-7 py-3.5",
  outline:
    "border border-[var(--text-primary)]/25 text-[var(--text-primary)] hover:border-[var(--primary)] hover:text-[var(--primary)] rounded-full px-7 py-3.5",
  outlineLight:
    "border border-[var(--background)]/40 text-[var(--background)] hover:border-[var(--background)] rounded-full px-7 py-3.5",
  link: "text-[var(--primary)] hover:text-[var(--accent)] underline underline-offset-[6px] decoration-[var(--accent)]/60 hover:decoration-[var(--accent)] px-0 py-1",
};

/** Renders a router <Link> when `to` is set, an <a> for `href`, else a <button>. */
export default function Button({
  to,
  href,
  variant = "primary",
  className = "",
  children,
  arrow = false,
  ...rest
}) {
  const cls = `${base} ${variants[variant]} ${className}`;
  const content = (
    <>
      {children}
      {arrow && (
        <span
          aria-hidden="true"
          className="inline-block transition-transform duration-300 group-hover:translate-x-1"
        >
          →
        </span>
      )}
    </>
  );
  const hover = { whileHover: { y: -2 }, whileTap: { y: 0 }, transition: { duration: 0.2 } };

  if (to)
    return (
      <MotionLink to={to} className={cls} {...hover} {...rest}>
        {content}
      </MotionLink>
    );
  if (href)
    return (
      <motion.a href={href} className={cls} {...hover} {...rest}>
        {content}
      </motion.a>
    );
  return (
    <motion.button className={cls} {...hover} {...rest}>
      {content}
    </motion.button>
  );
}