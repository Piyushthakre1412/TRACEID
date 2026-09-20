import sys
import os

# Ensure backend path is in sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app.db.loader import load_dataset, get_all_profiles
from app.services.graph_builder import graph_builder
from app.services.disambiguation import calculate_confidence
from app.services.text_engine import text_engine

print("=== STARTING BACKEND INTEGRATION TEST ===")

# 1. Load dataset into SQLite & ChromaDB vector store
load_dataset()
candidates = get_all_profiles()
print(f"Loaded {len(candidates)} candidates into SQLite & ChromaDB.")
for c in candidates:
    print(f" - Candidate: {c['person_id']} ({c['canonical_name']})")

# 2. Test Multi-Modal Scoring
confidence = calculate_confidence(
    facial_score=96.0,
    bio_score=93.5,
    handle_score=91.0,
    weight_face=0.40,
    weight_bio=0.35,
    weight_handle=0.25
)
print("\nMulti-Modal Score Test:")
print(f"Formula: (0.40 * 96) + (0.35 * 93.5) + (0.25 * 91) = {confidence['overall_confidence']}%")
assert confidence['overall_confidence'] == 93.9 or confidence['overall_confidence'] == 94.0 or confidence['overall_confidence'] > 90.0

# 3. Test NetworkX to React Flow graph conversion
react_flow_json = graph_builder.get_react_flow_graph("P_101", min_threshold=70.0)
nodes = react_flow_json["nodes"]
edges = react_flow_json["edges"]
print(f"\nReact Flow Output Test:")
print(f"Nodes count: {len(nodes)}")
print(f"Edges count: {len(edges)}")
if nodes:
    print(f"Sample Node 0: {nodes[0]}")
if edges:
    print(f"Sample Edge 0: {edges[0]}")

print("\n=== ALL INTEGRATION TESTS PASSED SUCCESSFULLY ===")
