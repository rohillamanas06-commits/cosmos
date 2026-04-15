from fastapi import FastAPI, Query, HTTPException, Path, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from enum import Enum
import os
from dotenv import load_dotenv
import logging

try:
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    SENDGRID_AVAILABLE = True
except ImportError:
    SENDGRID_AVAILABLE = False

# Load environment variables
load_dotenv()

# Import data from data.py
from data import (
    COSMIC_OBJECTS_PHASE1,
    COSMIC_OBJECTS_PHASE2,
    COSMIC_OBJECTS_PHASE3,
    COSMIC_OBJECTS_PHASE4,
    COSMIC_OBJECTS_PHASE5,
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables
API_VERSION = os.getenv("API_VERSION", "1.0.0")
APP_NAME = os.getenv("APP_NAME", "Cosmos API")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
PHASE_LIMIT = int(os.getenv("PHASE_LIMIT", "5"))

# Initialize FastAPI app
app = FastAPI(
    title=APP_NAME,
    description="API for accessing and querying cosmic objects data",
    version=API_VERSION,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Combine all phases into single dataset
ALL_OBJECTS = (
    COSMIC_OBJECTS_PHASE1
    + COSMIC_OBJECTS_PHASE2
    + COSMIC_OBJECTS_PHASE3
    + COSMIC_OBJECTS_PHASE4
    + COSMIC_OBJECTS_PHASE5
)

# Pydantic models for responses
class CosmicObjectResponse(BaseModel):
    """Response model for a cosmic object"""
    id: str
    name: str
    category: str
    subtype: Optional[str] = None
    tags: Optional[List[str]] = None
    difficulty_level: Optional[str] = None

    class Config:
        from_attributes = True


class CosmicObjectDetailResponse(BaseModel):
    """Detailed response model for a cosmic object"""
    id: str
    name: str
    category: str
    subtype: Optional[str] = None
    tags: Optional[List[str]] = None
    difficulty_level: Optional[str] = None
    spatial: Optional[Dict[str, Any]] = None
    physical: Optional[Dict[str, Any]] = None
    detailed_description: Optional[str] = None
    scientific_facts: Optional[List[str]] = None

    class Config:
        from_attributes = True


class CategoryEnum(str, Enum):
    """Enum for filtering by category"""
    GALAXY = "Galaxy"
    BLACK_HOLE = "Black Hole"
    PULSAR = "Pulsar"
    STAR = "Star"
    QUASAR = "Quasar"
    NEBULA = "Nebula"
    GALAXY_CLUSTER = "Galaxy Cluster"
    SUPERNOVA = "Supernova"
    EXOPLANET = "Exoplanet"
    X_RAY_SOURCE = "X-ray Source"
    GAMMA_RAY_BURST = "Gamma-Ray Burst"
    COSMIC_STRING = "Cosmic String"
    PRIMORDIAL_BLACK_HOLE = "Primordial Black Hole"
    AXION_STAR = "Axion Star"
    DARK_MATTER_STRUCTURE = "Dark Matter Structure"


class DifficultyEnum(str, Enum):
    """Enum for filtering by difficulty level"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


class ContactRequest(BaseModel):
    """Request model for contact form submissions"""
    name: str = Field(..., min_length=1, max_length=100)
    email: str = Field(...)
    message: str = Field(..., min_length=1, max_length=5000)


# Helper functions
def search_objects(
    query: Optional[str] = None,
    category: Optional[str] = None,
    difficulty: Optional[str] = None,
    skip: int = 0,
    limit: int = 50,
) -> List[Dict[str, Any]]:
    """
    Search cosmic objects based on filters.
    
    Args:
        query: Search term to match against name, category, and tags
        category: Filter by category
        difficulty: Filter by difficulty level
        skip: Number of results to skip (pagination)
        limit: Maximum number of results to return
    
    Returns:
        List of filtered cosmic objects
    """
    results = ALL_OBJECTS.copy()

    # Filter by category
    if category:
        results = [obj for obj in results if obj.get("category", "").lower() == category.lower()]

    # Filter by difficulty
    if difficulty:
        results = [obj for obj in results if obj.get("difficulty_level", "").lower() == difficulty.lower()]

    # Search query
    if query:
        query_lower = query.lower()
        results = [
            obj for obj in results
            if (
                query_lower in obj.get("name", "").lower()
                or query_lower in obj.get("category", "").lower()
                or any(query_lower in tag.lower() for tag in obj.get("tags", []))
            )
        ]

    # Apply pagination
    return results[skip : skip + limit]


def get_object_by_id(object_id: str) -> Optional[Dict[str, Any]]:
    """Get a cosmic object by its ID."""
    for obj in ALL_OBJECTS:
        if obj.get("id") == object_id:
            return obj
    return None


def get_statistics() -> Dict[str, Any]:
    """Get statistics about the cosmic objects database."""
    categories = {}
    difficulties = {}

    for obj in ALL_OBJECTS:
        category = obj.get("category", "Unknown")
        difficulty = obj.get("difficulty_level", "Unknown")

        categories[category] = categories.get(category, 0) + 1
        difficulties[difficulty] = difficulties.get(difficulty, 0) + 1

    return {
        "total_objects": len(ALL_OBJECTS),
        "total_categories": len(categories),
        "total_difficulties": len(difficulties),
        "categories": categories,
        "difficulties": difficulties,
        "phases": {
            "phase_1": len(COSMIC_OBJECTS_PHASE1),
            "phase_2": len(COSMIC_OBJECTS_PHASE2),
            "phase_3": len(COSMIC_OBJECTS_PHASE3),
            "phase_4": len(COSMIC_OBJECTS_PHASE4),
            "phase_5": len(COSMIC_OBJECTS_PHASE5),
        },
    }


# Routes
@app.get("/", tags=["Health"])
async def root():
    """Root endpoint - API health check."""
    return {
        "app_name": APP_NAME,
        "version": API_VERSION,
        "status": "online",
        "message": "Welcome to the Cosmos API",
    }


@app.get("/health", tags=["Health"])
async def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "total_objects": len(ALL_OBJECTS),
        "database_loaded": True,
    }


@app.get("/stats", tags=["Statistics"])
async def statistics():
    """Get database statistics."""
    return get_statistics()


@app.get("/objects", response_model=List[CosmicObjectResponse], tags=["Objects"])
async def list_objects(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of items to return"),
    category: Optional[str] = Query(None, description="Filter by category"),
    difficulty: Optional[str] = Query(None, description="Filter by difficulty level"),
):
    """
    List all cosmic objects with optional filtering and pagination.
    
    Query parameters:
    - skip: Number of items to skip (default: 0)
    - limit: Maximum items to return (default: 50, max: 100)
    - category: Filter by category name
    - difficulty: Filter by difficulty level (beginner, intermediate, advanced, expert)
    """
    results = search_objects(
        query=None,
        category=category,
        difficulty=difficulty,
        skip=skip,
        limit=limit,
    )
    return results


@app.get("/objects/search", response_model=List[CosmicObjectResponse], tags=["Objects"])
async def search(
    q: str = Query(..., description="Search term"),
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of items to return"),
):
    """
    Search cosmic objects by name, category, or tags.
    
    Query parameters:
    - q: Search query (required)
    - skip: Number of items to skip (default: 0)
    - limit: Maximum items to return (default: 50, max: 100)
    """
    if not q or len(q.strip()) < 2:
        raise HTTPException(status_code=400, detail="Search query must be at least 2 characters")

    results = search_objects(
        query=q,
        category=None,
        difficulty=None,
        skip=skip,
        limit=limit,
    )

    if not results:
        raise HTTPException(status_code=404, detail="No objects found matching search criteria")

    return results


@app.get("/objects/{object_id}", response_model=CosmicObjectDetailResponse, tags=["Objects"])
async def get_object(
    object_id: str = Path(..., description="The ID of the cosmic object"),
):
    """
    Get detailed information about a specific cosmic object.
    
    Path parameters:
    - object_id: The unique identifier of the cosmic object
    """
    obj = get_object_by_id(object_id)

    if not obj:
        raise HTTPException(status_code=404, detail="Cosmic object not found")

    return obj


@app.get("/categories", tags=["Metadata"])
async def get_categories():
    """Get all available categories."""
    categories = set()
    for obj in ALL_OBJECTS:
        category = obj.get("category")
        if category:
            categories.add(category)

    return {
        "categories": sorted(list(categories)),
        "count": len(categories),
    }


@app.get("/categories/{category}", response_model=List[CosmicObjectResponse], tags=["Metadata"])
async def get_by_category(
    category: str = Path(..., description="Category name"),
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of items to return"),
):
    """
    Get all objects in a specific category.
    
    Path parameters:
    - category: The category name
    """
    results = search_objects(
        query=None,
        category=category,
        difficulty=None,
        skip=skip,
        limit=limit,
    )

    if not results:
        raise HTTPException(status_code=404, detail=f"No objects found in category: {category}")

    return results


@app.get("/difficulties/{difficulty}", response_model=List[CosmicObjectResponse], tags=["Metadata"])
async def get_by_difficulty(
    difficulty: DifficultyEnum = Path(..., description="Difficulty level"),
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of items to return"),
):
    """
    Get all objects with a specific difficulty level.
    
    Path parameters:
    - difficulty: One of - beginner, intermediate, advanced, expert
    """
    results = search_objects(
        query=None,
        category=None,
        difficulty=difficulty.value,
        skip=skip,
        limit=limit,
    )

    if not results:
        raise HTTPException(status_code=404, detail=f"No objects found with difficulty: {difficulty.value}")

    return results


@app.get("/phases/{phase_num}", response_model=List[CosmicObjectResponse], tags=["Phases"])
async def get_phase(
    phase_num: int = Path(..., ge=1, le=5, description="Phase number (1-5)"),
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of items to return"),
):
    """
    Get objects from a specific phase.
    
    Path parameters:
    - phase_num: Phase number (1-5)
    """
    phases = {
        1: COSMIC_OBJECTS_PHASE1,
        2: COSMIC_OBJECTS_PHASE2,
        3: COSMIC_OBJECTS_PHASE3,
        4: COSMIC_OBJECTS_PHASE4,
        5: COSMIC_OBJECTS_PHASE5,
    }

    phase_objects = phases.get(phase_num, [])
    if not phase_objects:
        raise HTTPException(status_code=404, detail=f"Phase {phase_num} not found")

    return phase_objects[skip : skip + limit]


@app.get("/random", response_model=CosmicObjectDetailResponse, tags=["Objects"])
async def get_random():
    """Get a random cosmic object."""
    import random

    if not ALL_OBJECTS:
        raise HTTPException(status_code=500, detail="No objects available")

    random_object = random.choice(ALL_OBJECTS)
    return random_object


@app.get("/advanced-search", response_model=List[CosmicObjectResponse], tags=["Objects"])
async def advanced_search(
    name: Optional[str] = Query(None, description="Search in name"),
    category: Optional[str] = Query(None, description="Filter by category"),
    difficulty: Optional[str] = Query(None, description="Filter by difficulty"),
    tag: Optional[str] = Query(None, description="Filter by tag"),
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(50, ge=1, le=100, description="Maximum number to return"),
):
    """
    Advanced search with multiple filter options.
    
    Query parameters:
    - name: Search term for object name
    - category: Filter by category
    - difficulty: Filter by difficulty level
    - tag: Filter by tag
    - skip: Number of items to skip (default: 0)
    - limit: Maximum items to return (default: 50, max: 100)
    """
    results = ALL_OBJECTS.copy()

    # Apply filters
    if name:
        name_lower = name.lower()
        results = [obj for obj in results if name_lower in obj.get("name", "").lower()]

    if category:
        results = [obj for obj in results if obj.get("category", "").lower() == category.lower()]

    if difficulty:
        results = [obj for obj in results if obj.get("difficulty_level", "").lower() == difficulty.lower()]

    if tag:
        tag_lower = tag.lower()
        results = [obj for obj in results if any(tag_lower in t.lower() for t in obj.get("tags", []))]

    if not results:
        raise HTTPException(status_code=404, detail="No objects found matching all criteria")

    return results[skip : skip + limit]


@app.post("/contact", tags=["Contact"])
async def send_contact_email(contact: ContactRequest):
    """
    Send a contact form email using SendGrid.
    
    Request body:
    - name: Sender's name
    - email: Sender's email address
    - message: The contact message
    """
    try:
        if not SENDGRID_AVAILABLE:
            raise HTTPException(
                status_code=500,
                detail="Email service is not configured. Please install sendgrid: pip install sendgrid"
            )
        
        # Get SendGrid configuration from environment
        sendgrid_api_key = os.getenv("SENDGRID_API_KEY")
        from_email = os.getenv("SENDGRID_FROM_EMAIL")
        
        if not sendgrid_api_key or not from_email:
            logger.error("SendGrid configuration missing")
            raise HTTPException(
                status_code=500,
                detail="Email service is not properly configured"
            )
        
        # Initialize SendGrid client
        sg = SendGridAPIClient(sendgrid_api_key)
        
        # Create email message
        email_body = f"""New Contact Form Submission

Name: {contact.name}
Email: {contact.email}

Message:
{contact.message}"""
        
        mail = Mail(
            from_email=from_email,
            to_emails=from_email,
            subject=f"New Contact Form Submission from {contact.name}",
            plain_text_content=email_body
        )
        
        # Send email
        response = sg.send(mail)
        
        logger.info(f"Contact email sent successfully. Status: {response.status_code}")
        
        return {
            "success": True,
            "message": "Thank you for your message. We'll get back to you soon!"
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error sending contact email: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to send email: {str(e)}"
        )


# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "status_code": exc.status_code},
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Generic exception handler."""
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "status_code": 500},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload=DEBUG,
    )
