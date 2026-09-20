from app.config import settings

def calculate_confidence(
    facial_score: float,
    bio_score: float,
    handle_score: float,
    weight_face: float = 0.40,
    weight_bio: float = 0.35,
    weight_handle: float = 0.25
) -> dict:
    """
    Computes weighted confidence score using multi-modal formula:
    Confidence = (Weight_Face * Face Score) + (Weight_Bio * Bio Score) + (Weight_Handle * Handle Score)
    """
    face_contrib = weight_face * facial_score
    bio_contrib = weight_bio * bio_score
    handle_contrib = weight_handle * handle_score

    overall = round(face_contrib + bio_contrib + handle_contrib, 1)

    return {
        "overall_confidence": overall,
        "confidence_breakdown": {
            "facial_similarity": round(facial_score, 1),
            "bio_semantic_similarity": round(bio_score, 1),
            "handle_match": round(handle_score, 1)
        }
    }
