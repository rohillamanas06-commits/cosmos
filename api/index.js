import { createRequire } from 'module';
import { fileURLToPath } from 'url';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const serverModule = await import(path.join(__dirname, '../dist/server/server.js'));
const { server } = serverModule;

export default async function handler(request) {
  return await server.fetch(request);
}
