import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.join(__dirname, '..');
const distDir = path.join(rootDir, 'dist');
const clientDir = path.join(distDir, 'client');
const serverDir = path.join(distDir, 'server');

// Move client build to root
if (fs.existsSync(clientDir)) {
  // Get all files from client directory
  const files = fs.readdirSync(clientDir, { recursive: true });
  let mainJsFile = '';
  
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
      
      // Find the main index JS file
      if (file === 'index.html') {
        // Read existing index.html if it exists
        fs.readFileSync(destPath, 'utf-8');
      } else if (file.match(/^assets\/index-[\w]+\.js$/)) {
        mainJsFile = file;
      }
    }
  });
  
  // Create index.html if it doesn't exist
  const indexPath = path.join(distDir, 'index.html');
  if (!fs.existsSync(indexPath)) {
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
    <script type="module" src="/${mainJsFile}"></script>
  </body>
</html>`;
    fs.writeFileSync(indexPath, html);
  }
  
  // Remove client and server directories
  fs.rmSync(clientDir, { recursive: true, force: true });
  fs.rmSync(serverDir, { recursive: true, force: true });
  
  console.log('✓ Build optimized for Vercel static hosting');
}

