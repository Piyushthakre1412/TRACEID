import json
import os
from app.config import settings
from app.db.sqlite_db import sqlite_db
from app.db.vector_db import vector_db
from app.services.graph_builder import graph_builder
from app.services.text_engine import text_engine

profiles_cache = {}

def load_dataset():
    """Ingests dataset files (candidates_dataset.json), populates SQLite DB, ChromaDB, and NetworkX Graph."""
    global profiles_cache
    dataset_path = os.path.join(settings.DATASET_DIR, "candidates_dataset.json")
    if not os.path.exists(dataset_path):
        dataset_path = settings.PROFILES_PATH

    if os.path.exists(dataset_path):
        with open(dataset_path, "r", encoding="utf-8") as f:
            candidates = json.load(f)
            for candidate in candidates:
                p_id = candidate["person_id"]
                profiles_cache[p_id] = candidate
                # 1. Store in SQLite Database
                sqlite_db.upsert_candidate(candidate)
                
                # 2. Extract bio embedding and upsert to ChromaDB Vector DB
                bio_text = " ".join(candidate.get("bios", [])) or candidate["canonical_name"]
                vector = text_engine.get_embedding(bio_text)
                vector_db.upsert_candidate_vector(
                    person_id=p_id,
                    vector=vector,
                    metadata={"name": candidate["canonical_name"], "institution": candidate.get("institution", "")}
                )

    # Build NetworkX Graph automatically for all candidates
    graph_builder.build_from_candidates(list(profiles_cache.values()))

def get_profile_by_id(person_id: str):
    cached = profiles_cache.get(person_id)
    if cached:
        return cached
    return sqlite_db.get_candidate(person_id)

def get_all_profiles():
    if profiles_cache:
        return list(profiles_cache.values())
    return sqlite_db.get_all_candidates()
