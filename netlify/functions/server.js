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
    
    // Get URL from event - handle various Netlify Functions formats
    let urlString = event.url;
    
    if (!urlString) {
      // Fallback: construct from parts
      const protocol = event.headers?.['x-forwarded-proto'] || 'https';
      const host = event.headers?.['x-forwarded-host'] || event.headers?.host || 'localhost';
      const path = event.path || '/';
      const search = event.rawQuery ? `?${event.rawQuery}` : '';
      urlString = `${protocol}://${host}${path}${search}`;
    }
    
    // Ensure it's a valid URL
    const url = new URL(urlString);
    
    const response = await server.fetch(
      new Request(url.toString(), {
        method: event.httpMethod || event.method || 'GET',
        headers: new Headers(event.headers || {}),
        body: ['GET', 'HEAD'].includes(event.httpMethod || event.method || 'GET') ? undefined : event.body,
      }),
    );

    return response;
  } catch (error) {
    console.error('SSR Error:', error);
    console.error('Event:', { 
      path: event.path, 
      method: event.httpMethod || event.method, 
      headers: event.headers ? Object.keys(event.headers) : 'none',
      url: event.url
    });
    return new Response(
      JSON.stringify({ message: 'Internal Server Error', error: error.message }),
      { status: 500, headers: { 'Content-Type': 'application/json' } },
    );
  }
};
