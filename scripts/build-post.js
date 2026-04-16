import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.join(__dirname, '..');
const distDir = path.join(rootDir, 'dist');
const clientDir = path.join(distDir, 'client');
const serverDir = path.join(distDir, 'server');
const apiDir = path.join(rootDir, 'api');
const publicDir = path.join(rootDir, 'public');
const distPublicDir = path.join(distDir, 'public');

// Function to copy directory recursively
const copyDir = (src, dest) => {
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }
  const files = fs.readdirSync(src);
  files.forEach(file => {
    const srcPath = path.join(src, file);
    const destPath = path.join(dest, file);
    if (fs.statSync(srcPath).isDirectory()) {
      copyDir(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  });
};

// Copy public assets to dist/public for server to serve
if (fs.existsSync(publicDir)) {
  copyDir(publicDir, distPublicDir);
  console.log('✓ Copied public assets to dist/public/');
}

// Clean up api directory
if (fs.existsSync(apiDir)) {
  fs.rmSync(apiDir, { recursive: true, force: true });
}

// Create single Vercel serverless function
if (fs.existsSync(serverDir)) {
  fs.mkdirSync(apiDir, { recursive: true });
  
  const serverFile = path.join(serverDir, 'server.js');
  if (fs.existsSync(serverFile)) {
    // Copy only server.js to api/ (server.js is self-contained)
    fs.copyFileSync(serverFile, path.join(apiDir, 'server.js'));
  }
  
  // Create handler that imports local server
  const handler = `import { server } from './server.js';

export default async function handler(request) {
  return await server.fetch(request);
}
`;
  
  fs.writeFileSync(path.join(apiDir, 'index.js'), handler);
  console.log('✓ Created single serverless function (api/index.js + api/server.js)');
}

// Ensure client assets are accessible
if (fs.existsSync(clientDir)) {
  console.log('✓ Client assets available at dist/client/');
}

console.log('✓ Build post-processing complete');











