# Sajid's Portfolio Backend API

FastAPI backend for Sajid's portfolio website contact form.

## Features

- **Contact Form API**: Handles form submissions with validation
- **CORS Support**: Configured for frontend integration
- **SQLite Database**: Stores contact messages
- **Health Check**: Endpoint for Render monitoring
- **Input Validation**: Email and text validation using Pydantic
- **Error Handling**: Comprehensive error responses

## API Endpoints

- `GET /` - API information
- `GET /health` - Health check for Render
- `POST /contact` - Submit contact form
- `GET /contacts` - Get all messages (admin)
- `GET /docs` - Interactive API documentation

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload

# Server runs at http://127.0.0.1:8000
# API docs at http://127.0.0.1:8000/docs
```

## Environment Variables

- `FRONTEND_ORIGIN` - Frontend URL for CORS (default: https://sajid-portfolio.netlify.app)

## Database

Uses SQLite with automatic table creation. Database file: `portfolio.db`

## Deployment

Deploy to Render using the `render.yaml` configuration file.
