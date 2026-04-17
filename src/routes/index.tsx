import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Cosmos — Explore the Universe" },
    ],
  }),
  component: LandingPage,
});

function LandingPage() {
  return (
    <div className="w-full bg-black text-white">
      {/* Navbar */}
      <nav className="fixed top-0 left-0 right-0 z-50 bg-black/90 backdrop-blur-md border-b border-white/10">
        <div className="flex items-center px-6 md:px-12 py-4">
          <a href="/" className="font-semibold text-white hover:text-white/80 transition-colors">
            Cosmos
          </a>
          <div className="ml-auto flex items-center gap-6 md:gap-8 flex-wrap">
            <a href="/explore" className="text-sm text-white/60 hover:text-white transition-colors">
              Explore
            </a>
            <a href="/about" className="text-sm text-white/60 hover:text-white transition-colors">
              About
            </a>
            <a href="/contact" className="text-sm text-white/60 hover:text-white transition-colors">
              Contact
            </a>
            <a href="/terms" className="text-sm text-white/60 hover:text-white transition-colors">
              Terms
            </a>
            <a href="/privacy" className="text-sm text-white/60 hover:text-white transition-colors">
              Privacy
            </a>
            <a href="/cookies" className="text-sm text-white/60 hover:text-white transition-colors">
              Cookies
            </a>
            <a href="/license" className="text-sm text-white/60 hover:text-white transition-colors">
              License
            </a>
          </div>
        </div>
      </nav>

      {/* Hero - full screen image */}
      <div className="relative w-full h-screen overflow-hidden">
        <img
          src="/pawel-nolbert-62OK9xwVA0c-unsplash.jpg"
          alt="Cosmos hero"
          className="w-full h-full object-cover"
          width={1920}
          height={1080}
        />
        <div className="absolute inset-0 bg-gradient-to-b from-black/20 via-transparent to-black/60" />
      </div>

      {/* Footer */}
      <footer className="bg-black border-t border-white/10">
        <div className="w-full px-6 md:px-12 py-20">
          <div className="grid grid-cols-1 md:grid-cols-5 gap-16 mb-16">
            {/* Brand */}
            <div>
              <div className="mb-6">
                <span className="font-display text-lg font-bold">Cosmos</span>
              </div>
              <p className="text-sm text-white/60 mb-6">
                An interactive encyclopedia of the universe. Explore 169 cosmic objects with rich scientific data.
              </p>
              <div className="flex gap-4">
                <a
                  href="https://github.com/rohillamanas06-commits/cosmos"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-white/60 hover:text-white transition-colors"
                  title="GitHub"
                >
                  <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
                  </svg>
                </a>
                <a
                  href="https://www.linkedin.com/in/manas-rohilla-b73415338/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-white/60 hover:text-white transition-colors"
                  title="LinkedIn"
                >
                  <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z" />
                  </svg>
                </a>
                <a
                  href="mailto:rohillamanas06@gmail.com"
                  className="text-white/60 hover:text-white transition-colors"
                  title="Email"
                >
                  <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" />
                  </svg>
                </a>
              </div>
            </div>

            {/* Product */}
            <div>
              <h3 className="font-display font-semibold text-white mb-6">Product</h3>
              <ul className="space-y-3">
                <li>
                  <a href="/explore" className="text-sm text-white/60 hover:text-white transition-colors">
                    Cosmos Explorer
                  </a>
                </li>
              </ul>
            </div>

            {/* Other Products */}
            <div>
              <h3 className="font-display font-semibold text-white mb-6">Other Products</h3>
              <ul className="space-y-3">
                <li>
                  <a href="https://www.resuai.co.in/" target="_blank" rel="noopener noreferrer" className="text-sm text-white/60 hover:text-white transition-colors">
                    ResuAI
                  </a>
                </li>
                <li>
                  <a href="https://med-mate-ai-health-assistant-v2.vercel.app/" target="_blank" rel="noopener noreferrer" className="text-sm text-white/60 hover:text-white transition-colors">
                    Med-Mate
                  </a>
                </li>
                <li>
                  <a href="https://newsscope-ai-news-detector.vercel.app/" target="_blank" rel="noopener noreferrer" className="text-sm text-white/60 hover:text-white transition-colors">
                    NewsScope
                  </a>
                </li>
                <li>
                  <a href="https://cortex-ai-v1.vercel.app/" target="_blank" rel="noopener noreferrer" className="text-sm text-white/60 hover:text-white transition-colors">
                    Cortex
                  </a>
                </li>
              </ul>
            </div>

            {/* Company */}
            <div>
              <h3 className="font-display font-semibold text-white mb-6">Company</h3>
              <ul className="space-y-3">
                <li>
                  <a href="/about" className="text-sm text-white/60 hover:text-white transition-colors">
                    About Us
                  </a>
                </li>
                <li>
                  <a href="/contact" className="text-sm text-white/60 hover:text-white transition-colors">
                    Contact Us
                  </a>
                </li>
                <li>
                  <a href="/faq" className="text-sm text-white/60 hover:text-white transition-colors">
                    FAQ
                  </a>
                </li>
              </ul>
            </div>

            {/* Legal */}
            <div>
              <h3 className="font-display font-semibold text-white mb-6">Legal</h3>
              <ul className="space-y-3">
                <li>
                  <a href="/terms" className="text-sm text-white/60 hover:text-white transition-colors">
                    Terms of Service
                  </a>
                </li>
                <li>
                  <a href="/privacy" className="text-sm text-white/60 hover:text-white transition-colors">
                    Privacy Policy
                  </a>
                </li>
                <li>
                  <a href="/cookies" className="text-sm text-white/60 hover:text-white transition-colors">
                    Cookie Policy
                  </a>
                </li>
                <li>
                  <a href="/license" className="text-sm text-white/60 hover:text-white transition-colors">
                    License
                  </a>
                </li>
              </ul>
            </div>
          </div>

          <div className="border-t border-white/10 pt-8">
            <p className="text-sm text-white/40">
              © 2026 Cosmos. An open cosmic encyclopedia. Data sourced from astronomical databases.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}