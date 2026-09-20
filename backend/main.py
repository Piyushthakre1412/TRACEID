from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import search, profile, graph
from app.db.loader import load_dataset

app = FastAPI(
    title="Digital Identity Intelligence & OSINT Resolution System API",
    description="Multi-Modal AI System for Disambiguation & Cross-Platform Knowledge Graph Construction (Team Ace)",
    version="1.0.0"
)

# Enable CORS for React frontend dashboard (port 5173 / localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    load_dataset()

app.include_router(search.router, prefix="/api", tags=["Search & Disambiguation"])
app.include_router(profile.router, prefix="/api", tags=["Identity Profile"])
app.include_router(graph.router, prefix="/api", tags=["Knowledge Graph"])

@app.get("/")
def root():
    return {
        "status": "online",
        "system": "Digital Identity Intelligence & OSINT Resolution System",
        "team": "Ace (PRMITR Badnera)",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
