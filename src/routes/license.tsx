import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/license")({
  head: () => ({
    meta: [
      { title: "License - Cosmos" },
    ],
  }),
  component: LicensePage,
});

function LicensePage() {
  return (
    <div className="min-h-screen bg-black/90 text-white">
      <div className="mx-auto max-w-4xl px-6 md:px-12 py-20">
        <a href="/" className="text-white/60 hover:text-white transition-colors mb-6 inline-block">Back to Home</a>
        <h1 className="text-4xl md:text-5xl font-bold mb-8">License</h1>
        
        <div className="space-y-8 text-white/80 leading-relaxed">
          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Cosmos License</h2>
            <p>
              Cosmos is provided under the MIT License, which permits free use, modification, and distribution of the software, subject to the terms and conditions below.
            </p>
          </div>

          <div className="p-6 bg-white/10 border border-white/20 rounded font-mono text-sm">
            <p>MIT License</p>
            <p className="mt-3">Copyright (c) 2026 Cosmos Contributors</p>
            <p className="mt-3">
              Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
            </p>
            <p className="mt-3">
              The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
            </p>
            <p className="mt-3">
              THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Data License</h2>
            <p>
              The astronomical data provided by Cosmos is sourced from publicly available astronomical databases and is provided for educational and research purposes.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Attribution</h2>
            <p>
              When using data or code from Cosmos, we appreciate attribution to the Cosmos project. While not required by the MIT License, attribution helps support the project and allows others to discover our work.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Third-Party Licenses</h2>
            <p>
              Cosmos uses various open-source libraries and frameworks. Each of these maintains its own license. Please refer to the dependencies used in the project for their respective licenses.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Contributing</h2>
            <p>
              We welcome contributions to Cosmos! By contributing code, you agree that your contributions will be licensed under the same MIT License.
            </p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold text-white mb-3">Questions?</h2>
            <p>
              If you have any questions about the license, please contact us at license@cosmos.dev
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
