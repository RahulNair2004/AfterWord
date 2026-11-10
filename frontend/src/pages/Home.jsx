import { useEffect } from "react";
import { useLocation } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import HeroSection from "../components/home/HeroSection";
import IntroSection from "../components/home/IntroSection";
import FeaturedCases from "../components/home/FeaturedCases";
import WhyAfterWord from "../components/home/Why";
import HowItWorks from "../components/home/HowItWorks";
import CommunitySection from "../components/home/Community";
import AISection from "../components/home/AISection";
import FinalCTA from "../components/home/CTA";

export default function Home() {
  const { hash } = useLocation();

  // React Router doesn't scroll to #anchors by itself.
  useEffect(() => {
    if (!hash) {
      window.scrollTo({ top: 0 });
      return;
    }
    const el = document.getElementById(hash.slice(1));
    if (el) requestAnimationFrame(() => el.scrollIntoView({ behavior: "smooth", block: "start" }));
  }, [hash]);

  return (
    <>
      <a href="#main" className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[100] focus:bg-[var(--primary)] focus:px-4 focus:py-2 focus:text-white">
        Skip to content
      </a>
      <Navbar />
      <main id="main" className="overflow-x-clip">
        {/* <HeroSection /> */}
        {/* <IntroSection />
        <FeaturedCases />
        <WhyAfterWord />
        <HowItWorks />
        <CommunitySection />
        <AISection />
        <FinalCTA /> */}
      </main>
      <Footer />
    </>
  );
}