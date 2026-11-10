// Sample data for the homepage only. No API calls.
// Images are Unsplash photos; every <SmartImage> falls back gracefully if a URL fails.
// Swap in your own photography at any time by editing `image`.
const u = (id, w = 1400) => `https://images.unsplash.com/${id}?auto=format&fit=crop&w=${w}&q=80`;

export const heroImages = {
  house: u("photo-1448375240586-882707db888b", 1400),
  letters: u("photo-1455390582262-044cdead277a", 800),
  news: u("photo-1457369804613-52c61a468e7d", 800),
};

export const cases = [
  {
    id: "blackwood-manor",
    number: "01",
    caseNo: "0248",
    title: "The Vanishing at Blackwood Manor",
    description:
      "A locked estate. An empty bedroom. A final letter that raises more questions than answers.",
    category: "Disappearance",
    status: "Active Investigation",
    evidence: 12,
    theories: 8,
    image: u("photo-1448375240586-882707db888b", 1600),
    treatment: "warm",
    tone: "linear-gradient(160deg,#3B4A3F,#1E2A22)",
    fallbackLabel: "Blackwood Manor, in fog",
  },
  {
    id: "the-last-signal",
    number: "02",
    caseNo: "0251",
    title: "The Last Signal",
    description:
      "A transmission appeared on an abandoned frequency. Its origin remains unknown, and its final message has never been decoded.",
    category: "Unexplained Phenomenon",
    status: "Under Investigation",
    evidence: 9,
    theories: 14,
    image: u("photo-1593078165899-c7d2ac0d6aea", 1200),
    treatment: "cool",
    tone: "linear-gradient(160deg,#8794A0,#4D5A66)",
    fallbackLabel: "A radio, still tuned",
  },
  {
    id: "ashford-letters",
    number: "03",
    caseNo: "0262",
    title: "The Ashford Letters",
    description:
      "Three letters surfaced decades apart, each describing an event before it happened. Coincidence, deception, or something stranger?",
    category: "Historical Mystery",
    status: "Open Case",
    evidence: 16,
    theories: 11,
    image: u("photo-1495364141860-b0d03eccd065", 1200),
    treatment: "sepia",
    tone: "linear-gradient(160deg,#CDBB98,#9C8760)",
    fallbackLabel: "Three letters, one hand",
  },
];