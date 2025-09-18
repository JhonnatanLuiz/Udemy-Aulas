const CACHE_NAME = 'spotify-clone-v3';
const HOST = self.location.hostname || '';
const IS_LOCAL = HOST === 'localhost' || HOST === '127.0.0.1' || HOST === '0.0.0.0' || /^192\.168\./.test(HOST);

// Em ambiente local: não controlar nada e remover qualquer cache/registro
if (IS_LOCAL) {
  self.addEventListener('install', event => { self.skipWaiting(); });
  self.addEventListener('activate', event => {
    event.waitUntil(
      caches.keys().then(keys => Promise.all(keys.map(k => caches.delete(k)))).then(() => self.registration.unregister()).then(() => self.clients.claim())
    );
  });
  self.addEventListener('fetch', event => {
    // Sempre passar direto para a rede no ambiente local
    event.respondWith(fetch(event.request));
  });
}
const OFFLINE_URL = 'offline.html';
const NOT_FOUND_URL = '404.html';
const ASSETS = [
  '/',
  'index.html',
  'css/estilo.css',
  'imagens/capa.png',
  'imagens/ruido.png',
  'imagens/spotify.svg',
  'imagens/favicon.png',
  OFFLINE_URL,
  NOT_FOUND_URL
];

if (!IS_LOCAL) self.addEventListener('install', event => {
  event.waitUntil(
  caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS)).then(()=> self.skipWaiting())
  );
});

if (!IS_LOCAL) self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
  )).then(()=> self.clients.claim())
  );
});
// Recebe mensagem para pular espera
if (!IS_LOCAL) self.addEventListener('message', event => {
  if(event.data && event.data.action === 'skipWaiting') {
    self.skipWaiting();
  }
});

function isNavigationRequest(request){
  return request.mode === 'navigate' || (request.method === 'GET' && request.headers.get('accept')?.includes('text/html'));
}

if (!IS_LOCAL) self.addEventListener('fetch', event => {
  const { request } = event;
  if(request.method !== 'GET') return;

  if(isNavigationRequest(request)) {
    event.respondWith(
      fetch(request)
        .then(resp => {
          if(resp.status === 404) { return caches.match(NOT_FOUND_URL); }
          const copy = resp.clone();
          caches.open(CACHE_NAME).then(c => c.put(request, copy));
          return resp;
        })
        .catch(() => caches.match(request).then(c => c || caches.match(OFFLINE_URL)))
    );
    return;
  }

  event.respondWith(
    caches.match(request).then(cached => {
      if(cached) return cached;
      return fetch(request).then(resp => {
        const copy = resp.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(request, copy));
        return resp;
      }).catch(() => cached);
    })
  );
});
