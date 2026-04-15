import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/terms")({
  head: () => ({
    meta: [
      { title: "Terms of Service - Cosmos" },
    ],
  }),
  component: TermsPage,
});

function TermsPage() {
  return (
    <div className="min-h-screen bg-black/90 text-white">
      <div className="mx-auto max-w-4xl px-6 md:px-12 py-20">
        <a href="/" className="text-white/60 hover:text-white transition-colors mb-6 inline-block">Back to Home</a>
        <h1 className="text-4xl md:text-5xl font-bold mb-8">Terms of Service</h1>
        
        <div className="space-y-8 text-white/80 leading-relaxed">
          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">1. Acceptance of Terms</h2>
            <p>
              By accessing and using Cosmos, you accept and agree to be bound by the terms and provision of this agreement. If you do not agree to abide by the above, please do not use this service.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">2. Use License</h2>
            <p>
              Permission is granted to temporarily download one copy of the materials (information or software) on Cosmos for personal, non-commercial transitory viewing only. This is the grant of a license, not a transfer of title, and under this license you may not:
            </p>
            <ul className="list-disc list-inside mt-3 space-y-2">
              <li>Modifying or copying the materials</li>
              <li>Using the materials for any commercial purpose or for any public display</li>
              <li>Attempting to decompile or reverse engineer any software contained on Cosmos</li>
              <li>Removing any copyright or other proprietary notations from the materials</li>
              <li>Transferring the materials to another person or "mirroring" the materials on any other server</li>
            </ul>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">3. Disclaimer</h2>
            <p>
              The materials on Cosmos are provided on an 'as is' basis. Cosmos makes no warranties, expressed or implied, and hereby disclaims and negates all other warranties including, without limitation, implied warranties or conditions of merchantability, fitness for a particular purpose, or non-infringement of intellectual property or other violation of rights.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">4. Limitations</h2>
            <p>
              In no event shall Cosmos or its suppliers be liable for any damages (including, without limitation, damages for loss of data or profit, or due to business interruption) arising out of the use or inability to use the materials on Cosmos, even if Cosmos or an authorized representative has been notified orally or in writing of the possibility of such damage.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">5. Accuracy of Materials</h2>
            <p>
              The materials appearing on Cosmos could include technical, typographical, or photographic errors. Cosmos does not warrant that any of the materials on its website are accurate, complete, or current. Cosmos may make changes to the materials contained on its website at any time without notice.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">6. Links</h2>
            <p>
              Cosmos has not reviewed all of the sites linked to its website and is not responsible for the contents of any such linked site. The inclusion of any link does not imply endorsement by Cosmos of the site. Use of any such linked website is at the user's own risk.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">7. Modifications</h2>
            <p>
              Cosmos may revise these terms of service for its website at any time without notice. By using this website, you are agreeing to be bound by the then current version of these terms of service.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">8. Governing Law</h2>
            <p>
              These terms and conditions are governed by and construed in accordance with the laws of the jurisdiction in which Cosmos is located, and you irrevocably submit to the exclusive jurisdiction of the courts in that location.
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
