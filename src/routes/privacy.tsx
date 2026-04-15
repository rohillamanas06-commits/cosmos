import { createFileRoute } from "@tanstack/react-router";
import { ArrowLeft } from "lucide-react";

export const Route = createFileRoute("/privacy")({
  head: () => ({
    meta: [
      { title: "Privacy Policy - Cosmos" },
    ],
  }),
  component: PrivacyPage,
});

function PrivacyPage() {
  return (
    <div className="min-h-screen bg-black/90 text-white">
      <div className="mx-auto max-w-4xl px-6 md:px-12 py-20">
        <a href="/" className="inline-flex items-center gap-2 text-white/60 hover:text-white transition-colors mb-6"><ArrowLeft className="h-4 w-4" />Back to Home</a>
        <h1 className="text-4xl md:text-5xl font-bold mb-8">Privacy Policy</h1>
        
        <div className="space-y-8 text-white/80 leading-relaxed">
          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Introduction</h2>
            <p>
              Cosmos ("we", "us", "our") operates the website. This page informs you of our policies regarding the collection, use, and disclosure of personal data when you use our service and the choices you have associated with that data.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Information Collection and Use</h2>
            <p>We collect several different types of information for various purposes to provide and improve our service to you.</p>
            
            <h3 className="text-lg font-semibold text-white mt-4 mb-2">Types of Data Collected:</h3>
            <ul className="list-disc list-inside space-y-2">
              <li><strong>Personal Data:</strong> While using our service, we may ask you to provide us with certain personally identifiable information that can be used to contact or identify you ("Personal Data"). This may include: Email address, First and last name, Cookies and usage data</li>
              <li><strong>Usage Data:</strong> We may also collect information on how the service is accessed and used ("Usage Data"). This may include your computer's Internet Protocol address, browser type, the pages you visit, the time and date of your visit, and other diagnostic data.</li>
            </ul>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Use of Data</h2>
            <p>Cosmos uses the collected data for various purposes:</p>
            <ul className="list-disc list-inside space-y-2 mt-3">
              <li>To provide and maintain our service</li>
              <li>To notify you about changes to our service</li>
              <li>To allow you to participate in interactive features of our service</li>
              <li>To provide customer support</li>
              <li>To gather analysis or valuable information so that we can improve our service</li>
              <li>To monitor the usage of our service</li>
              <li>To detect, prevent and address technical and security issues</li>
            </ul>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Security of Data</h2>
            <p>
              The security of your data is important to us but remember that no method of transmission over the Internet or method of electronic storage is 100% secure. While we strive to use commercially acceptable means to protect your Personal Data, we cannot guarantee its absolute security.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Changes to This Privacy Policy</h2>
            <p>
              We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page and updating the "effective date" at the bottom of this Privacy Policy.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Contact Us</h2>
            <p>
              If you have any questions about this Privacy Policy, please contact us at privacy@cosmos.dev
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
