from rapidfuzz import fuzz
import numpy as np

class TextEngine:
    def __init__(self):
        self.model = None
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
        except Exception:
            self.model = None

    def get_embedding(self, text: str) -> list:
        """Extracts dense vector embedding for bio text using sentence-transformers."""
        if self.model and text:
            try:
                emb = self.model.encode(text)
                return emb.tolist()
            except Exception:
                pass
        # Fallback deterministic vector seed
        vec = np.random.RandomState(abs(hash(text)) % (2**32 - 1)).randn(384)
        norm = np.linalg.norm(vec)
        return (vec / norm).tolist() if norm > 0 else vec.tolist()

    def get_bio_similarity(self, bio1: str, bio2: str) -> float:
        """Computes bio semantic & lexical similarity score combining dense vector embeddings and RapidFuzz token matching."""
        if not bio1 or not bio2:
            return 0.0
        fuzz_score = float(max(fuzz.token_set_ratio(bio1, bio2), fuzz.partial_ratio(bio1, bio2)))
        vec_sim = 0.0
        if self.model:
            try:
                emb1 = np.array(self.get_embedding(bio1))
                emb2 = np.array(self.get_embedding(bio2))
                vec_sim = float(round(max(0.0, np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))) * 100.0, 1))
            except Exception:
                pass
        return float(round(max(fuzz_score, vec_sim), 1))

    def get_handle_match_score(self, handle1: str, handle2: str) -> float:
        """Computes handle fuzzy string distance matching using RapidFuzz."""
        if not handle1 or not handle2:
            return 0.0
        clean1 = handle1.replace("@", "").lower().strip()
        clean2 = handle2.replace("@", "").lower().strip()
        ratio = fuzz.token_sort_ratio(clean1, clean2)
        return float(round(ratio, 1))

    def predict_all_possible_handles(self, name: str) -> list:
        """
        Multi-Model Username Predictor Engine.
        Generates ALL possible handle variations across 5 prediction models:
        Model A: Delimiter & Permutation Model (first_last, first.last, first-last, flast)
        Model B: Leetspeak Transformation Model (7 for s, 1 for i, 0 for o, 3 for e, 4 for a)
        Model C: Domain & Role Suffix Model (_dev, _ai, _official, _ui, _sec, _osint)
        Model D: Institutional & Location Model (_badnera, _prmitr)
        Model E: Year & Counter Model (_01, _26, _2026)
        """
        if not name:
            return []
        parts = [p.lower() for p in name.strip().split() if p]
        if not parts:
            return []

        first = parts[0]
        last = parts[-1] if len(parts) > 1 else ""

        predicted = set()

        # Model A: Basic Permutations & Delimiters
        if last:
            predicted.add(f"{first}{last}")
            predicted.add(f"{first}_{last}")
            predicted.add(f"{first}-{last}")
            predicted.add(f"{first}.{last}")
            predicted.add(f"{last}{first}")
            predicted.add(f"{last}_{first}")
            predicted.add(f"{last}-{first}")
            predicted.add(f"{last}.{first}")
            predicted.add(f"{first[0]}{last}")
            predicted.add(f"{first[0]}_{last}")
            predicted.add(f"{first[0]}-{last}")
            predicted.add(f"{first}{last[0]}")
            predicted.add(f"{first}_{last[0]}")
        else:
            predicted.add(first)

        # Model B: Leetspeak Substitutions (including 1 for 'i' and 1 for 'l')
        leet_maps = [
            {'s': '7', 'i': '1', 'l': '1', 'o': '0', 'e': '3', 'a': '4'},
            {'s': '7', 'i': '1', 'l': 'l', 'o': '0', 'e': '3', 'a': '4'}
        ]
        base_list = list(predicted)
        for handle in base_list:
            for lmap in leet_maps:
                leet_h = handle
                for k, v in lmap.items():
                    if k in leet_h:
                        leet_h = leet_h.replace(k, v)
                predicted.add(leet_h)

        # Model C: Domain & Role Suffix Model
        role_suffixes = ["dev", "ai", "ui", "sec", "osint", "official", "tech", "code"]
        for handle in base_list:
            for sfx in role_suffixes:
                predicted.add(f"{handle}_{sfx}")
                predicted.add(f"{handle}-{sfx}")

        # Model D: Institutional Suffix Model
        inst_suffixes = ["badnera", "prmitr", "in"]
        for handle in base_list:
            for sfx in inst_suffixes:
                predicted.add(f"{handle}_{sfx}")
                predicted.add(f"{handle}-{sfx}")

        # Model E: Year & Number Suffix Model
        num_suffixes = ["01", "26", "2026"]
        for handle in base_list:
            for num in num_suffixes:
                predicted.add(f"{handle}_{num}")
                predicted.add(f"{handle}{num}")

        return sorted(list(predicted))

text_engine = TextEngine()

