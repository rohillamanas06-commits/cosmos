import { jsx, jsxs } from "react/jsx-runtime";
import { ArrowLeft } from "lucide-react";
function PrivacyPage() {
  return /* @__PURE__ */ jsx("div", { className: "min-h-screen bg-black/90 text-white", children: /* @__PURE__ */ jsxs("div", { className: "mx-auto max-w-4xl px-6 md:px-12 py-20", children: [
    /* @__PURE__ */ jsxs("a", { href: "/", className: "inline-flex items-center gap-2 text-white/60 hover:text-white transition-colors mb-6", children: [
      /* @__PURE__ */ jsx(ArrowLeft, { className: "h-4 w-4" }),
      "Back to Home"
    ] }),
    /* @__PURE__ */ jsx("h1", { className: "text-4xl md:text-5xl font-bold mb-8", children: "Privacy Policy" }),
    /* @__PURE__ */ jsxs("div", { className: "space-y-8 text-white/80 leading-relaxed", children: [
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Introduction" }),
        /* @__PURE__ */ jsx("p", { children: 'Cosmos ("we", "us", "our") operates the website. This page informs you of our policies regarding the collection, use, and disclosure of personal data when you use our service and the choices you have associated with that data.' })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Information Collection and Use" }),
        /* @__PURE__ */ jsx("p", { children: "We collect several different types of information for various purposes to provide and improve our service to you." }),
        /* @__PURE__ */ jsx("h3", { className: "text-lg font-semibold text-white mt-4 mb-2", children: "Types of Data Collected:" }),
        /* @__PURE__ */ jsxs("ul", { className: "list-disc list-inside space-y-2", children: [
          /* @__PURE__ */ jsxs("li", { children: [
            /* @__PURE__ */ jsx("strong", { children: "Personal Data:" }),
            ' While using our service, we may ask you to provide us with certain personally identifiable information that can be used to contact or identify you ("Personal Data"). This may include: Email address, First and last name, Cookies and usage data'
          ] }),
          /* @__PURE__ */ jsxs("li", { children: [
            /* @__PURE__ */ jsx("strong", { children: "Usage Data:" }),
            ` We may also collect information on how the service is accessed and used ("Usage Data"). This may include your computer's Internet Protocol address, browser type, the pages you visit, the time and date of your visit, and other diagnostic data.`
          ] })
        ] })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Use of Data" }),
        /* @__PURE__ */ jsx("p", { children: "Cosmos uses the collected data for various purposes:" }),
        /* @__PURE__ */ jsxs("ul", { className: "list-disc list-inside space-y-2 mt-3", children: [
          /* @__PURE__ */ jsx("li", { children: "To provide and maintain our service" }),
          /* @__PURE__ */ jsx("li", { children: "To notify you about changes to our service" }),
          /* @__PURE__ */ jsx("li", { children: "To allow you to participate in interactive features of our service" }),
          /* @__PURE__ */ jsx("li", { children: "To provide customer support" }),
          /* @__PURE__ */ jsx("li", { children: "To gather analysis or valuable information so that we can improve our service" }),
          /* @__PURE__ */ jsx("li", { children: "To monitor the usage of our service" }),
          /* @__PURE__ */ jsx("li", { children: "To detect, prevent and address technical and security issues" })
        ] })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Security of Data" }),
        /* @__PURE__ */ jsx("p", { children: "The security of your data is important to us but remember that no method of transmission over the Internet or method of electronic storage is 100% secure. While we strive to use commercially acceptable means to protect your Personal Data, we cannot guarantee its absolute security." })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Changes to This Privacy Policy" }),
        /* @__PURE__ */ jsx("p", { children: 'We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page and updating the "effective date" at the bottom of this Privacy Policy.' })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Contact Us" }),
        /* @__PURE__ */ jsx("p", { children: "If you have any questions about this Privacy Policy, please contact us at privacy@cosmos.dev" })
      ] }),
      /* @__PURE__ */ jsx("p", { className: "text-sm text-white/60 mt-12", children: "Last updated: April 2026" })
    ] })
  ] }) });
}
export {
  PrivacyPage as component
};
