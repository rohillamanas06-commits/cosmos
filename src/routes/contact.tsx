import { createFileRoute } from "@tanstack/react-router";
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

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Form submitted:", formData);
    setFormData({ name: "", email: "", message: "" });
    alert("Thank you for your message. We'll get back to you soon!");
  };

  return (
    <div className="min-h-screen bg-black/90 text-white">
      <div className="mx-auto max-w-2xl px-6 md:px-12 py-20">
        <a href="/" className="text-white/60 hover:text-white transition-colors mb-6 inline-block">Back to Home</a>
        <h1 className="text-4xl md:text-5xl font-bold mb-8">Contact Us</h1>
        
        <p className="text-white/80 mb-12">
          Have questions or feedback about Cosmos? We'd love to hear from you. Fill out the form below and we'll get back to you as soon as possible.
        </p>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label htmlFor="name" className="block text-white mb-2">Name</label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
              className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded text-white placeholder-white/50 focus:outline-none focus:border-white/50"
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
              className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded text-white placeholder-white/50 focus:outline-none focus:border-white/50"
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
              rows={6}
              className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded text-white placeholder-white/50 focus:outline-none focus:border-white/50 resize-none"
              placeholder="Your message here..."
            />
          </div>

          <button
            type="submit"
            className="w-full px-6 py-3 bg-white text-black font-semibold rounded hover:bg-white/90 transition-colors"
          >
            Send Message
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
