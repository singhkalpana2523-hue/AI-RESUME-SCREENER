from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def generate_pdf_report(result: dict):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 40

    def draw_line(text):
        nonlocal y
        p.drawString(40, y, text)
        y -= 18

    # ----- HEADER -----
    draw_line("AI Resume Screening Report")
    draw_line("")

    draw_line(f"Final Score: {result.get('final_score', 'N/A')}")
    draw_line(f"Similarity: {result.get('similarity', 'N/A')}")
    draw_line(f"Decision: {result.get('decision', 'N/A')}")
    draw_line("")

    # ----- MATCHED SKILLS -----
    draw_line("Matched Skills:")
    for skill in result.get("matched_skills", []):
        draw_line(f"- {skill}")
    draw_line("")

    # ----- MISSING REQUIRED -----
    draw_line("Missing Required Skills:")
    for skill in result.get("missing_required_skills", []):
        draw_line(f"- {skill}")
    draw_line("")

    # ----- REWRITE SUGGESTIONS -----
    draw_line("Resume Rewrite Suggestions:")
    for section in result.get("resume_rewrite_suggestions", []):
        draw_line(f"{section.get('title', '')}")
        for skill in section.get("skills", []):
            draw_line(f"  - {skill}")
        draw_line("")

    p.save()
    buffer.seek(0)

    return buffer
