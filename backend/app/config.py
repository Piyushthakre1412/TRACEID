import os
from dotenv import load_dotenv

# Load .env file from backend directory or parent root
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
if not os.path.exists(dotenv_path):
    dotenv_path = os.path.join(os.path.dirname(__file__), "..", "..", ".env")

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Settings:
    # Server & Port Settings
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    BACKEND_HOST: str = os.getenv("BACKEND_HOST", "0.0.0.0")
    BACKEND_PORT: int = int(os.getenv("BACKEND_PORT", 8000))
    FRONTEND_PORT: int = int(os.getenv("FRONTEND_PORT", 5173))
    ALLOWED_CORS_ORIGINS: list = os.getenv("ALLOWED_CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",")

    # Security & JWT Tokens
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "ace_digital_identity_osint_super_secret_jwt_key_2026_prmitr")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
    REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7))
    SYSTEM_API_KEY: str = os.getenv("SYSTEM_API_KEY", "ace_osint_resolution_api_key_v1_secure")

    # OSINT Scraping API Keys
    GITHUB_PERSONAL_ACCESS_TOKEN: str = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN", "")
    TWITTER_BEARER_TOKEN: str = os.getenv("TWITTER_BEARER_TOKEN", "")
    LINKEDIN_SESSION_COOKIE: str = os.getenv("LINKEDIN_SESSION_COOKIE", "")
    GOOGLE_SEARCH_API_KEY: str = os.getenv("GOOGLE_SEARCH_API_KEY", "")
    GOOGLE_SEARCH_ENGINE_ID: str = os.getenv("GOOGLE_SEARCH_CX") or os.getenv("GOOGLE_SEARCH_ENGINE_ID", "e42a18f00575a47c4")
    SCRAPING_USER_AGENT: str = os.getenv("SCRAPING_USER_AGENT", "OSINT-IdentityBot/1.0")

    # Disambiguation Weights
    WEIGHT_FACE: float = float(os.getenv("WEIGHT_FACIAL", 0.40))
    WEIGHT_BIO: float = float(os.getenv("WEIGHT_BIO", 0.35))
    WEIGHT_HANDLE: float = float(os.getenv("WEIGHT_HANDLE", 0.25))

    # Thresholds
    MIN_CONFIDENCE_THRESHOLD: float = float(os.getenv("MIN_CONFIDENCE_THRESHOLD", 70.0))
    HIGH_CONFIDENCE_THRESHOLD: float = float(os.getenv("HIGH_CONFIDENCE_THRESHOLD", 85.0))

    # Data Paths
    DATASET_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "dataset"))
    PROFILES_PATH: str = os.path.join(DATASET_DIR, "raw_profiles.json")
    GRAPH_PATH: str = os.path.join(DATASET_DIR, "ground_truth_graph.json")
    CHROMADB_PERSIST_DIR: str = os.getenv("CHROMADB_PERSIST_DIR", "./data/chroma_db")

settings = Settings()
