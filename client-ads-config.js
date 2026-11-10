/**
 * Temporary Third-Party Advertising Experiment Configuration
 * Strictly isolated from core Calculatorship scripts (theme.js, calculator.js).
 *
 * SECURITY GUARDRAIL:
 * - Kept DISABLED by default (`ENABLE_CLIENT_ADS = false`) until the service
 *   worker security audit has been reviewed and activation is explicitly approved.
 */
(function (global) {
  "use strict";

  var ENABLE_CLIENT_ADS = false;

  global.CALCULATORSHIP_CLIENT_ADS = Object.freeze({
    ENABLE_CLIENT_ADS: ENABLE_CLIENT_ADS,
    EXPERIMENT_ID: "client-ads-3nbf4-12233805",
    SW_PATH: "/client-ads-sw.js",
    SW_SCOPE: "/",
    DOMAIN: "3nbf4.com",
    ZONE_ID: 12233805
  });
})(window);

