def explain_match(
    similarity,
    required_skills,
    preferred_skills,
    missing_required,
    missing_preferred,
    final_score
):
    explanation_parts = []

    # Semantic similarity
    if similarity > 70:
        explanation_parts.append(
            "Resume content is strongly aligned with the job description."
        )
    elif similarity > 40:
        explanation_parts.append(
            "Resume content is moderately aligned with the job description."
        )
    else:
        explanation_parts.append(
            "Resume content has low alignment with the job description."
        )

    # Required skills
    if not missing_required:
        explanation_parts.append(
            "All required skills are present."
        )
    else:
        explanation_parts.append(
            f"Missing required skills: {', '.join(missing_required)}."
        )

    # Preferred skills
    if missing_preferred:
        explanation_parts.append(
            f"Some preferred skills are missing: {', '.join(missing_preferred)}."
        )

    return " ".join(explanation_parts)
def resume_rewrite_suggestions(missing_required, missing_preferred):
    suggestions = []

    # Remove duplicates just in case
    missing_required = list(set(missing_required))
    missing_preferred = list(set(missing_preferred))

    if missing_required:
        suggestions.append({
            "type": "required",
            "title": "Strengthen Required Skills",
            "description": "Add measurable bullet points demonstrating hands-on experience in:",
            "skills": missing_required
        })

    if missing_preferred:
        suggestions.append({
            "type": "preferred",
            "title": "Improve Preferred Skills Alignment",
            "description": "Mention familiarity, certifications, or learning projects related to:",
            "skills": missing_preferred
        })

    return suggestions

