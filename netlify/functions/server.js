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
    
    const url = new URL(
      event.rawUrl || `https://${event.headers.host || 'localhost'}${event.path || '/'}`,
    );

    const response = await server.fetch(
      new Request(url, {
        method: event.httpMethod || 'GET',
        headers: event.headers,
        body: event.body,
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
