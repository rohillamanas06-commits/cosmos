import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/cookies")({
  head: () => ({
    meta: [
      { title: "Cookie Policy - Cosmos" },
    ],
  }),
  component: CookiePage,
});

function CookiePage() {
  return (
    <div className="min-h-screen bg-black/90 text-white">
      <div className="mx-auto max-w-4xl px-6 md:px-12 py-20">
        <a href="/" className="text-white/60 hover:text-white transition-colors mb-6 inline-block">Back to Home</a>
        <h1 className="text-4xl md:text-5xl font-bold mb-8">Cookie Policy</h1>
        
        <div className="space-y-8 text-white/80 leading-relaxed">
          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">What Are Cookies?</h2>
            <p>
              Cookies are small pieces of data stored on your device (computer, mobile phone, or tablet) when you visit a website. They help websites remember information about you, such as your preferences or login information.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">How We Use Cookies</h2>
            <p>Cosmos uses cookies for the following purposes:</p>
            <ul className="list-disc list-inside space-y-2 mt-3">
              <li><strong>Essential Cookies:</strong> These are necessary for the website to function properly, including user authentication and security features.</li>
              <li><strong>Performance Cookies:</strong> These help us analyze how you use the website, which pages are popular, and improve website performance.</li>
              <li><strong>Functional Cookies:</strong> These remember your preferences and choices to provide a personalized experience.</li>
              <li><strong>Analytics Cookies:</strong> These collect anonymous data about how visitors use our site.</li>
            </ul>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Third-Party Cookies</h2>
            <p>
              Some cookies may be placed by third-party services integrated with Cosmos, such as analytics providers. These cookies are subject to the privacy policies of those third parties.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Managing Your Cookies</h2>
            <p>
              You have the right to choose whether to accept or reject cookies. Most web browsers allow you to control cookies through their settings. You can typically find these settings in the "Preferences" or "Settings" menu of your browser.
            </p>
            <div className="mt-3 p-4 bg-white/5 border border-white/20 rounded">
              <p className="text-sm">Please note that disabling cookies may affect the functionality of Cosmos and your ability to access certain features.</p>
            </div>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Your Rights</h2>
            <p>
              You have the right to access, modify, or delete cookies stored on your device. You can do this through your browser settings or by contacting us directly.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Changes to This Cookie Policy</h2>
            <p>
              We may update this Cookie Policy from time to time to reflect changes in our practice or for other operational, legal, or regulatory reasons. We encourage you to review this policy periodically.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Contact Us</h2>
            <p>
              If you have questions about our use of cookies, please contact us at privacy@cosmos.dev
            </p>
          </div>

          <p className="text-sm text-white/60 mt-12">
            Last updated: April 2026
          </p>
        </div>
      </div>
    </div>
  );
}
