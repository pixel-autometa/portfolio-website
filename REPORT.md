# Brief Report


**Student:** Sajid  
**Date:** 2025-01-27

## AI Tool Chosen
I used **Cursor (v1.5.11)** as my primary AI coding assistant, supported by ChatGPT for explanations and quick fixes.

## Why Cursor?
- Deep editor integration (inline suggestions, quick refactors)
- Strong context awareness across multiple files
- Fast iteration speed for HTML/CSS/JS + Python

## How AI Helped
- **Scaffolding:** Generated initial HTML structure, FastAPI endpoints, and deployment configs.
- **Content Creation:** Rewrote hero copy to highlight FastAPI and JavaScript expertise, created professional project descriptions.
- **Accessibility:** Enhanced button contrast, padding, and focus states for WCAG compliance.
- **Error Handling:** Refactored contact form with comprehensive validation and user-friendly error messages.
- **Social Integration:** Added professional social media links with enhanced styling and hover effects.
- **Refactoring:** Improved CSS responsiveness and accessibility throughout the site.
- **Debugging:** Helped resolve CORS issues between Netlify (frontend) and Render (backend).
- **Docs:** Drafted README and this report outline quickly.

## Challenges & Solutions
- **CORS between Netlify and backend:** Fixed by setting `FRONTEND_ORIGIN` env var in FastAPI CORS middleware.
- **Deployment split (static vs API):** Deployed frontend on Netlify and backend on Render, then connected via `config.js`.
- **Form validation:** Added comprehensive client-side validation with email format checking and server-side validation.
- **Accessibility compliance:** Enhanced button contrast ratios and touch targets to meet WCAG guidelines.
- **Error handling:** Implemented robust error handling for network issues, server errors, and user input validation.
- **Content personalization:** Created engaging hero copy and professional project descriptions that highlight technical expertise.

## Outcome
- **Live Website:** Deployed to Netlify (frontend) & Render (backend) with professional branding for Sajid.  
- **GitHub Repo:** Clean structure with README and AI usage documented.  
- **Working Contact Form:** Enhanced form with comprehensive error handling and validation.
- **Professional Portfolio:** Showcases FastAPI and JavaScript expertise with three featured projects.
- **Accessibility Compliant:** WCAG-compliant design with improved contrast and focus states.
- **Social Integration:** Professional social media links with engaging hover effects.
- **Mobile Responsive:** Optimized for all device sizes with smooth animations and transitions.
