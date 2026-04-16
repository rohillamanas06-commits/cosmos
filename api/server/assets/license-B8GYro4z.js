import { jsx, jsxs } from "react/jsx-runtime";
import { ArrowLeft } from "lucide-react";
function LicensePage() {
  return /* @__PURE__ */ jsx("div", { className: "min-h-screen bg-black/90 text-white", children: /* @__PURE__ */ jsxs("div", { className: "mx-auto max-w-4xl px-6 md:px-12 py-20", children: [
    /* @__PURE__ */ jsxs("a", { href: "/", className: "inline-flex items-center gap-2 text-white/60 hover:text-white transition-colors mb-6", children: [
      /* @__PURE__ */ jsx(ArrowLeft, { className: "h-4 w-4" }),
      "Back to Home"
    ] }),
    /* @__PURE__ */ jsx("h1", { className: "text-4xl md:text-5xl font-bold mb-8", children: "License" }),
    /* @__PURE__ */ jsxs("div", { className: "space-y-8 text-white/80 leading-relaxed", children: [
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Cosmos License" }),
        /* @__PURE__ */ jsx("p", { children: "Cosmos is provided under the MIT License, which permits free use, modification, and distribution of the software, subject to the terms and conditions below." })
      ] }),
      /* @__PURE__ */ jsxs("div", { className: "p-6 bg-white/10 border border-white/20 rounded font-mono text-sm", children: [
        /* @__PURE__ */ jsx("p", { children: "MIT License" }),
        /* @__PURE__ */ jsx("p", { className: "mt-3", children: "Copyright (c) 2026 Cosmos Contributors" }),
        /* @__PURE__ */ jsx("p", { className: "mt-3", children: 'Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:' }),
        /* @__PURE__ */ jsx("p", { className: "mt-3", children: "The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software." }),
        /* @__PURE__ */ jsx("p", { className: "mt-3", children: 'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.' })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Data License" }),
        /* @__PURE__ */ jsx("p", { children: "The astronomical data provided by Cosmos is sourced from publicly available astronomical databases and is provided for educational and research purposes." })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Attribution" }),
        /* @__PURE__ */ jsx("p", { children: "When using data or code from Cosmos, we appreciate attribution to the Cosmos project. While not required by the MIT License, attribution helps support the project and allows others to discover our work." })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Third-Party Licenses" }),
        /* @__PURE__ */ jsx("p", { children: "Cosmos uses various open-source libraries and frameworks. Each of these maintains its own license. Please refer to the dependencies used in the project for their respective licenses." })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Contributing" }),
        /* @__PURE__ */ jsx("p", { children: "We welcome contributions to Cosmos! By contributing code, you agree that your contributions will be licensed under the same MIT License." })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h2", { className: "text-2xl font-semibold text-white mb-3", children: "Questions?" }),
        /* @__PURE__ */ jsx("p", { children: "If you have any questions about the license, please contact us at license@cosmos.dev" })
      ] }),
      /* @__PURE__ */ jsx("p", { className: "text-sm text-white/60 mt-12", children: "Last updated: April 2026" })
    ] })
  ] }) });
}
export {
  LicensePage as component
};
