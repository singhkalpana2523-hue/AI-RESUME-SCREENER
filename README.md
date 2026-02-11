📄 AI Resume Screener

An AI-powered Resume Screening and Analysis System that evaluates resumes against a given job description using semantic similarity, skill extraction, weighted scoring, and automated PDF report generation.

🚀 Project Overview

AI Resume Screener helps candidates and recruiters:

Compare resumes with job descriptions

Calculate semantic similarity

Evaluate required vs preferred skill match

Generate a weighted final score

Provide resume rewrite suggestions

Export a structured PDF analysis report

This project simulates a real-world ATS (Applicant Tracking System) workflow.

🧠 Does It Use AI?

Yes.

The system uses:

Semantic similarity computation (NLP-based text matching)

Resume and JD text processing

Skill extraction logic

Weighted scoring model

While it is not using large-scale LLM APIs, it applies core AI concepts:

Natural Language Processing

Text similarity modeling

Intelligent scoring logic

Heuristic-based resume enhancement suggestions

🏗️ Tech Stack
🔹 Frontend

React (Vite)

JavaScript

CSS (custom UI, animated progress bars)

Fetch API

🔹 Backend

FastAPI

Python

Uvicorn

CORS Middleware

🔹 PDF Report

ReportLab (PDF generation)

🔹 Core Logic Modules

Resume Parser

Skill Extractor

Semantic Matcher

Weighted Scoring Engine

Rewrite Suggestion Engine

PDF Report Generator

📊 Features

Resume upload (PDF)

Job Description input

Semantic similarity score

Required vs Preferred skill scoring

Weighted final score breakdown

Color-coded animated progress bars

Resume rewrite suggestions

PDF report export

Decision recommendation system

📁 Project Structure
smart_resume_screener/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── resume_parser.py
│   │   ├── skill_extractor.py
│   │   ├── matcher.py
│   │   ├── scorer.py
│   │   ├── explainer.py
│   │   ├── rewrite.py
│   │   ├── report.py
│   │
│   └── requirements.txt
│
├── frontend/
│   └── resume-ui/
│       ├── src/
│       │   ├── App.jsx
│       │   ├── api.js
│       │   ├── index.css
│       │
│       └── package.json
⚙️ Installation Guide
1️⃣ Clone Repository
git clone (https://github.com/singhkalpana2523-hue/AI-RESUME-SCREENER)
cd ai-resume-screener

2️⃣ Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload


Backend runs on:

http://127.0.0.1:8000

3️⃣ Frontend Setup
cd frontend/resume-ui
npm install
npm run dev


Frontend runs on:

http://localhost:5173

🧮 Scoring Formula

Final Score =
(0.5 × Semantic Similarity) +
(0.35 × Required Skills Score) +
(0.15 × Preferred Skills Score)

Decision Logic:

75+ → Strongly Recommended

55–74 → Recommended

40–54 → Borderline

< 40 → Not Recommended

📄 PDF Report Contains

Final Score

Similarity Score

Decision

Matched Skills

Missing Required Skills

Resume Rewrite Suggestions

🎯 Use Cases

Students preparing for placements

Resume optimization before applying

Recruiters shortlisting candidates

ATS simulation for learning purposes

🔮 Future Improvements

Real LLM-based rewrite suggestions

Keyword heatmap visualization

Resume auto-enhancement

Cloud deployment (Render / Railway / AWS)

Authentication system

Database storage

👨‍💻 Author
KALPANA SINGH
Developed as a Full Stack AI Resume Analysis Project
Built using FastAPI + React
