import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.join(__dirname, '..');
const distDir = path.join(rootDir, 'dist');
const clientDir = path.join(distDir, 'client');
const serverDir = path.join(distDir, 'server');
const apiDir = path.join(rootDir, 'api');

// Copy server.js to api/ for Vercel serverless deployment
if (fs.existsSync(serverDir)) {
  const serverFile = path.join(serverDir, 'server.js');
  
  if (fs.existsSync(serverFile)) {
    // Create api directory if it doesn't exist
    if (!fs.existsSync(apiDir)) {
      fs.mkdirSync(apiDir, { recursive: true });
    }
    
    // Copy server.js to api/index.js for Vercel
    fs.copyFileSync(serverFile, path.join(apiDir, 'index.js'));
    console.log('✓ Copied server.js to api/index.js for Vercel deployment');
  }
}

// Ensure client assets are accessible
if (fs.existsSync(clientDir)) {
  console.log('✓ Client assets available at dist/client/');
}

// Verify public assets are included
const publicDir = path.join(rootDir, 'public');
const distPublicDir = path.join(distDir, 'public');
if (fs.existsSync(publicDir) && !fs.existsSync(distPublicDir)) {
  console.log('⚠ Public assets not copied to dist/ - server.js should serve from public/');
}

console.log('✓ Build post-processing complete');




