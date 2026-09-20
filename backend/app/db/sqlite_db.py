import sqlite3
import json
import os
from typing import Optional, List, Dict, Any

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "candidates.db"))

class SQLiteDB:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.init_db()

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS candidates (
                    person_id TEXT PRIMARY KEY,
                    canonical_name TEXT NOT NULL,
                    primary_image TEXT,
                    institution TEXT,
                    roles_json TEXT,
                    handles_json TEXT,
                    bios_json TEXT,
                    contacts_json TEXT,
                    mutual_contacts_json TEXT,
                    projects_json TEXT,
                    timeline_json TEXT,
                    evidence_json TEXT
                )
            """)
            conn.commit()
            
            # Migration check for pre-existing databases
            cursor.execute("PRAGMA table_info(candidates)")
            existing_cols = [row["name"] for row in cursor.fetchall()]
            if "contacts_json" not in existing_cols:
                cursor.execute("ALTER TABLE candidates ADD COLUMN contacts_json TEXT")
            if "mutual_contacts_json" not in existing_cols:
                cursor.execute("ALTER TABLE candidates ADD COLUMN mutual_contacts_json TEXT")
            conn.commit()

    def upsert_candidate(self, candidate: Dict[str, Any]):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO candidates (
                    person_id, canonical_name, primary_image, institution,
                    roles_json, handles_json, bios_json, contacts_json, mutual_contacts_json,
                    projects_json, timeline_json, evidence_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(person_id) DO UPDATE SET
                    canonical_name=excluded.canonical_name,
                    primary_image=excluded.primary_image,
                    institution=excluded.institution,
                    roles_json=excluded.roles_json,
                    handles_json=excluded.handles_json,
                    bios_json=excluded.bios_json,
                    contacts_json=excluded.contacts_json,
                    mutual_contacts_json=excluded.mutual_contacts_json,
                    projects_json=excluded.projects_json,
                    timeline_json=excluded.timeline_json,
                    evidence_json=excluded.evidence_json
            """, (
                candidate["person_id"],
                candidate["canonical_name"],
                candidate.get("primary_image", ""),
                candidate.get("institution", ""),
                json.dumps(candidate.get("roles", [])),
                json.dumps(candidate.get("handles", [])),
                json.dumps(candidate.get("bios", [])),
                json.dumps(candidate.get("contacts", {})),
                json.dumps(candidate.get("mutual_contacts", [])),
                json.dumps(candidate.get("projects", [])),
                json.dumps(candidate.get("timeline", [])),
                json.dumps(candidate.get("evidence_trail", []))
            ))
            conn.commit()

    def get_candidate(self, person_id: str) -> Optional[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM candidates WHERE person_id = ?", (person_id,))
            row = cursor.fetchone()
            if not row:
                return None
            keys = row.keys()
            return {
                "person_id": row["person_id"],
                "canonical_name": row["canonical_name"],
                "primary_image": row["primary_image"],
                "institution": row["institution"],
                "roles": json.loads(row["roles_json"]) if row["roles_json"] else [],
                "handles": json.loads(row["handles_json"]) if row["handles_json"] else [],
                "bios": json.loads(row["bios_json"]) if row["bios_json"] else [],
                "contacts": json.loads(row["contacts_json"]) if "contacts_json" in keys and row["contacts_json"] else {},
                "mutual_contacts": json.loads(row["mutual_contacts_json"]) if "mutual_contacts_json" in keys and row["mutual_contacts_json"] else [],
                "projects": json.loads(row["projects_json"]) if row["projects_json"] else [],
                "timeline": json.loads(row["timeline_json"]) if row["timeline_json"] else [],
                "evidence_trail": json.loads(row["evidence_json"]) if row["evidence_json"] else []
            }

    def get_all_candidates(self) -> List[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM candidates")
            rows = cursor.fetchall()
            candidates = []
            for row in rows:
                keys = row.keys()
                candidates.append({
                    "person_id": row["person_id"],
                    "canonical_name": row["canonical_name"],
                    "primary_image": row["primary_image"],
                    "institution": row["institution"],
                    "roles": json.loads(row["roles_json"]) if row["roles_json"] else [],
                    "handles": json.loads(row["handles_json"]) if row["handles_json"] else [],
                    "bios": json.loads(row["bios_json"]) if row["bios_json"] else [],
                    "contacts": json.loads(row["contacts_json"]) if "contacts_json" in keys and row["contacts_json"] else {},
                    "mutual_contacts": json.loads(row["mutual_contacts_json"]) if "mutual_contacts_json" in keys and row["mutual_contacts_json"] else [],
                    "projects": json.loads(row["projects_json"]) if row["projects_json"] else [],
                    "timeline": json.loads(row["timeline_json"]) if row["timeline_json"] else [],
                    "evidence_trail": json.loads(row["evidence_json"]) if row["evidence_json"] else []
                })
            return candidates


sqlite_db = SQLiteDB()
