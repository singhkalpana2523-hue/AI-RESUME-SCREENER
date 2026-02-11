def final_score(similarity, required_score, preferred_score):
    SIM_WEIGHT = 0.5
    REQ_WEIGHT = 0.35
    PREF_WEIGHT = 0.15

    similarity_contribution = similarity * SIM_WEIGHT
    required_contribution = required_score * REQ_WEIGHT
    preferred_contribution = preferred_score * PREF_WEIGHT

    total_score = (
        similarity_contribution +
        required_contribution +
        preferred_contribution
    )

    return round(total_score, 2), {
        "semantic_similarity": {
            "value": round(similarity, 2),
            
            "contribution": round(similarity_contribution, 2)
        },
        "required_skills": {
            "value": round(required_score, 2),
            
            "contribution": round(required_contribution, 2)
        },
        "preferred_skills": {
            "value": round(preferred_score, 2),
            
            "contribution": round(preferred_contribution, 2)
        }
    }
