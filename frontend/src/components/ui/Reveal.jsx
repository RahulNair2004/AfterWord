import { motion, useReducedMotion } from "framer-motion";

/**
 * Scroll-reveal wrapper. Fades + lifts content once as it enters the viewport.
 * Respects prefers-reduced-motion (renders content with no movement).
 */
export default function Reveal({
  children,
  delay = 0,
  y = 24,
  scale = 1,
  className = "",
  as = "div",
  once = true,
  ...rest
}) {
  const reduce = useReducedMotion();
  const Comp = motion[as] || motion.div;
  return (
    <Comp
      className={className}
      initial={reduce ? false : { opacity: 0, y, scale: scale === 1 ? 1 : 0.96 }}
      whileInView={{ opacity: 1, y: 0, scale: 1 }}
      viewport={{ once, margin: "-80px" }}
      transition={{ duration: 0.8, delay, ease: [0.22, 1, 0.36, 1] }}
      {...rest}
    >
      {children}
    </Comp>
  );
}