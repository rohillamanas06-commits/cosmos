import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.join(__dirname, '..');
const distDir = path.join(rootDir, 'dist');

// Check if build was successful
if (!fs.existsSync(distDir)) {
  console.error('✗ Build directory not found. TanStack Start build may have failed.');
  process.exit(1);
}

// List build output for debugging
console.log('✓ Build output structure:');
const listFiles = (dir, prefix = '') => {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  entries.slice(0, 10).forEach(entry => {
    console.log(`  ${prefix}${entry.name}${entry.isDirectory() ? '/' : ''}`);
  });
  if (entries.length > 10) {
    console.log(`  ... and ${entries.length - 10} more items`);
  }
};
listFiles(distDir);

// If this is a TanStack Start server output, no need for manual transformation
if (fs.existsSync(path.join(distDir, 'index.html'))) {
  console.log('✓ TanStack Start build completed successfully for Vercel');
} else {
  console.warn('⚠ index.html not found in dist/ - build may need verification');
}

console.log('✓ Build post-processing complete');




