(function () {
  "use strict";

  /* ============ Helpers ============ */
  const $ = (sel, ctx) => (ctx || document).querySelector(sel);
  const $$ = (sel, ctx) => Array.from((ctx || document).querySelectorAll(sel));

  /* ============ Logo Swap Utility ============ */
  function updateLogos(theme) {
    const logoSrc = theme === "light"
      ? "logo-light.svg"
      : "logo-dark.svg";
    // Handle both root-relative and same-dir img paths
    $$("img[src*='logo']").forEach((img) => {
      // Preserve the filename part, only swap which variant
      if (img.src.includes("logo-dark") || img.src.includes("logo-light") || img.src.includes("logo.svg")) {
        img.src = logoSrc;
      }
    });
  }

  /* ============ Theme Setup & Toggle ============ */
  (function initTheme() {
    const toggle = $("#theme-toggle");
    if (!toggle) return;
    const root = document.documentElement;
    
    // Load theme from memory or default to dark
    let storedTheme = localStorage.getItem("calculatorship-theme") || "dark";
    root.setAttribute("data-theme", storedTheme);
    toggle.setAttribute("aria-pressed", storedTheme === "light" ? "true" : "false");
    toggle.setAttribute("aria-label", storedTheme === "light" ? "Switch to dark theme" : "Switch to light theme");
    // Set correct logo on first load
    updateLogos(storedTheme);

    toggle.addEventListener("click", () => {
      let currentTheme = root.getAttribute("data-theme") || "dark";
      let nextTheme = currentTheme === "dark" ? "light" : "dark";
      
      root.setAttribute("data-theme", nextTheme);
      localStorage.setItem("calculatorship-theme", nextTheme);
      toggle.setAttribute("aria-pressed", nextTheme === "light" ? "true" : "false");
      toggle.setAttribute("aria-label", nextTheme === "light" ? "Switch to dark theme" : "Switch to light theme");
      // Swap logo text colour
      updateLogos(nextTheme);
      // Dispatch custom event for chart redrawing on theme change
      window.dispatchEvent(new CustomEvent("themechange", { detail: { theme: nextTheme } }));
    });
  })();

  /* ============ Mobile Navigation Toggler ============ */
  (function initMobileNav() {
    const toggleBtn = $("#nav-toggle");
    const navMenu = $(".main-nav");
    if (!toggleBtn || !navMenu) return;

    toggleBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      const isOpen = navMenu.classList.toggle("is-open-mobile");
      toggleBtn.classList.toggle("is-active", isOpen);
      toggleBtn.setAttribute("aria-expanded", isOpen ? "true" : "false");

      if (isOpen) {
        navMenu.style.cssText = `
          display: flex;
          flex-direction: column;
          position: absolute;
          top: 72px;
          left: 0;
          right: 0;
          background: var(--bg-elevated);
          padding: 24px 24px 30px;
          border-bottom: 1px solid var(--border-soft);
          gap: 20px;
          animation: slideDownMobile 0.3s var(--ease) both;
          box-shadow: var(--shadow-soft);
        `;
        // Inject slide keyframe dynamically if not loaded
        if (!document.getElementById("mobile-menu-style")) {
          const style = document.createElement("style");
          style.id = "mobile-menu-style";
          style.innerHTML = `
            @keyframes slideDownMobile {
              from { opacity: 0; transform: translateY(-10px); }
              to { opacity: 1; transform: translateY(0); }
            }
          `;
          document.head.appendChild(style);
        }
      } else {
        navMenu.removeAttribute("style");
      }
    });

    // Close menu when clicking outside
    document.addEventListener("click", (e) => {
      if (navMenu.classList.contains("is-open-mobile") && !navMenu.contains(e.target) && e.target !== toggleBtn) {
        navMenu.classList.remove("is-open-mobile");
        toggleBtn.classList.remove("is-active");
        toggleBtn.setAttribute("aria-expanded", "false");
        navMenu.removeAttribute("style");
      }
    });

    // Close menu when clicking items
    $$("a", navMenu).forEach((link) => {
      link.addEventListener("click", () => {
        navMenu.classList.remove("is-open-mobile");
        toggleBtn.classList.remove("is-active");
        toggleBtn.setAttribute("aria-expanded", "false");
        navMenu.removeAttribute("style");
      });
    });
  })();

  /* ============ Active Navigation Indicator ============ */
  (function initActiveMenu() {
    const currentPath = window.location.pathname;
    const pageName = currentPath.substring(currentPath.lastIndexOf("/") + 1);
    
    $$(".main-nav a").forEach((a) => {
      const href = a.getAttribute("href");
      // Check exact match or home link
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
      {
        threshold: 0.1,
        rootMargin: "0px 0px -40px 0px",
      }
    );

    revealTargets.forEach((el) => observer.observe(el));
  })();

  /* ============ FAQ Accordion Auto-Collapse ============ */
  (function initFAQ() {
    const faqDetails = $$(".faq-item");
    faqDetails.forEach((detail) => {
      detail.addEventListener("click", (e) => {
        if (!detail.hasAttribute("open")) {
          // Collapse all others
          faqDetails.forEach((otherDetail) => {
            if (otherDetail !== detail && otherDetail.hasAttribute("open")) {
              otherDetail.removeAttribute("open");
            }
          });
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
        // Show success modal
        const modal = $("#success-modal");
        if (modal) {
          modal.classList.add("is-active");
          contactForm.reset();
        }
      }
    });

    // Close Modal Event Listener
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

    // Input listening to clear errors
    $$(".form-input, .form-textarea").forEach((el) => {
      el.addEventListener("input", () => {
        el.classList.remove("has-error");
        const feedback = $(`#${el.id}-error`);
        if (feedback) feedback.style.display = "none";
      });
    });
  })();

  /* ============ Newsletter Form Submission ============ */
  (function initNewsletter() {
    const form = $("#newsletter-form");
    if (!form) return;

    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const input = $("#newsletter-email");
      if (!input || !input.value) return;

      const toast = $("#copy-toast");
      if (toast) {
        toast.textContent = "Thank you! You have successfully subscribed.";
        toast.classList.add("is-visible");
        input.value = "";
        
        setTimeout(() => {
          toast.classList.remove("is-visible");
        }, 3000);
      } else {
        alert("Thank you! You have successfully subscribed.");
        input.value = "";
      }
    });
  })();

})();
