# Digital Identity Intelligence 

> **Multi-Modal AI System for Identity Disambiguation & Cross-Platform Knowledge Graph Construction**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React 18](https://img.shields.io/badge/Frontend-React%2018-61DAFB.svg?logo=react&logoColor=black)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Build-Vite-646CFF.svg?logo=vite&logoColor=white)](https://vitejs.dev/)
[![DeepFace](https://img.shields.io/badge/AI-DeepFace%20%2F%20ArcFace-FF6F00.svg)](https://github.com/serengil/deepface)
[![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-orange.svg)](https://www.trychroma.com/)
[![NetworkX](https://img.shields.io/badge/Graph-NetworkX-green.svg)](https://networkx.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

##  Team Information

- **Team Name**: Ace
- **Problem Statement**: Public Profile & Digital Footprint Intelligence
- **Team Lead**: Piyush Thakre
- **Team Members**: Piyush Thakre, Om Patil, Satwik Mhasaye, Vyankatesh Raut
- **Institution**: Prof. Ram Meghe Institute Of Technology and Research, Badnera

---

##  Executive Summary

Modern individuals leave digital footprints fragmented across diverse web platforms—including GitHub, X (Twitter), LinkedIn, Instagram, Google Scholar, and institutional research portals. Resolving these disparate fragments into a single, verified canonical identity is a critical challenge in cybersecurity, open-source intelligence, and digital forensics. Simple handle lookup or text search fails due to name collisions, handle variations, altered bio descriptions, and cross-platform profile impersonation.

The **Digital Identity Intelligence Resolution System** is a software-only, privacy-compliant, **Multi-Modal AI System** that automatically discovers, correlates, disambiguates, and synthesizes fragmented web profiles. By integrating **512-D DeepFace/ArcFace facial vector embeddings**, **sentence-transformers bio semantic embeddings**, **RapidFuzz string distance algorithms**, and **NetworkX dynamic graph construction**, our system resolves cross-platform identities into an interactive Knowledge Graph complete with weighted confidence scores and audit-verifiable evidence trails.

---

##  Strategic Architecture & Pipeline Diagram

The system operates across a modular **4-Layer Intelligence Pipeline**:

```
+-----------------------------------------------------------------------------------+
|                               LAYER 1: DISCOVERY                                  |
|  - Web Crawling / API Connectors (GitHub, X, LinkedIn, Academic Portals, Images)  |
|  - Seed Query Input: Facial Image, User Handle, or Canonical Name                 |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                        LAYER 2: MULTI-MODAL FEATURE EXTRACTION                    |
|  +--------------------------+  +--------------------------+  +------------------+ |
|  |    DeepFace / ArcFace    |  |   sentence-transformers  |  |    RapidFuzz     | |
|  |  (512-D Facial Embed)    |  |  (all-MiniLM-L6-v2 Bio)  |  |  (Handle Match)  | |
|  +--------------+-----------+  +------------+-------------+  +--------+---------+ |
+-----------------|---------------------------|-------------------------|-----------+
                  |                           |                         |
                  v                           v                         v
+-----------------------------------------------------------------------------------+
|                     LAYER 3: MULTI-MODAL CONFIDENCE ENGINE                        |
|  - ChromaDB Vector Store Similarity Querying (Cosine Distance)                    |
|  - Multi-Modal Weighted Confidence Calculation:                                   |
|    Confidence = (0.40 * S_face) + (0.35 * S_bio) + (0.25 * S_handle)              |
|  - Threshold Filtering & False-Positive Elimination (T_min = 70.0%)               |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                       LAYER 4: SYNTHESIS & VISUALIZATION                          |
|  - NetworkX Graph Construction (Person, Handle, Organization, Project Nodes)      |
|  - FastAPI Backend REST Endpoints (/api/search, /api/profile, /api/graph)         |
|  - React + React Flow Interactive Graph Canvas + Recharts Activity Timeline       |
|  - Evidence Inspector & Audit Trail Side Panel                                    |
+-----------------------------------------------------------------------------------+
```

---

## Disambiguation Engine Formula

Identity correlation across multi-modal data streams is computed using a weighted confidence scoring model combining visual feature vectors, natural language semantics, and textual handle similarity.

### Multi-Modal Weighted Confidence Score

$$\text{Confidence} = \left( 0.40 \times S_{\text{face}} \right) + \left( 0.35 \times S_{\text{bio}} \right) + \left( 0.25 \times S_{\text{handle}} \right)$$

Where:

1. **Facial Similarity Score ($S_{\text{face}}$)**:
   Calculated using 512-dimensional feature vector extraction from ArcFace/DeepFace and normalized Cosine Similarity:
   $$S_{\text{face}} = \max\left(0, \frac{\vec{V}_{\text{seed}} \cdot \vec{V}_{\text{cand}}}{\|\vec{V}_{\text{seed}}\| \|\vec{V}_{\text{cand}}\|}\right) \times 100$$

2. **Bio Semantic Score ($S_{\text{bio}}$)**:
   Generated using `sentence-transformers` (`all-MiniLM-L6-v2`) dense vector embeddings of user bios, role descriptions, and institutional affiliations:
   $$S_{\text{bio}} = \left( \frac{\vec{E}_{\text{seed}} \cdot \vec{E}_{\text{cand}}}{\|\vec{E}_{\text{seed}}\| \|\vec{E}_{\text{cand}}\|} \right) \times 100$$

3. **Handle Fuzzy Score ($S_{\text{handle}}$)**:
   Computed using RapidFuzz Levenshtein and Token Sort Ratio algorithms across profile handles, aliases, and username variations:
   $$S_{\text{handle}} = \text{RapidFuzz.ratio}(\text{handle}_{\text{seed}}, \text{handle}_{\text{cand}})$$

### Decision Thresholds

| Confidence Score Range | Identity Resolution Status | Action / Visualization |
| :--- | :--- | :--- |
| **85.0% - 100.0%** | **Verified Match** | High-confidence canonical entity merge |
| **70.0% - 84.9%** | **Probable Match** | Linked node with flagged verification evidence |
| **< 70.0%** | **Ambiguous / Discarded** | Filtered out to avoid false-positive graph clutter |

---

##  Project Repository Structure

```
identity-intelligence-system/
│
├── dataset/                            <-- [1. LOCAL DATASET STORE]
│   ├── raw_profiles.json               # Profile bios, links, roles, events
│   ├── ground_truth_graph.json         # Known relationships & entity links
│   └── images/                         # Candidate photos (e.g., piyush.jpg)
│
├── backend/                            <-- [2. PYTHON FASTAPI BACKEND]
│   ├── app/
│   │   ├── api/
│   │   │   ├── search.py               # POST /api/search (Search by image/name)
│   │   │   ├── profile.py              # GET /api/profile/{id}
│   │   │   └── graph.py                # GET /api/graph/{id}
│   │   │
│   │   ├── services/
│   │   │   ├── face_engine.py          # DeepFace vector extraction & matching
│   │   │   ├── text_engine.py          # sentence-transformers bio embeddings
│   │   │   ├── disambiguation.py       # Multi-modal weighted scoring math
│   │   │   └── graph_builder.py        # NetworkX entity graph construction
│   │   │
│   │   ├── db/
│   │   │   ├── vector_db.py            # ChromaDB interface
│   │   │   └── loader.py               # Dataset ingestion script on startup
│   │   │
│   │   └── config.py                   # Thresholds & weight settings
│   │
│   ├── requirements.txt
│   └── main.py                         # Server entry point (FastAPI)
│
└── frontend/                           <-- [3. REACT DASHBOARD]
    ├── src/
    │   ├── components/
    │   │   ├── SearchSection.jsx       # Image upload & query input zone
    │   │   ├── KnowledgeGraph.jsx      # React Flow interactive graph canvas
    │   │   ├── ActivityTimeline.jsx    # Chronological event sequence
    │   │   ├── ProfileSummary.jsx      # Matched identity profile card
    │   │   └── EvidenceInspector.jsx   # Source verification & audit side panel
    │   │
    │   ├── api/
    │   │   └── client.js               # Axios / Fetch client to backend
    │   │
    │   ├── App.jsx                     # Dashboard layout manager
    │   └── main.jsx
    │
    ├── package.json
    └── vite.config.js
```

---

## 🛠️ Local Setup & Installation Guide

### Prerequisites
- **Python**: `v3.10` or higher
- **Node.js**: `v18.0` or higher & `npm`
- **Git**

### 1. Clone Repository
```bash
git clone https://github.com/Ace-PRMITR/digital-identity-intelligence.git
cd digital-identity-intelligence
```

### 2. Backend Setup (FastAPI Python)
```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI Development Server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
> The API server will start at `http://localhost:8000` with interactive Swagger docs at `http://localhost:8000/docs`.

### 3. Frontend Setup (React + Vite)
Open a new terminal window:
```bash
# Navigate to frontend folder
cd frontend

# Install npm packages
npm install

# Start Vite Development Server
npm run dev
```
> The web application will launch at `http://localhost:5173`.

---

## 📡 API Response Schema

The backend `/api/graph/{id}` endpoint returns resolved entity nodes, relationships, chronological activity timelines, confidence breakdowns, and verifiable audit trails:

```json
{
  "target_identity": {
    "person_id": "P_101",
    "canonical_name": "Piyush Thakre",
    "primary_image": "/dataset/images/piyush.jpg",
    "overall_confidence": 94.2,
    "confidence_breakdown": {
      "facial_similarity": 96.0,
      "bio_semantic_similarity": 93.5,
      "handle_match": 91.0
    }
  },
  "graph_data": {
    "nodes": [
      { "id": "P_101", "label": "Piyush Thakre", "type": "person" },
      { "id": "H_01", "label": "@piyush-thakre (GitHub)", "type": "handle" },
      { "id": "ORG_01", "label": "PRMITR Badnera", "type": "organization" },
      { "id": "PROJ_01", "label": "ACE / InterceptAI", "type": "project" }
    ],
    "edges": [
      { "source": "P_101", "target": "H_01", "relationship": "OWNED_BY", "confidence": 92.0 },
      { "source": "P_101", "target": "ORG_01", "relationship": "AFFILIATED_WITH", "confidence": 95.0 },
      { "source": "P_101", "target": "PROJ_01", "relationship": "CONTRIBUTED_TO", "confidence": 90.0 }
    ]
  },
  "timeline": [
    { "year": "2023", "event": "Enrolled at PRMITR Badnera", "category": "education" },
    { "year": "2026", "event": "Project ACE Created for Hack Synthesis 3.0", "category": "hackathon" }
  ],
  "evidence_trail": [
    {
      "node_id": "H_01",
      "source_url": "https://github.com/piyush-thakre",
      "verified_at": "2026-09-19",
      "proof_type": "Direct Bi-Directional URL Match"
    }
  ]
}
```

<p align="center">
  <b>Developed by Team Ace</b> • Prof. Ram Meghe Institute Of Technology and Research, Badnera (2026)
</p>
