import { createFileRoute } from "@tanstack/react-router";
import { ArrowLeft } from "lucide-react";

export const Route = createFileRoute("/about")({
  head: () => ({
    meta: [
      { title: "About - Cosmos" },
    ],
  }),
  component: AboutPage,
});

function AboutPage() {
  return (
    <div className="min-h-screen bg-black/90 text-white">
      <div className="mx-auto max-w-4xl px-6 md:px-12 py-20">
        <a href="/" className="inline-flex items-center gap-2 text-white/60 hover:text-white transition-colors mb-6"><ArrowLeft className="h-4 w-4" />Back to Home</a>
        <h1 className="text-4xl md:text-5xl font-bold mb-8">About Cosmos</h1>
        
        <div className="space-y-6 text-white/80 leading-relaxed">
          <p>
            Cosmos is an interactive encyclopedia dedicated to exploring and understanding the universe. Our mission is to make astronomical data and cosmic objects accessible to everyone, from casual stargazers to serious astronomers.
          </p>
          
          <h2 className="text-2xl font-semibold text-white mt-8 mb-4">Our Mission</h2>
          <p>
            We believe that knowledge about the cosmos should be freely accessible to all. By aggregating rich scientific data about 169+ cosmic objects, we provide a comprehensive resource for learning about galaxies, nebulae, stars, and other celestial phenomena.
          </p>
          
          <h2 className="text-2xl font-semibold text-white mt-8 mb-4">What We Offer</h2>
          <ul className="list-disc list-inside space-y-2 text-white/80">
            <li>Detailed information on over 169 cosmic objects</li>
            <li>Advanced filtering and search capabilities</li>
            <li>Data sourced from astronomical databases</li>
            <li>Easy-to-use interface for exploring the universe</li>
            <li>Structured information by category and difficulty level</li>
          </ul>
          
          <h2 className="text-2xl font-semibold text-white mt-8 mb-4">Data</h2>
          <p>
            Our data is carefully curated from reputable astronomical sources and organized into phases, with difficulty levels ranging from Beginner to Expert. Whether you're just starting to explore the cosmos or you're an advanced astronomer, we have information to suit your needs.
          </p>
          
          <p className="mt-8">
            Thank you for using Cosmos. We hope it enhances your journey through the universe.
          </p>
        </div>
      </div>
    </div>
  );
}
