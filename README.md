# Sajid's Portfolio Website (FastAPI + HTML/CSS/JS)

A clean, responsive portfolio showcasing **Sajid's** expertise as CEO, FastAPI Architect, and JavaScript Full-Stack Developer. Features a **FastAPI** backend for the contact form and a **static frontend** deployable to **Netlify**.

## Tech Stack
- Frontend: HTML5, CSS3, JavaScript (Enhanced with accessibility features)
- Backend: FastAPI (Python)
- Hosting: Netlify (frontend), Render (backend)
- AI Tool: Cursor (and ChatGPT)
- Features: Responsive design, contact form, social media integration, project showcase

## Quick Start (Local)

### 1) Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Backend runs at http://127.0.0.1:8000

### 2) Frontend
```bash
cd ../frontend
# Copy config and point to your local backend
cp config.example.js config.js
# Ensure BACKEND_URL inside config.js is http://127.0.0.1:8000
# Open index.html with Live Server or use any static server
python -m http.server 5500
```
Open http://127.0.0.1:5500 and test the contact form.

## Deploy

### A) Frontend → Netlify
1. Push this repo to GitHub.
2. In Netlify, **New site from Git** → select repo.
3. Build command: _none_ ; Publish directory: `frontend`
4. After deploy, note your site URL e.g. `https://YOUR-SITE.netlify.app`.

### B) Backend → Render (FastAPI)
Two options:

- **With render.yaml (recommended):**
  1. In Render: **New +** → **Blueprint** → point to your repo.
  2. It will detect `render.yaml` and create your **portfolio-fastapi** web service using `backend/`.
  3. Set env var **FRONTEND_ORIGIN** to your Netlify URL.
  4. Deploy; copy the service URL, e.g. `https://portfolio-fastapi.onrender.com`.

- **Manual (if not using render.yaml):**
  1. New → **Web Service** → pick repo, set **Root Directory** = `backend`.
  2. Build command: `pip install -r requirements.txt`
  3. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
  4. Add env var `FRONTEND_ORIGIN` with your Netlify site URL.

### C) Connect Frontend to Backend
- In `frontend/config.js` set:
```js
window.CONFIG = { BACKEND_URL: "https://YOUR-RENDER-BACKEND.onrender.com" }
```
- Redeploy Netlify (push to GitHub or use Netlify UI).

## Structure
```
portfolio-website/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .gitignore
├── frontend/
│   ├── assets/
│   │   ├── profile-placeholder.svg
│   │   ├── placeholder-1.svg
│   │   ├── placeholder-2.svg
│   │   └── placeholder-3.svg
│   ├── config.example.js
│   ├── index.html
│   ├── script.js
│   └── styles.css
├── netlify.toml
├── render.yaml
├── .gitignore
└── README.md
```

## Portfolio Features
- **Hero Section:** Dynamic copy highlighting FastAPI and JavaScript expertise
- **Project Showcase:** Three featured projects (CloudSync API, DataViz Dashboard, TaskFlow Manager)
- **Contact Form:** Enhanced error handling with comprehensive validation
- **Social Media:** Integrated links to GitHub, LinkedIn, Twitter, and email
- **Accessibility:** WCAG-compliant buttons with improved contrast and focus states
- **Responsive Design:** Mobile-first approach with smooth animations

## Documenting AI Usage (for assignment)
- **AI Tools Used:** Cursor (Composer, Chat), ChatGPT
- **Prompts:** "Generate responsive header with mobile menu", "Create FastAPI /contact endpoint with SQLite", "Rewrite hero copy to highlight FastAPI and JS skills", "Improve button accessibility and contrast", "Add social media integration", etc.
- **Value:** Speed up scaffolding, debugging, deployment config, content creation, and accessibility improvements.

## License
MIT
