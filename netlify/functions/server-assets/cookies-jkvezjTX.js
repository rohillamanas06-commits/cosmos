import { jsx, jsxs } from "react/jsx-runtime";
import { ArrowLeft } from "lucide-react";
function CookiePage() {
  return /* @__PURE__ */ jsx("div", { className: "min-h-screen bg-black/90 text-white", children: /* @__PURE__ */ jsxs("div", { className: "mx-auto max-w-4xl px-6 md:px-12 py-20", children: [
    /* @__PURE__ */ jsxs("a", { href: "/", className: "inline-flex items-center gap-2 text-white/60 hover:text-white transition-colors mb-6", children: [
      /* @__PURE__ */ jsx(ArrowLeft, { className: "h-4 w-4" }),
      "Back to Home"
    ] }),
    /* @__PURE__ */ jsx("h1", { className: "text-4xl md:text-5xl font-bold mb-8", children: "Cookie Policy" }),
    /* @__PURE__ */ jsxs("div", { className: "space-y-8 text-white/80 leading-relaxed", children: [
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "What Are Cookies?" }),
        /* @__PURE__ */ jsx("p", { children: "Cookies are small pieces of data stored on your device (computer, mobile phone, or tablet) when you visit a website. They help websites remember information about you, such as your preferences or login information." })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "How We Use Cookies" }),
        /* @__PURE__ */ jsx("p", { children: "Cosmos uses cookies for the following purposes:" }),
        /* @__PURE__ */ jsxs("ul", { className: "list-disc list-inside space-y-2 mt-3", children: [
          /* @__PURE__ */ jsxs("li", { children: [
            /* @__PURE__ */ jsx("strong", { children: "Essential Cookies:" }),
            " These are necessary for the website to function properly, including user authentication and security features."
          ] }),
          /* @__PURE__ */ jsxs("li", { children: [
            /* @__PURE__ */ jsx("strong", { children: "Performance Cookies:" }),
            " These help us analyze how you use the website, which pages are popular, and improve website performance."
          ] }),
          /* @__PURE__ */ jsxs("li", { children: [
            /* @__PURE__ */ jsx("strong", { children: "Functional Cookies:" }),
            " These remember your preferences and choices to provide a personalized experience."
          ] }),
          /* @__PURE__ */ jsxs("li", { children: [
            /* @__PURE__ */ jsx("strong", { children: "Analytics Cookies:" }),
            " These collect anonymous data about how visitors use our site."
          ] })
        ] })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Third-Party Cookies" }),
        /* @__PURE__ */ jsx("p", { children: "Some cookies may be placed by third-party services integrated with Cosmos, such as analytics providers. These cookies are subject to the privacy policies of those third parties." })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Managing Your Cookies" }),
        /* @__PURE__ */ jsx("p", { children: 'You have the right to choose whether to accept or reject cookies. Most web browsers allow you to control cookies through their settings. You can typically find these settings in the "Preferences" or "Settings" menu of your browser.' }),
        /* @__PURE__ */ jsx("div", { className: "mt-3 p-4 bg-white/5 border border-white/20 rounded", children: /* @__PURE__ */ jsx("p", { className: "text-sm", children: "Please note that disabling cookies may affect the functionality of Cosmos and your ability to access certain features." }) })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Your Rights" }),
        /* @__PURE__ */ jsx("p", { children: "You have the right to access, modify, or delete cookies stored on your device. You can do this through your browser settings or by contacting us directly." })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Changes to This Cookie Policy" }),
        /* @__PURE__ */ jsx("p", { children: "We may update this Cookie Policy from time to time to reflect changes in our practice or for other operational, legal, or regulatory reasons. We encourage you to review this policy periodically." })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Contact Us" }),
        /* @__PURE__ */ jsx("p", { children: "If you have questions about our use of cookies, please contact us at privacy@cosmos.dev" })
      ] }),
      /* @__PURE__ */ jsx("p", { className: "text-sm text-white/60 mt-12", children: "Last updated: April 2026" })
    ] })
  ] }) });
}
export {
  CookiePage as component
};
