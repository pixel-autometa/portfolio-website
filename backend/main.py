from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import Optional
import sqlite3
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Sajid's Portfolio API",
    description="Backend API for Sajid's portfolio website contact form",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "https://sajid-portfolio.netlify.app",
        os.getenv("FRONTEND_ORIGIN", "https://sajid-portfolio.netlify.app")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
DATABASE_URL = "portfolio.db"

def init_db():
    """Initialize the database with contacts table"""
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()
    logger.info("Database initialized successfully")

# Initialize database on startup
init_db()

# Pydantic models
class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    message: str

class ContactResponse(BaseModel):
    success: bool
    message: str

# Routes
@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Sajid's Portfolio API",
        "version": "1.0.0",
        "status": "active",
        "endpoints": {
            "health": "/health",
            "contact": "/contact",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint for Render"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/contact", response_model=ContactResponse)
async def submit_contact(contact: ContactMessage):
    """Submit a contact form message"""
    try:
        # Validate input
        if not contact.name.strip():
            raise HTTPException(status_code=400, detail="Name is required")
        if not contact.message.strip():
            raise HTTPException(status_code=400, detail="Message is required")
        
        # Store in database
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO contacts (name, email, message)
            VALUES (?, ?, ?)
        """, (contact.name.strip(), contact.email, contact.message.strip()))
        conn.commit()
        conn.close()
        
        logger.info(f"New contact message from {contact.name} ({contact.email})")
        
        return ContactResponse(
            success=True,
            message="Thank you for your message! I'll get back to you soon."
        )
        
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error occurred")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@app.get("/contacts")
async def get_contacts():
    """Get all contact messages (for admin purposes)"""
    try:
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, name, email, message, created_at
            FROM contacts
            ORDER BY created_at DESC
        """)
        contacts = cursor.fetchall()
        conn.close()
        
        return {
            "contacts": [
                {
                    "id": contact[0],
                    "name": contact[1],
                    "email": contact[2],
                    "message": contact[3],
                    "created_at": contact[4]
                }
                for contact in contacts
            ]
        }
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error occurred")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
