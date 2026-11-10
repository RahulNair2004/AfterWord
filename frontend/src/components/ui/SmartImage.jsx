import { useState } from "react";
import { ImageOff } from "lucide-react";

/**
 * <img> with a graceful, on-brand fallback if the URL fails to load.
 * `tone` is the fallback background; `label` is the caption shown inside it.
 */
export default function SmartImage({
  src,
  alt,
  className = "",
  imgClassName = "",
  tone = "linear-gradient(135deg,#D9D4C3,#BDB8A4)",
  label,
}) {
  const [failed, setFailed] = useState(false);
  if (failed || !src) {
    return (
      <div
        role="img"
        aria-label={alt}
        className={`flex flex-col items-center justify-center gap-2 text-white/80 ${className}`}
        style={{ background: tone }}
      >
        <ImageOff size={22} strokeWidth={1.4} aria-hidden="true" />
        {label && <span className="font-playfair italic text-sm px-4 text-center">{label}</span>}
      </div>
    );
  }
  return (
    <div className={`overflow-hidden ${className}`} style={{ background: tone }}>
      <img
        src={src}
        alt={alt}
        loading="lazy"
        onError={() => setFailed(true)}
        className={`h-full w-full object-cover ${imgClassName}`}
      />
    </div>
  );
}