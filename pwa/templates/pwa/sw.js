importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.2.0/workbox-sw.js');

const {registerRoute, setCatchHandler} = workbox.routing;
const { precacheAndRoute } = workbox.precaching;
const {CacheFirst, StaleWhileRevalidate, NetworkFirst} = workbox.strategies;
const {CacheableResponsePlugin } = workbox.cacheableResponse;
const {ExpirationPlugin  } = workbox.expiration;
const { cacheNames } = workbox.core;


const CACHE_NAME = 'pages';
const FALLBACK_HTML_URL = '/offline';
self.addEventListener('install', async (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.add(FALLBACK_HTML_URL))
  );
});


setCatchHandler(async ({event}) => {
  switch (event.request.destination) {
    case 'document':
      return await caches.match(FALLBACK_HTML_URL);
  }
});

setCatchHandler(async ({ request }) => { 
  return caches.match(FALLBACK_HTML_URL);
})


self.addEventListener("activate", function(event) {
    event.waitUntil(
      caches.keys().then(function(cacheNames) {
        let validCacheSet = new Set(Object.values(workbox.core.cacheNames));
        return Promise.all(
          cacheNames
            .filter(function(cacheName) {
              return !validCacheSet.has(cacheName);
            })
            .map(function(cacheName) {
              console.log("deleting cache", cacheName);
              return caches.delete(cacheName);
            })
        );
      })
    );
});

registerRoute(({ request }) => request.mode == 'navigate', new NetworkFirst({ 
    cacheName: 'pages',
    plugins: [ 
        new CacheableResponsePlugin({ statuses: [200]})
    ]
}));

registerRoute(
    ({ request }) =>
      request.destination === 'style' ||
      request.destination === 'script',

    new StaleWhileRevalidate({
      cacheName: 'assets',
      plugins: [
        new CacheableResponsePlugin({
          statuses: [200],
        }),
      ],
    }),
  );

registerRoute(
({ request }) => 
    request.destination === 'font',

    new CacheFirst({
        cacheName: 'fonts',
        plugins: [
            new CacheableResponsePlugin({
                statuses: [200],
            }),
        ],
    }),
);
  

registerRoute(
    ({ request }) => request.destination === 'image',
    new CacheFirst({
        cacheName: 'images',
        plugins: [
        new CacheableResponsePlugin({
            statuses: [200],
        }),
        new ExpirationPlugin({
            maxEntries: 50,
            maxAgeSeconds: 60 * 60 * 24 * 30
        }),
        ],
    }),
);


precacheAndRoute([ { url: '{{ PWA_START_URL }}', revision: '1' }, { url: '/offline', revision: '2' }])
self.__WB_DISABLE_DEV_LOGS = true
