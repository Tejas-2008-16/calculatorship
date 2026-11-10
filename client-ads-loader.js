/**
 * Isolated Controller for Temporary Third-Party Advertising Experiment
 * Kept strictly separate from theme.js and calculator.js.
 *
 * - Disabled state (`ENABLE_CLIENT_ADS !== true`):
 *   Does NOT register any service worker, does NOT contact external ad domains,
 *   and cleanly unregisters /client-ads-sw.js (plus experiment-specific caches/IDBs)
 *   only if an experiment registration already exists on the origin.
 * - Enabled state (`ENABLE_CLIENT_ADS === true`):
 *   After window load, verifies secure context & checks that no unrelated service
 *   worker occupies scope '/', then registers /client-ads-sw.js without adding any
 *   popups, redirects, or Notification.requestPermission() prompts.
 */
(function () {
  "use strict";

  var cfg = window.CALCULATORSHIP_CLIENT_ADS;
  if (!cfg) return;

  var EXPERIMENT_IDB_NAMES = [
    "swDatabase",
    "swMetrics",
    "bannerDb",
    "subscriptionDb",
    "statsFEDb",
    "swaab"
  ];

  function matchesExperimentSwUrl(scriptUrl) {
    if (!scriptUrl) return false;
    try {
      if (window.location.origin && window.location.origin !== "null") {
        var parsed = new URL(scriptUrl, window.location.origin);
        return parsed.pathname === cfg.SW_PATH;
      }
    } catch (err) {}
    return String(scriptUrl).indexOf(cfg.SW_PATH) !== -1;
  }

  function registrationMatchesExperiment(reg) {
    if (!reg) return false;
    var workers = [reg.active, reg.waiting, reg.installing];
    for (var i = 0; i < workers.length; i++) {
      if (workers[i] && matchesExperimentSwUrl(workers[i].scriptURL)) {
        return true;
      }
    }
    return false;
  }

  function clearExperimentStorageOnly() {
    try {
      if ("caches" in window && window.caches && typeof window.caches.keys === "function") {
        window.caches.keys().then(function (keys) {
          keys.forEach(function (key) {
            var isExpCache =
              key.indexOf("client-ads-") === 0 ||
              key.indexOf("3nbf4") !== -1 ||
              key === "runCmdCache";
            if (isExpCache) {
              window.caches.delete(key).catch(function () {});
            }
          });
        }).catch(function () {});
      }
    } catch (err) {}

    try {
      if ("indexedDB" in window && window.indexedDB && typeof window.indexedDB.deleteDatabase === "function") {
        EXPERIMENT_IDB_NAMES.forEach(function (dbName) {
          try {
            window.indexedDB.deleteDatabase(dbName);
          } catch (err) {}
        });
      }
    } catch (err) {}
  }

  function disableAndCleanupIfRegistered() {
    if (!("serviceWorker" in navigator) || !window.isSecureContext) return;
    try {
      navigator.serviceWorker.getRegistrations().then(function (regs) {
        var foundExperimentSw = false;
        regs.forEach(function (reg) {
          if (registrationMatchesExperiment(reg)) {
            foundExperimentSw = true;
            reg.unregister().catch(function () {});
          }
        });
        if (foundExperimentSw) {
          clearExperimentStorageOnly();
        }
      }).catch(function () {});
    } catch (err) {}
  }

  function registerExperimentServiceWorker() {
    if (!("serviceWorker" in navigator) || !window.isSecureContext) return;
    try {
      navigator.serviceWorker.getRegistrations().then(function (regs) {
        var hasUnrelatedSameScopeSw = regs.some(function (reg) {
          if (registrationMatchesExperiment(reg)) return false;
          try {
            var scopePath = new URL(reg.scope).pathname;
            return scopePath === cfg.SW_SCOPE;
          } catch (err) {
            return true;
          }
        });
        if (hasUnrelatedSameScopeSw) return;

        navigator.serviceWorker.register(cfg.SW_PATH, {
          scope: cfg.SW_SCOPE,
          updateViaCache: "none"
        }).catch(function () {});
      }).catch(function () {});
    } catch (err) {}
  }

  if (cfg.ENABLE_CLIENT_ADS !== true) {
    disableAndCleanupIfRegistered();
    return;
  }

  if (document.readyState === "complete") {
    registerExperimentServiceWorker();
  } else {
    window.addEventListener("load", registerExperimentServiceWorker, { once: true });
  }
})();

