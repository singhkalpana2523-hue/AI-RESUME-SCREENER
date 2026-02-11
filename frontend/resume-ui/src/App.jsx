import { useState } from "react";
import { analyzeResume } from "./api";
import "./index.css";

function App() {
  const [resume, setResume] = useState(null);
  const [jd, setJd] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  // 🎨 Score Color Logic
  const getScoreColor = (value) => {
    if (value < 40) return "score-red";
    if (value < 70) return "score-yellow";
    return "score-green";
  };

  const handleSubmit = async () => {
    if (!resume || !jd) {
      alert("Please upload resume and paste job description");
      return;
    }

    setLoading(true);
    try {
      const data = await analyzeResume(resume, jd);
      setResult(data);
    } catch (err) {
      console.error("Analyze error:", err);
      alert("Error analyzing resume");
    }
    setLoading(false);
  };

  const downloadReport = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/download-report",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(result),
        }
      );

      if (!response.ok) throw new Error("Download failed");

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "resume_report.pdf";
      a.click();
    } catch (err) {
      alert("Failed to download report.");
      console.error(err);
    }
  };

  return (
    <div className="app-layout">
      {/* LEFT PANEL */}
      <div className="left-panel">
        <div className="card input-card">
          <h1 className="app-title">📄 AI Resume Screener</h1>

          <label className="label">Job Description</label>
          <textarea
            className="jd-textarea"
            placeholder="Paste Job Description here..."
            value={jd}
            onChange={(e) => setJd(e.target.value)}
          />

          <label className="label upload-label">
            Upload Resume (PDF)
          </label>
          <input
            type="file"
            accept=".pdf"
            onChange={(e) => setResume(e.target.files[0])}
          />

          <button
            className="analyze-btn"
            onClick={handleSubmit}
            disabled={loading}
          >
            {loading ? "Analyzing..." : "Analyze Resume"}
          </button>
        </div>
      </div>

      {/* RIGHT PANEL */}
      <div className="right-panel">
        {!result ? (
          <div className="empty-state">
            Upload resume & analyze to see results →
          </div>
        ) : (
          <div className="card result-card">
            <h2>📊 Result</h2>

            {/* SCORE BLOCK */}
            {["similarity", "skill_match", "final_score"].map(
              (key) => {
                const value = result[key] || 0;
                return (
                  <div className="score-row" key={key}>
                    <div className="score-header">
                      <span className="score-title">
                        {key.replace("_", " ").toUpperCase()}
                      </span>
                      <span
                        className={`score-badge ${getScoreColor(
                          value
                        )}`}
                      >
                        {value.toFixed(2)}%
                      </span>
                    </div>

                    <div className="progress-bar">
                      <div
                        className={`progress-fill ${getScoreColor(
                          value
                        )}`}
                        style={{ width: `${value}%` }}
                      ></div>
                    </div>
                  </div>
                );
              }
            )}

            {/* Explanation */}
            <p className="explanation">
              <b>Explanation:</b> {result.explanation}
            </p>

            {/* Resume Rewrite Suggestions */}
            <h3>📝 Resume Rewrite Suggestions</h3>

            {Array.isArray(result.resume_rewrite_suggestions) &&
              result.resume_rewrite_suggestions.map(
                (section, index) => (
                  <div key={index} className="rewrite-section">
                    <p className="rewrite-title">
                      {section.title}
                    </p>
                    <p>{section.description}</p>
                    <ul>
                      {section.skills.map((skill, i) => (
                        <li key={i}>{skill}</li>
                      ))}
                    </ul>
                  </div>
                )
              )}

            <button
              className="download-btn"
              onClick={downloadReport}
            >
              ⬇ Download Report
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
