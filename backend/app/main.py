from fastapi import FastAPI, UploadFile, File, Form, Body

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.resume_parser import extract_text_from_pdf
from app.skill_extractor import extract_resume_skills, extract_jd_skills
from app.matcher import calculate_similarity
from app.scorer import final_score
from app.explainer import explain_match, resume_rewrite_suggestions
from app.report import generate_pdf_report

# ---------------------------------
# CREATE APP
# ---------------------------------
app = FastAPI(title="AI Resume Screener")

# ---------------------------------
# CORS (React)
# ---------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------
# SIMPLE DECISION LOGIC
# ---------------------------------
def recommendation(score: float) -> str:
    if score >= 75:
        return "Strongly Recommended"
    elif score >= 55:
        return "Recommended"
    elif score >= 40:
        return "Borderline"
    else:
        return "Not Recommended"

# ---------------------------------
# ANALYZE ROUTE
# ---------------------------------
@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    # -------- TEXT EXTRACTION --------
    resume_text = extract_text_from_pdf(resume.file)

    # -------- SKILL EXTRACTION --------
    resume_skills = extract_resume_skills(resume_text)
    required_skills, preferred_skills = extract_jd_skills(job_description)

    missing_required = list(set(required_skills) - set(resume_skills))
    missing_preferred = list(set(preferred_skills) - set(resume_skills))

    # -------- SEMANTIC SIMILARITY --------
    similarity = float(calculate_similarity(resume_text, job_description))

    # -------- SKILL SCORES --------
    required_score = (
        (len(required_skills) - len(missing_required))
        / max(len(required_skills), 1)
    ) * 100

    preferred_score = (
        (len(preferred_skills) - len(missing_preferred))
        / max(len(preferred_skills), 1)
    ) * 100
    # -------- OVERALL SKILL MATCH --------
    skill_match = (0.7 * required_score) + (0.3 * preferred_score)

    # -------- FINAL SCORE --------
    score, score_breakdown = final_score(
        similarity,
        required_score,
        preferred_score
    )

    decision = recommendation(score)

    # -------- EXPLANATION --------
    explanation = explain_match(
        similarity=similarity,
        required_skills=required_skills,
        preferred_skills=preferred_skills,
        missing_required=missing_required,
        missing_preferred=missing_preferred,
        final_score=score
    )

    # -------- REWRITE SUGGESTIONS --------
    rewrite_suggestions = resume_rewrite_suggestions(
        missing_required,
        missing_preferred
    )

    suggestions = (
        rewrite_suggestions
        if rewrite_suggestions
        else ["Resume is well-aligned. No major improvements needed."]
    )

    # -------- RESPONSE --------
    return {
        "similarity": float(similarity),
        "skill_match": float(skill_match),
        "final_score": float(score),
        "score_breakdown": score_breakdown,
        "decision": decision,
        "matched_skills": list(resume_skills),
        "missing_required_skills": missing_required,
        "missing_preferred_skills": missing_preferred,
        "explanation": explanation,
        "improvement_suggestions": suggestions,
        "resume_rewrite_suggestions": rewrite_suggestions
    }


# ---------------------------------
# REQUEST MODEL FOR PDF DOWNLOAD
# ---------------------------------
class ReportRequest(BaseModel):
    similarity: float
    final_score: float
    decision: str
    explanation: str


# ---------------------------------
# PDF DOWNLOAD ROUTE
# ---------------------------------
@app.post("/download-report")
async def download_report(data: dict = Body(...)):
    pdf_buffer = generate_pdf_report(data)

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=resume_report.pdf"
        }
    )
