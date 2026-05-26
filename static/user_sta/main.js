/* ═══════════════════════════════════════════
   ELDERCARE — Enhanced main.js
   ═══════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

  /* ─── NAVBAR SCROLL ─── */
  const nav = document.getElementById('mainNav');
  if (nav) {
    const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 30);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ─── SCROLL ANIMATIONS ─── */
  const animateEls = document.querySelectorAll('[data-animate]');
  if (animateEls.length && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const delay = entry.target.dataset.delay || 0;
          setTimeout(() => entry.target.classList.add('animated'), +delay);
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    animateEls.forEach(el => io.observe(el));
  }

  /* ─── COUNTER ANIMATION ─── */
  const counters = document.querySelectorAll('[data-count]');
  if (counters.length && 'IntersectionObserver' in window) {
    const cio = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = +el.getAttribute('data-count');
          const dur = 1800;
          const step = target / (dur / 16);
          let cur = 0;
          const tick = () => {
            cur = Math.min(cur + step, target);
            el.textContent = Math.floor(cur).toLocaleString('en-IN');
            if (cur < target) requestAnimationFrame(tick);
          };
          tick();
          cio.unobserve(el);
        }
      });
    }, { threshold: 0.5 });
    counters.forEach(el => cio.observe(el));
  }

  /* ─── SOS MODAL ─── */
  const sosModal = document.getElementById('sosModal');
  const sosBtn = document.getElementById('sosBtn');
  const cancelSos = document.getElementById('cancelSos');
  const confirmSos = document.getElementById('confirmSos');

  if (sosBtn && sosModal) {
    sosBtn.addEventListener('click', () => sosModal.classList.add('active'));
  }
  if (cancelSos) cancelSos.addEventListener('click', () => sosModal.classList.remove('active'));
  if (confirmSos) {
    confirmSos.addEventListener('click', () => {
      sosModal.classList.remove('active');
      showToast('🚨 SOS Alert sent! Admin has been notified.', 'danger');
    });
  }
  if (sosModal) {
    sosModal.addEventListener('click', (e) => {
      if (e.target === sosModal) sosModal.classList.remove('active');
    });
  }

  /* ─── SIDEBAR TOGGLE ─── */
  const sidebarToggle = document.getElementById('sidebarToggle');
  const sidebar = document.getElementById('sidebar');
  const mainContent = document.getElementById('mainContent');
  if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      sidebar.classList.toggle('collapsed');
      if (mainContent) mainContent.classList.toggle('expanded');
    });
  }

  /* ─── PASSWORD TOGGLE ─── */
  const passToggle = document.getElementById('passToggle');
  const passInput = document.getElementById('passInput');
  const passEye = document.getElementById('passEye');
  if (passToggle && passInput) {
    passToggle.addEventListener('click', () => {
      const isPass = passInput.type === 'password';
      passInput.type = isPass ? 'text' : 'password';
      if (passEye) passEye.className = isPass ? 'fas fa-eye-slash' : 'fas fa-eye';
    });
  }

  /* ─── REGISTER STEPS ─── */
  window.nextRegStep = (step) => {
    document.querySelectorAll('.reg-step-content').forEach(c => c.classList.remove('active'));
    document.querySelectorAll('.reg-step').forEach((s, i) => {
      s.classList.remove('active');
      if (i + 1 < step) s.classList.add('done');
    });
    const content = document.getElementById('regStep' + step);
    if (content) content.classList.add('active');
    const stepEl = document.querySelector(`.reg-step[data-step="${step}"]`);
    if (stepEl) stepEl.classList.add('active');
  };

  /* ─── DATE ─── */
  const dateEl = document.getElementById('currentDate');
  if (dateEl) {
    const now = new Date();
    dateEl.textContent = now.toLocaleDateString('en-IN', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
  }

  /* ─── ROLE TOGGLE ─── */
  document.querySelectorAll('.role-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.role-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });

  /* ─── FILTER BUTTONS ─── */
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const parent = btn.closest('.dc-filters') || btn.parentElement;
      parent.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });

  /* ─── TOAST NOTIFICATION ─── */
  window.showToast = (msg, type = 'success') => {
    const existing = document.getElementById('toast-container');
    if (existing) existing.remove();
    const container = document.createElement('div');
    container.id = 'toast-container';
    container.style.cssText = 'position:fixed;bottom:1.5rem;right:1.5rem;z-index:9999;max-width:360px;';
    const colors = { success: 'var(--green)', danger: 'var(--red)', info: 'var(--blue)', warn: 'var(--yellow)' };
    const toast = document.createElement('div');
    toast.style.cssText = `background:#fff;border:1px solid var(--warm-border);border-left:4px solid ${colors[type]||colors.success};border-radius:12px;padding:1rem 1.25rem;box-shadow:0 8px 40px rgba(0,0,0,0.12);font-family:'DM Sans',sans-serif;font-size:0.875rem;color:var(--text-primary);animation:fadeInUp 0.4s ease;`;
    toast.textContent = msg;
    container.appendChild(toast);
    document.body.appendChild(container);
    setTimeout(() => container.remove(), 4000);
  };

  /* ─── PROFILE TABS ─── */
  window.switchTab = (tab) => {
    document.querySelectorAll('.ptab').forEach((t, i) => {
      t.classList.remove('active');
      const tabs = ['info', 'edit', 'security'];
      if (tabs[i] === tab) t.classList.add('active');
    });
    document.querySelectorAll('.ptab-content').forEach(c => c.classList.remove('active'));
    const target = document.getElementById('tab-' + tab);
    if (target) target.classList.add('active');
  };

  /* ─── BOOKING FORM STEPS ─── */
  let currentStep = 1, selectedTime = '';
  window.goStep = (n) => {
    for (let i = 1; i <= 3; i++) {
      const el = document.getElementById('formStep' + i);
      if (el) el.style.display = i === n ? 'block' : 'none';
    }
    currentStep = n;
    if (n === 3) {
      const d = document.getElementById('apptDate');
      const cd = document.getElementById('confirmDate');
      const ct = document.getElementById('confirmTime');
      if (cd) cd.textContent = d ? d.value : '—';
      if (ct) ct.textContent = selectedTime || '—';
    }
  };
  window.selectSlot = (el) => {
    if (el.classList.contains('unavailable')) return;
    document.querySelectorAll('.time-slot').forEach(s => s.classList.remove('selected'));
    el.classList.add('selected');
    selectedTime = el.textContent.trim();
  };
  window.submitBooking = () => {
    const m = document.getElementById('successModal');
    if (m) m.style.display = 'flex';
  };

  /* ─── CARETAKER COST CALC ─── */
  window.calcCost = () => {
    const s = document.getElementById('startDate'), e = document.getElementById('endDate');
    if (s && e && s.value && e.value) {
      const days = Math.max(0, Math.round((new Date(e.value) - new Date(s.value)) / 86400000));
      const dt = document.getElementById('durationText');
      const tt = document.getElementById('totalText');
      if (dt) dt.textContent = days + ' day' + (days !== 1 ? 's' : '');
      if (tt) tt.textContent = '₹' + (days * 400).toLocaleString('en-IN');
    }
  };

  /* ─── CARETAKER SERVICE OPTIONS ─── */
  window.toggleService = (el) => el.classList.toggle('selected');

  /* ─── FAQ TOGGLE ─── */
  window.toggleFaq = (el) => {
    const item = el.closest('.faq-item');
    const isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
    if (!isOpen) item.classList.add('open');
  };

  /* ─── HISTORY FILTER ─── */
  window.filterHistory = (btn, filter) => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.hist-row').forEach(row => {
      if (filter === 'all') { row.style.display = 'flex'; return; }
      const type = row.dataset.type, status = row.dataset.status;
      row.style.display = (type === filter || status === filter) ? 'flex' : 'none';
    });
  };

  /* ─── DATE CONSTRAINTS ─── */
  const apptDate = document.getElementById('apptDate');
  if (apptDate) apptDate.min = new Date().toISOString().split('T')[0];
  const today = new Date().toISOString().split('T')[0];
  ['startDate', 'endDate'].forEach(id => {
    const el = document.getElementById(id);
    if (el) {
      el.min = today;
      el.addEventListener('change', window.calcCost);
    }
  });

  /* ─── ELDER MODAL ─── */
  window.openModal = (id) => {
    const m = document.getElementById(id);
    if (m) m.classList.add('active');
  };
  window.closeModal = (id) => {
    const m = document.getElementById(id);
    if (m) m.classList.remove('active');
  };

  /* ─── MOBILE OVERLAY CLOSE ─── */
  document.addEventListener('click', (e) => {
    if (sidebar && sidebar.classList.contains('open') && !sidebar.contains(e.target) && e.target !== sidebarToggle) {
      sidebar.classList.remove('open');
    }
  });

});
