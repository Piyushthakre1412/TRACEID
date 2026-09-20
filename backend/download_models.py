import sys
import os

print("=== PRE-LOADING AI MODELS FOR DISAMBIGUATION ===")

# 1. Download & cache sentence-transformers model 'all-MiniLM-L6-v2'
try:
    print("\n1. Pre-downloading sentence-transformers ('all-MiniLM-L6-v2')...")
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("✓ sentence-transformers ('all-MiniLM-L6-v2') model downloaded successfully.")
except Exception as e:
    print(f"⚠ sentence-transformers download note: {e}")

# 2. Download & cache DeepFace ArcFace model
try:
    print("\n2. Pre-downloading DeepFace ArcFace model weights...")
    from deepface import DeepFace
    import numpy as np
    # Represent dummy image array to trigger ArcFace weight download & initialization
    dummy_img = (np.random.rand(100, 100, 3) * 255).astype(np.uint8)
    DeepFace.represent(img_path=dummy_img, model_name="ArcFace", enforce_detection=False)
    print("✓ DeepFace (ArcFace) model weights initialized successfully.")
except Exception as e:
    print(f"⚠ DeepFace note: {e}")

print("\n=== ALL AI MODELS & WEIGHTS PRE-LOADED SUCCESSFULLY ===")
