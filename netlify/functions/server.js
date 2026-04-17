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

exports.handler = async (event, context) => {
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

    const bodyBuffer = Buffer.from(await response.arrayBuffer());

    return {
      statusCode: response.status,
      headers: Object.fromEntries(response.headers),
      body: bodyBuffer.toString('base64'),
      isBase64Encoded: true,
    };
  } catch (error) {
    console.error('SSR Error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ message: 'Internal Server Error', error: error.message }),
    };
  }
};
