(function () {
  "use strict";

  /* ============ Localhost / File:// Protocol Link & Logo Normalizer ============ */
  // When opened via file:// or a basic localhost static server (like python -m http.server
  // or VS Code Live Server that does not rewrite /slug to /slug.html),
  // this ensures clean URLs like /blog, /about, and root assets like /logo-light.svg
  // resolve directly to their target files without "ERR_FILE_NOT_FOUND" 404s.
  (function initLocalPathResolver() {
    const isFile = window.location.protocol === "file:";
    const isDevLocal = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1";

    if (isFile || isDevLocal) {
      function fixElements() {
        // Fix logos or root-relative images
        document.querySelectorAll("img[src^='/']").forEach((img) => {
          const src = img.getAttribute("src");
          if (src && src.startsWith("/") && !src.startsWith("//")) {
            img.src = src.substring(1);
          }
        });
      }

      if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", fixElements);
      } else {
        fixElements();
      }

      // Intercept navigation clicks on local/file environment
      document.addEventListener("click", function (e) {
        const a = e.target.closest("a");
        if (!a || !a.getAttribute("href")) return;
        const href = a.getAttribute("href").trim();

        if (href.startsWith("http://") || href.startsWith("https://") || href.startsWith("#") || href.startsWith("mailto:") || href.startsWith("tel:")) return;

        // Homepage link
        if (href === "/" || href === "") {
          if (isFile || (isDevLocal && window.location.pathname.endsWith(".html"))) {
            e.preventDefault();
            window.location.href = "index.html";
          }
          return;
        }

        const cleanPath = href.startsWith("/") ? href.substring(1) : href;
        const noHash = cleanPath.split("#")[0].split("?")[0];
        const hashPart = cleanPath.includes("#") ? "#" + cleanPath.split("#")[1] : "";
        const searchPart = cleanPath.includes("?") ? "?" + cleanPath.split("?")[1].split("#")[0] : "";

        // If it's a clean internal route (e.g. /blog, /about, /income-tax-act-2025...)
        if (noHash && !noHash.includes(".")) {
          // In file:// mode or localhost mode where clean URLs aren't natively mapped by server:
          if (isFile || (isDevLocal && window.location.pathname.endsWith(".html"))) {
            e.preventDefault();
            window.location.href = noHash + ".html" + searchPart + hashPart;
          }
        }
      });
    }
  })();

  /* ============ Helpers ============ */
  const $ = (sel, ctx) => (ctx || document).querySelector(sel);
  const $$ = (sel, ctx) => Array.from((ctx || document).querySelectorAll(sel));

  /* ============ Reading Progress Bar ============ */
  (function initReadingProgress() {
    const bar = $("#reading-progress");
    if (!bar) return;

    function updateProgress() {
      const h = document.documentElement;
      const scrollTop = h.scrollTop || document.body.scrollTop;
      const scrollHeight = h.scrollHeight - h.clientHeight;
      const pct = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
      bar.style.width = pct + "%";
    }

    window.addEventListener("scroll", updateProgress, { passive: true });
    updateProgress();
  })();

  /* ============ Back to Top Button ============ */
  (function initBackToTop() {
    const btt = $("#back-to-top");
    if (!btt) return;

    function onScroll() {
      btt.classList.toggle("is-visible", window.scrollY > 400);
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    btt.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
    onScroll();
  })();

  /* ============ Disclaimer Banner Dismissal ============ */
  (function initDisclaimerBanner() {
    $$(".disclaimer-banner").forEach((banner) => {
      const bannerId = banner.dataset.bannerId || "default";
      const storageKey = "cs-disc-dismissed-" + bannerId;

      if (localStorage.getItem(storageKey)) {
        banner.classList.add("is-hidden");
        return;
      }

      const dismissBtn = banner.querySelector(".disc-dismiss");
      if (dismissBtn) {
        dismissBtn.addEventListener("click", () => {
          banner.classList.add("is-hidden");
          localStorage.setItem(storageKey, "1");
        });
      }
    });
  })();

  /* ============ Mobile Navigation Toggler (Global Event Delegation) ============ */
  (function initMobileNav() {
    function getBackdrop() {
      let bd = document.querySelector(".nav-backdrop");
      if (!bd) {
        bd = document.createElement("div");
        bd.className = "nav-backdrop";
        document.body.appendChild(bd);
      }
      return bd;
    }

    function ensureDrawerHeader() {
      const navMenu = document.querySelector(".main-nav");
      if (navMenu && !navMenu.querySelector(".drawer-header")) {
        const drawerHeader = document.createElement("div");
        drawerHeader.className = "drawer-header";
        drawerHeader.innerHTML = `
          <span class="drawer-title">Navigation</span>
          <button type="button" class="drawer-close-btn" aria-label="Close menu">&times;</button>
        `;
        navMenu.insertBefore(drawerHeader, navMenu.firstChild);
      }
    }

    function closeNav() {
      const navMenu = document.querySelector(".main-nav");
      const toggleBtn = document.querySelector("#nav-toggle");
      const backdrop = getBackdrop();
      if (navMenu) navMenu.classList.remove("is-open-mobile");
      if (toggleBtn) {
        toggleBtn.classList.remove("is-active");
        toggleBtn.setAttribute("aria-expanded", "false");
      }
      if (backdrop) backdrop.classList.remove("is-visible");
      document.body.style.overflow = "";
    }

    function openNav() {
      ensureDrawerHeader();
      const navMenu = document.querySelector(".main-nav");
      const toggleBtn = document.querySelector("#nav-toggle");
      const backdrop = getBackdrop();
      if (navMenu) navMenu.classList.add("is-open-mobile");
      if (toggleBtn) {
        toggleBtn.classList.add("is-active");
        toggleBtn.setAttribute("aria-expanded", "true");
      }
      if (backdrop) backdrop.classList.add("is-visible");
      document.body.style.overflow = "hidden";
    }

    function toggleNav() {
      const navMenu = document.querySelector(".main-nav");
      if (navMenu && navMenu.classList.contains("is-open-mobile")) {
        closeNav();
      } else {
        openNav();
      }
    }

    // Global Click Delegation - works regardless of DOM timing or framework lifecycle
    document.addEventListener("click", function(e) {
      // 1. Toggle Button Click
      const toggleBtn = e.target.closest("#nav-toggle");
      if (toggleBtn) {
        e.preventDefault();
        e.stopPropagation();
        toggleNav();
        return;
      }

      // 2. Drawer Top Close Button Click
      const closeBtn = e.target.closest(".drawer-close-btn");
      if (closeBtn) {
        e.preventDefault();
        e.stopPropagation();
        closeNav();
        return;
      }

      // 3. Backdrop Overlay Click
      const backdrop = e.target.closest(".nav-backdrop");
      if (backdrop) {
        e.preventDefault();
        e.stopPropagation();
        closeNav();
        return;
      }

      // 4. Nav link clicks
      const navLink = e.target.closest(".main-nav a");
      if (navLink) {
        if (navLink.classList.contains("nav-dropdown-toggle")) {
          if (window.innerWidth <= 900) {
            e.preventDefault();
            e.stopPropagation();
            const parentDropdown = navLink.closest(".nav-dropdown");
            if (parentDropdown) {
              parentDropdown.classList.toggle("is-collapsed");
            }
            return;
          }
        }
        closeNav();
        return;
      }

      // 5. Outside Click
      const navMenu = document.querySelector(".main-nav");
      if (navMenu && navMenu.classList.contains("is-open-mobile")) {
        if (!navMenu.contains(e.target)) {
          closeNav();
        }
      }
    });

    // Close on Escape key
    document.addEventListener("keydown", function(e) {
      if (e.key === "Escape") {
        const navMenu = document.querySelector(".main-nav");
        if (navMenu && navMenu.classList.contains("is-open-mobile")) {
          closeNav();
        }
      }
    });

    // Ensure on DOM ready
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", ensureDrawerHeader);
    } else {
      ensureDrawerHeader();
    }
  })();

  /* ============ Active Navigation Indicator ============ */
  (function initActiveMenu() {
    const currentPath = window.location.pathname;
    const pageName = currentPath.substring(currentPath.lastIndexOf("/") + 1);
    
    $$(".main-nav a").forEach((a) => {
      const href = a.getAttribute("href");
      if (href === pageName || (href === "/" && (pageName === "" || pageName === "index.html"))) {
        a.classList.add("active");
      } else {
        a.classList.remove("active");
      }
    });
  })();

  /* ============ Scroll Reveal Animation ============ */
  (function initScrollReveal() {
    const revealTargets = $$(".reveal, .advantage-card, .testimonial-card, .related-card, .step");
    if (revealTargets.length === 0) return;

    revealTargets.forEach((el) => {
      if (!el.classList.contains("reveal")) {
        el.classList.add("reveal");
      }
    });

    if (!("IntersectionObserver" in window)) {
      revealTargets.forEach((el) => el.classList.add("is-visible"));
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: "0px 0px -40px 0px" }
    );

    revealTargets.forEach((el) => observer.observe(el));
  })();

  /* ============ FAQ Accordion Auto-Collapse ============ */
  (function initFAQ() {
    const faqDetails = $$(".faq-item");
    faqDetails.forEach((detail) => {
      detail.addEventListener("click", (e) => {
        if (!detail.hasAttribute("open")) {
          faqDetails.forEach((otherDetail) => {
            if (otherDetail !== detail && otherDetail.hasAttribute("open")) {
              otherDetail.removeAttribute("open");
            }
          });
        }
      });
    });
  })();

  /* ============ Social Share Buttons — Copy Link ============ */
  (function initShareButtons() {
    $$(".share-btn.cp").forEach((btn) => {
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        const url = btn.dataset.url || window.location.href;
        if (navigator.clipboard) {
          navigator.clipboard.writeText(url).then(() => {
            const orig = btn.innerHTML;
            btn.textContent = "Copied!";
            setTimeout(() => { btn.innerHTML = orig; }, 2000);
          });
        } else {
          const el = document.createElement("input");
          el.value = url;
          document.body.appendChild(el);
          el.select();
          document.execCommand("copy");
          document.body.removeChild(el);
        }
      });
    });
  })();

  /* ============ Contact Form Handling ============ */
  (function initContactForm() {
    const contactForm = $("#contact-form");
    if (!contactForm) return;

    contactForm.addEventListener("submit", (e) => {
      e.preventDefault();
      
      let hasError = false;
      const fields = ["name", "email", "subject", "message"];

      fields.forEach((fieldId) => {
        const input = $(`#${fieldId}`);
        const feedback = $(`#${fieldId}-error`);
        if (!input || !feedback) return;

        if (!input.value.trim()) {
          input.classList.add("has-error");
          feedback.style.display = "block";
          hasError = true;
        } else if (fieldId === "email" && !validateEmail(input.value)) {
          input.classList.add("has-error");
          feedback.textContent = "Please enter a valid email address.";
          feedback.style.display = "block";
          hasError = true;
        } else {
          input.classList.remove("has-error");
          feedback.style.display = "none";
        }
      });

      if (!hasError) {
        const modal = $("#success-modal");
        if (modal) {
          modal.classList.add("is-active");
          contactForm.reset();
        }
      }
    });

    const closeModalBtn = $("#close-modal");
    if (closeModalBtn) {
      closeModalBtn.addEventListener("click", () => {
        const modal = $("#success-modal");
        if (modal) modal.classList.remove("is-active");
      });
    }

    function validateEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(String(email).toLowerCase());
    }

    $$(".form-input, .form-textarea").forEach((el) => {
      el.addEventListener("input", () => {
        el.classList.remove("has-error");
        const feedback = $(`#${el.id}-error`);
        if (feedback) feedback.style.display = "none";
      });
    });
  })();

  /* ============ Cookie Consent Banner & Preferences Modal ============ */
  (function initCookieConsent() {
    function setupCookieConsent() {
      let consent = localStorage.getItem('cookieConsent');
      
      // Auto-render banner if not present in static DOM
      let banner = document.getElementById('cs-cookie-banner');
      if (!banner && !consent) {
        banner = document.createElement('div');
        banner.id = 'cs-cookie-banner';
        banner.setAttribute('role', 'region');
        banner.setAttribute('aria-label', 'Cookie Consent');
        banner.style.cssText = 'position:fixed; bottom:0; left:0; right:0; background:#0f172a; color:#f8fafc; padding:16px 24px; z-index:99999; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px; box-shadow:0 -4px 20px rgba(0,0,0,0.15); font-size:0.9rem; font-family:Inter,sans-serif;';
        banner.innerHTML = `
          <div style="flex:1; min-width:280px; line-height:1.5;">
            Calculatorship uses strictly client-side calculators. Optional analytics and ad measurement scripts use cookies only if you consent. Read our <a href="/cookies" style="color:#38bdf8; text-decoration:underline;">Cookie Policy</a> and <a href="/privacy" style="color:#38bdf8; text-decoration:underline;">Privacy Policy</a>.
          </div>
          <div style="display:flex; gap:10px; align-items:center;">
            <button id="cs-decline-cookies" style="background:transparent; border:1px solid #475569; color:#f8fafc; padding:8px 16px; border-radius:6px; cursor:pointer; font-weight:600; font-size:0.88rem;">Decline</button>
            <button id="cs-accept-cookies" style="background:#059669; border:none; color:#ffffff; padding:8px 18px; border-radius:6px; cursor:pointer; font-weight:700; font-size:0.88rem;">Accept</button>
          </div>
        `;
        document.body.appendChild(banner);
      }

      const btnAccept = document.getElementById('cs-accept-cookies');
      const btnDecline = document.getElementById('cs-decline-cookies');

      if (btnAccept) {
        btnAccept.onclick = function() {
          localStorage.setItem('cookieConsent', 'accepted');
          localStorage.setItem('cookiePreferences', JSON.stringify({ analytics: true, advertising: true }));
          if (banner) banner.style.display = 'none';
          if (typeof window.gtag === 'function') {
            window.gtag('config', 'G-0C93Q0VBQP');
          }
        };
      }

      if (btnDecline) {
        btnDecline.onclick = function() {
          localStorage.setItem('cookieConsent', 'declined');
          localStorage.setItem('cookiePreferences', JSON.stringify({ analytics: false, advertising: false }));
          if (banner) banner.style.display = 'none';
        };
      }
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', setupCookieConsent);
    } else {
      setupCookieConsent();
    }

    window.resetCookieConsent = function() {
      localStorage.removeItem('cookieConsent');
      localStorage.removeItem('cookiePreferences');
      const banner = document.getElementById('cs-cookie-banner');
      if (banner) banner.remove();
      setupCookieConsent();
    };
  })();

})();
