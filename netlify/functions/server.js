let serverModule = null;
let serverModulePromise = null;

async function getServer() {
  if (serverModule) return serverModule;
  
  if (!serverModulePromise) {
    serverModulePromise = (async () => {
      const mod = await import('./server-build.js');
      serverModule = mod.default || mod.server || mod;
      return serverModule;
    })();
  }
  
  return serverModulePromise;
}

export default async (event, context) => {
  try {
    const server = await getServer();
    
    // Construct URL from Netlify Functions v2 event properties
    const protocol = event.headers['x-forwarded-proto'] || 'https';
    const host = event.headers['x-forwarded-host'] || event.headers.host || 'localhost';
    const path = event.path || '/';
    const search = event.rawQuery ? `?${event.rawQuery}` : '';
    
    const url = new URL(`${path}${search}`, `${protocol}://${host}`);
    
    const response = await server.fetch(
      new Request(url.toString(), {
        method: event.httpMethod || event.method || 'GET',
        headers: event.headers || {},
        body: ['GET', 'HEAD'].includes(event.httpMethod || event.method) ? undefined : event.body,
      }),
    );

    return response;
  } catch (error) {
    console.error('SSR Error:', error);
    return new Response(
      JSON.stringify({ message: 'Internal Server Error', error: error.message }),
      { status: 500, headers: { 'Content-Type': 'application/json' } },
    );
  }
};
