import { server } from './server.js';

export default async function handler(request) {
  return await server.fetch(request);
}
