import { createFileRoute } from "@tanstack/react-router";
import { useState } from "react";

export const Route = createFileRoute("/faq")({
  head: () => ({
    meta: [
      { title: "FAQ - Cosmos" },
    ],
  }),
  component: FAQPage,
});

function FAQPage() {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  const faqs = [
    {
      question: "What is Cosmos?",
      answer: "Cosmos is an interactive encyclopedia of the universe containing detailed information about 169+ cosmic objects including galaxies, nebulae, stars, and other celestial phenomena with rich scientific data.",
    },
    {
      question: "How many cosmic objects are in the database?",
      answer: "We currently have 169 cosmic objects in our database, organized across 5 phases. Each object is carefully curated with scientific data.",
    },
    {
      question: "Is Cosmos free to use?",
      answer: "Yes! Cosmos is completely free to use. Our mission is to make astronomical data accessible to everyone.",
    },
    {
      question: "Can I filter objects by difficulty?",
      answer: "Absolutely. You can filter cosmic objects by difficulty levels: Beginner, Intermediate, Advanced, and Expert.",
    },
    {
      question: "What categories of objects are available?",
      answer: "We have various categories of cosmic objects including galaxies, nebulae, stars, clusters, and more. Use the search feature to explore specific categories.",
    },
    {
      question: "Can I export the data?",
      answer: "Currently, data export is not available, but it's on our roadmap. You can view and search all cosmic objects directly in Cosmos.",
    },
    {
      question: "Where does the data come from?",
      answer: "Our data is sourced from reputable astronomical databases and scientific sources, carefully organized and verified for accuracy.",
    },
    {
      question: "How often is the data updated?",
      answer: "We regularly update our data to include new discoveries and ensure accuracy. Check back often for new cosmic objects and information.",
    },
    {
      question: "How can I contact support?",
      answer: "You can reach us through our Contact page. We respond to inquiries within 24-48 hours.",
    },
  ];

  return (
    <div className="min-h-screen bg-black/90 text-white">
      <div className="mx-auto max-w-3xl px-6 md:px-12 py-20">
        <a href="/" className="text-white/60 hover:text-white transition-colors mb-6 inline-block">Back to Home</a>
        <h1 className="text-4xl md:text-5xl font-bold mb-12">Frequently Asked Questions</h1>

        <div className="space-y-4">
          {faqs.map((faq, index) => (
            <div key={index} className="border border-white/20 rounded">
              <button
                onClick={() => setOpenIndex(openIndex === index ? null : index)}
                className="w-full px-6 py-4 flex items-center justify-between hover:bg-white/5 transition-colors"
              >
                <h3 className="text-lg font-semibold text-left">{faq.question}</h3>
                <span className="text-2xl">{openIndex === index ? "−" : "+"}</span>
              </button>
              
              {openIndex === index && (
                <div className="px-6 py-4 border-t border-white/20 bg-white/5">
                  <p className="text-white/80 leading-relaxed">{faq.answer}</p>
                </div>
              )}
            </div>
          ))}
        </div>

        <div className="mt-12 p-6 bg-white/10 border border-white/20 rounded">
          <p className="text-white/80">
            Still have questions? <a href="/contact" className="text-white hover:text-white/80 underline">Contact us</a> and we'll be happy to help.
          </p>
        </div>
      </div>
    </div>
  );
}
