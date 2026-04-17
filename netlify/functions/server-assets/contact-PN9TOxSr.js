import { jsx, jsxs } from "react/jsx-runtime";
import { ArrowLeft } from "lucide-react";
import { useState } from "react";
function ContactPage() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: ""
  });
  const [isLoading, setIsLoading] = useState(false);
  const [successMessage, setSuccessMessage] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const handleChange = (e) => {
    const {
      name,
      value
    } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value
    }));
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setSuccessMessage("");
    setErrorMessage("");
    try {
      const apiUrl = "http://localhost:8000";
      const response = await fetch(`${apiUrl}/contact`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
      });
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Failed to send message");
      }
      const data = await response.json();
      setSuccessMessage(data.message);
      setFormData({
        name: "",
        email: "",
        message: ""
      });
    } catch (error) {
      setErrorMessage(error instanceof Error ? error.message : "Failed to send message. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };
  return /* @__PURE__ */ jsx("div", { className: "min-h-screen bg-black/90 text-white", children: /* @__PURE__ */ jsxs("div", { className: "mx-auto max-w-2xl px-6 md:px-12 py-20", children: [
    /* @__PURE__ */ jsxs("a", { href: "/", className: "inline-flex items-center gap-2 text-white/60 hover:text-white transition-colors mb-6", children: [
      /* @__PURE__ */ jsx(ArrowLeft, { className: "h-4 w-4" }),
      "Back to Home"
    ] }),
    /* @__PURE__ */ jsx("h1", { className: "text-4xl md:text-5xl font-bold mb-8", children: "Contact Us" }),
    /* @__PURE__ */ jsx("p", { className: "text-white/80 mb-12", children: "Have questions or feedback about Cosmos? We'd love to hear from you. Fill out the form below and we'll get back to you as soon as possible." }),
    /* @__PURE__ */ jsxs("form", { onSubmit: handleSubmit, className: "space-y-6", children: [
      successMessage && /* @__PURE__ */ jsx("div", { className: "p-4 bg-green-500/20 border border-green-500 rounded text-green-100", children: successMessage }),
      errorMessage && /* @__PURE__ */ jsx("div", { className: "p-4 bg-red-500/20 border border-red-500 rounded text-red-100", children: errorMessage }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("label", { htmlFor: "name", className: "block text-white mb-2", children: "Name" }),
        /* @__PURE__ */ jsx("input", { type: "text", id: "name", name: "name", value: formData.name, onChange: handleChange, required: true, disabled: isLoading, className: "w-full px-4 py-2 bg-white/10 border border-white/20 rounded text-white placeholder-white/50 focus:outline-none focus:border-white/50 disabled:opacity-50", placeholder: "Your name" })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("label", { htmlFor: "email", className: "block text-white mb-2", children: "Email" }),
        /* @__PURE__ */ jsx("input", { type: "email", id: "email", name: "email", value: formData.email, onChange: handleChange, required: true, disabled: isLoading, className: "w-full px-4 py-2 bg-white/10 border border-white/20 rounded text-white placeholder-white/50 focus:outline-none focus:border-white/50 disabled:opacity-50", placeholder: "your@email.com" })
      ] }),
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("label", { htmlFor: "message", className: "block text-white mb-2", children: "Message" }),
        /* @__PURE__ */ jsx("textarea", { id: "message", name: "message", value: formData.message, onChange: handleChange, required: true, disabled: isLoading, rows: 6, className: "w-full px-4 py-2 bg-white/10 border border-white/20 rounded text-white placeholder-white/50 focus:outline-none focus:border-white/50 resize-none disabled:opacity-50", placeholder: "Your message here..." })
      ] }),
      /* @__PURE__ */ jsx("button", { type: "submit", disabled: isLoading, className: "w-full px-6 py-3 bg-white text-black font-semibold rounded hover:bg-white/90 transition-colors disabled:opacity-50 disabled:cursor-not-allowed", children: isLoading ? "Sending..." : "Send Message" })
    ] }),
    /* @__PURE__ */ jsxs("div", { className: "mt-16 pt-8 border-t border-white/20", children: [
      /* @__PURE__ */ jsx("h2", { className: "text-xl font-semibold text-white mb-4", children: "Other Ways to Reach Us" }),
      /* @__PURE__ */ jsxs("div", { className: "space-y-3 text-white/80", children: [
        /* @__PURE__ */ jsx("p", { children: "Email: contact@cosmos.dev" }),
        /* @__PURE__ */ jsx("p", { children: "Twitter: @CosmosExplorer" }),
        /* @__PURE__ */ jsx("p", { children: "GitHub: github.com/cosmos" })
      ] })
    ] })
  ] }) });
}
export {
  ContactPage as component
};
