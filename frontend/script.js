/* Smooth navigation + working contact form wired to FastAPI backend */
(function () {
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Mobile nav toggle
  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.getElementById('nav-menu');
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
      const open = navMenu.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', String(open));
    });
  }

  // Contact form
  const form = document.getElementById('contact-form');
  const status = document.getElementById('form-status');
  const BACKEND_URL = (window.CONFIG && window.CONFIG.BACKEND_URL) || 'http://127.0.0.1:8000';

  const setStatus = (msg, ok = true) => {
    if (!status) return;
    status.textContent = msg;
    status.style.color = ok ? '#7cf7d4' : '#ff7a7a';
  };

  const validateForm = (data) => {
    const errors = [];
    if (!data.name?.trim()) errors.push('Name is required');
    if (!data.email?.trim()) errors.push('Email is required');
    if (!data.message?.trim()) errors.push('Message is required');
    if (data.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) {
      errors.push('Please enter a valid email address');
    }
    return errors;
  };

  const handleFormError = (error, response = null) => {
    console.error('Form submission error:', error);
    
    if (error.name === 'TypeError' && error.message.includes('fetch')) {
      setStatus('Unable to connect to server. Please check your internet connection.', false);
    } else if (response?.status === 429) {
      setStatus('Too many requests. Please wait a moment and try again.', false);
    } else if (response?.status >= 500) {
      setStatus('Server error. Please try again later.', false);
    } else if (response?.status >= 400) {
      setStatus('Invalid request. Please check your information.', false);
    } else {
      setStatus('Something went wrong. Please try again.', false);
    }
  };

  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const data = Object.fromEntries(new FormData(form).entries());

      // Enhanced client validation
      const validationErrors = validateForm(data);
      if (validationErrors.length > 0) {
        setStatus(validationErrors.join('. ') + '.', false);
        return;
      }

      setStatus('Sending message...', true);

      try {
        const res = await fetch(`${BACKEND_URL}/contact`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data),
        });

        if (res.ok) {
          setStatus('Thanks! Your message has been sent.');
          form.reset();
        } else {
          let errorMessage = 'Something went wrong. Try again.';
          try {
            const errorData = await res.json();
            errorMessage = errorData.detail || errorData.message || errorMessage;
          } catch {
            // If response isn't JSON, use default message
          }
          setStatus(errorMessage, false);
        }
      } catch (err) {
        handleFormError(err);
      }
    });
  }
})();