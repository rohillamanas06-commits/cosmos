import { createFileRoute } from "@tanstack/react-router";
import { ArrowLeft } from "lucide-react";
import { useState } from "react";

export const Route = createFileRoute("/contact")({
  head: () => ({
    meta: [
      { title: "Contact - Cosmos" },
    ],
  }),
  component: ContactPage,
});

function ContactPage() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: "",
  });
  const [isLoading, setIsLoading] = useState(false);
  const [successMessage, setSuccessMessage] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setSuccessMessage("");
    setErrorMessage("");

    try {
      const apiUrl = import.meta.env.VITE_API_URL || "http://localhost:8000";
      const response = await fetch(`${apiUrl}/contact`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Failed to send message");
      }

      const data = await response.json();
      setSuccessMessage(data.message);
      setFormData({ name: "", email: "", message: "" });
    } catch (error) {
      setErrorMessage(error instanceof Error ? error.message : "Failed to send message. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-black/90 text-white">
      <div className="mx-auto max-w-2xl px-6 md:px-12 py-20">
        <a href="/" className="inline-flex items-center gap-2 text-white/60 hover:text-white transition-colors mb-6"><ArrowLeft className="h-4 w-4" />Back to Home</a>
        <h1 className="text-4xl md:text-5xl font-bold mb-8">Contact Us</h1>
        
        <p className="text-white/80 mb-12">
          Have questions or feedback about Cosmos? We'd love to hear from you. Fill out the form below and we'll get back to you as soon as possible.
        </p>

        <form onSubmit={handleSubmit} className="space-y-6">
          {successMessage && (
            <div className="p-4 bg-green-500/20 border border-green-500 rounded text-green-100">
              {successMessage}
            </div>
          )}
          
          {errorMessage && (
            <div className="p-4 bg-red-500/20 border border-red-500 rounded text-red-100">
              {errorMessage}
            </div>
          )}
          
          <div>
            <label htmlFor="name" className="block text-white mb-2">Name</label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
              disabled={isLoading}
              className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded text-white placeholder-white/50 focus:outline-none focus:border-white/50 disabled:opacity-50"
              placeholder="Your name"
            />
          </div>

          <div>
            <label htmlFor="email" className="block text-white mb-2">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              disabled={isLoading}
              className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded text-white placeholder-white/50 focus:outline-none focus:border-white/50 disabled:opacity-50"
              placeholder="your@email.com"
            />
          </div>

          <div>
            <label htmlFor="message" className="block text-white mb-2">Message</label>
            <textarea
              id="message"
              name="message"
              value={formData.message}
              onChange={handleChange}
              required
              disabled={isLoading}
              rows={6}
              className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded text-white placeholder-white/50 focus:outline-none focus:border-white/50 resize-none disabled:opacity-50"
              placeholder="Your message here..."
            />
          </div>

          <button
            type="submit"
            disabled={isLoading}
            className="w-full px-6 py-3 bg-white text-black font-semibold rounded hover:bg-white/90 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isLoading ? "Sending..." : "Send Message"}
          </button>
        </form>

        <div className="mt-16 pt-8 border-t border-white/20">
          <h2 className="text-xl font-semibold text-white mb-4">Other Ways to Reach Us</h2>
          <div className="space-y-3 text-white/80">
            <p>Email: contact@cosmos.dev</p>
            <p>Twitter: @CosmosExplorer</p>
            <p>GitHub: github.com/cosmos</p>
          </div>
        </div>
      </div>
    </div>
  );
}
