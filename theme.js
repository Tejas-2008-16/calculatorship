(function () {
  "use strict";

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

  /* ============ Mobile Navigation Toggler ============ */
  (function initMobileNav() {
    const toggleBtn = $("#nav-toggle");
    const navMenu = $(".main-nav");
    if (!toggleBtn || !navMenu) return;

    let backdrop = $(".nav-backdrop");
    if (!backdrop) {
      backdrop = document.createElement("div");
      backdrop.className = "nav-backdrop";
      document.body.appendChild(backdrop);
    }

    function closeNav() {
      navMenu.classList.remove("is-open-mobile");
      toggleBtn.classList.remove("is-active");
      toggleBtn.setAttribute("aria-expanded", "false");
      backdrop.classList.remove("is-visible");
      document.body.style.overflow = "";
    }

    function openNav() {
      navMenu.classList.add("is-open-mobile");
      toggleBtn.classList.add("is-active");
      toggleBtn.setAttribute("aria-expanded", "true");
      backdrop.classList.add("is-visible");
      document.body.style.overflow = "hidden";
    }

    toggleBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      if (navMenu.classList.contains("is-open-mobile")) {
        closeNav();
      } else {
        openNav();
      }
    });

    backdrop.addEventListener("click", closeNav);

    document.addEventListener("click", (e) => {
      if (navMenu.classList.contains("is-open-mobile") && !navMenu.contains(e.target) && e.target !== toggleBtn) {
        closeNav();
      }
    });

    $$("a", navMenu).forEach((link) => {
      link.addEventListener("click", (e) => {
        if (link.classList.contains("nav-dropdown-toggle")) {
          // On mobile, keep dropdown expanded
          return;
        }
        closeNav();
      });
    });
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
      const consent = localStorage.getItem('cookieConsent');
      const banner = document.getElementById('cs-cookie-banner');
      const modal = document.getElementById('cs-cookie-modal-overlay');
      const btnAccept = document.getElementById('cs-accept-cookies');
      const btnManage = document.getElementById('cs-manage-cookies');
      const btnSave = document.getElementById('cs-save-preferences');

      if (banner && !consent) {
        banner.style.display = 'block';
      }

      if (btnAccept) {
        btnAccept.onclick = function() {
          localStorage.setItem('cookieConsent', 'accepted');
          localStorage.setItem('cookiePreferences', JSON.stringify({ analytics: true, advertising: true }));
          if (banner) banner.style.display = 'none';
          if (modal) modal.style.display = 'none';
        };
      }

      function openModal() {
        if (modal) modal.style.display = 'flex';
        else if (banner) banner.style.display = 'block';
      }

      if (btnManage) btnManage.onclick = openModal;

      document.querySelectorAll('.js-cookie-settings, a[href="#cookie-settings"], a[href="#cookie-preferences"], #cs-open-cookie-modal').forEach((el) => {
        el.onclick = function(e) {
          e.preventDefault();
          openModal();
        };
      });

      if (btnSave) {
        btnSave.onclick = function() {
          const analyticsInput = document.getElementById('cs-toggle-analytics');
          const advertisingInput = document.getElementById('cs-toggle-advertising');
          const analytics = analyticsInput ? analyticsInput.checked : true;
          const advertising = advertisingInput ? advertisingInput.checked : true;
          localStorage.setItem('cookieConsent', 'custom');
          localStorage.setItem('cookiePreferences', JSON.stringify({ analytics, advertising }));
          if (modal) modal.style.display = 'none';
          if (banner) banner.style.display = 'none';
        };
      }

      if (modal) {
        modal.onclick = function(e) {
          if (e.target === modal) modal.style.display = 'none';
        };
      }
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', setupCookieConsent);
    } else {
      setupCookieConsent();
    }

    window.openCookiePreferences = function() {
      const modal = document.getElementById('cs-cookie-modal-overlay');
      if (modal) modal.style.display = 'flex';
      else {
        const banner = document.getElementById('cs-cookie-banner');
        if (banner) banner.style.display = 'block';
      }
    };

    window.resetCookieConsent = function() {
      localStorage.removeItem('cookieConsent');
      localStorage.removeItem('cookiePreferences');
      const banner = document.getElementById('cs-cookie-banner');
      if (banner) banner.style.display = 'block';
    };
  })();

})();
