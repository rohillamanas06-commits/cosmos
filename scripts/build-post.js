import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.join(__dirname, '..');
const distDir = path.join(rootDir, 'dist');
const clientDir = path.join(distDir, 'client');
const serverDir = path.join(distDir, 'server');
const assetsDir = path.join(distDir, 'assets');

// Move client build to root
if (fs.existsSync(clientDir)) {
  const files = fs.readdirSync(clientDir, { recursive: true });
  let mainJsFile = '';
  let mainJsSize = 0;
  
  files.forEach(file => {
    const srcPath = path.join(clientDir, file);
    const destPath = path.join(distDir, file);
    
    // Create directories if they don't exist
    const destDir = path.dirname(destPath);
    if (!fs.existsSync(destDir)) {
      fs.mkdirSync(destDir, { recursive: true });
    }
    
    // Only copy files, not directories
    if (fs.statSync(srcPath).isFile()) {
      fs.copyFileSync(srcPath, destPath);
      
      // Find the largest index JS file (main app bundle)
      if (file.match(/assets\/index-[\w]+\.js$/) && !file.includes('arrow-left')) {
        const stats = fs.statSync(destPath);
        if (stats.size > mainJsSize) {
          mainJsFile = file;
          mainJsSize = stats.size;
        }
      }
    }
  });
  
  // Fallback: if not found, search for it
  if (!mainJsFile && fs.existsSync(assetsDir)) {
    const assetFiles = fs.readdirSync(assetsDir);
    assetFiles.forEach(file => {
      if (file.match(/^index-[\w]+\.js$/) && !file.includes('arrow')) {
        const stats = fs.statSync(path.join(assetsDir, file));
        if (stats.size > mainJsSize) {
          mainJsFile = path.join('assets', file);
          mainJsSize = stats.size;
        }
      }
    });
  }
  
  // Create index.html
  const indexPath = path.join(distDir, 'index.html');
  const scriptSrc = mainJsFile ? `/${mainJsFile.replace(/\\/g, '/')}` : '/assets/index.js';
  
  const html = `<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" href="/nasa-Yj1M5riCKk4-unsplash.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Cosmos — Explore the Universe</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="${scriptSrc}"></script>
  </body>
</html>`;
  
  fs.writeFileSync(indexPath, html);
  
  // Remove client and server directories
  fs.rmSync(clientDir, { recursive: true, force: true });
  fs.rmSync(serverDir, { recursive: true, force: true });
  
  console.log(`✓ Build optimized for Vercel (main JS: ${mainJsFile})`);
}



