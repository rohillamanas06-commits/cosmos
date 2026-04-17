import { jsx, jsxs } from "react/jsx-runtime";
import { ArrowLeft } from "lucide-react";
function AboutPage() {
  return /* @__PURE__ */ jsx("div", { className: "min-h-screen bg-black/90 text-white", children: /* @__PURE__ */ jsxs("div", { className: "mx-auto max-w-4xl px-6 md:px-12 py-20", children: [
    /* @__PURE__ */ jsxs("a", { href: "/", className: "inline-flex items-center gap-2 text-white/60 hover:text-white transition-colors mb-6", children: [
      /* @__PURE__ */ jsx(ArrowLeft, { className: "h-4 w-4" }),
      "Back to Home"
    ] }),
    /* @__PURE__ */ jsx("h1", { className: "text-4xl md:text-5xl font-bold mb-8", children: "About Cosmos" }),
    /* @__PURE__ */ jsxs("div", { className: "space-y-6 text-white/80 leading-relaxed", children: [
      /* @__PURE__ */ jsx("p", { children: "Cosmos is an interactive encyclopedia dedicated to exploring and understanding the universe. Our mission is to make astronomical data and cosmic objects accessible to everyone, from casual stargazers to serious astronomers." }),
      /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mt-8 mb-4", children: "Our Mission" }),
      /* @__PURE__ */ jsx("p", { children: "We believe that knowledge about the cosmos should be freely accessible to all. By aggregating rich scientific data about 169+ cosmic objects, we provide a comprehensive resource for learning about galaxies, nebulae, stars, and other celestial phenomena." }),
      /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mt-8 mb-4", children: "What We Offer" }),
      /* @__PURE__ */ jsxs("ul", { className: "list-disc list-inside space-y-2 text-white/80", children: [
        /* @__PURE__ */ jsx("li", { children: "Detailed information on over 169 cosmic objects" }),
        /* @__PURE__ */ jsx("li", { children: "Advanced filtering and search capabilities" }),
        /* @__PURE__ */ jsx("li", { children: "Data sourced from astronomical databases" }),
        /* @__PURE__ */ jsx("li", { children: "Easy-to-use interface for exploring the universe" }),
        /* @__PURE__ */ jsx("li", { children: "Structured information by category and difficulty level" })
      ] }),
      /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mt-8 mb-4", children: "Data" }),
      /* @__PURE__ */ jsx("p", { children: "Our data is carefully curated from reputable astronomical sources and organized into phases, with difficulty levels ranging from Beginner to Expert. Whether you're just starting to explore the cosmos or you're an advanced astronomer, we have information to suit your needs." }),
      /* @__PURE__ */ jsx("p", { className: "mt-8", children: "Thank you for using Cosmos. We hope it enhances your journey through the universe." })
    ] })
  ] }) });
}
export {
  AboutPage as component
};
