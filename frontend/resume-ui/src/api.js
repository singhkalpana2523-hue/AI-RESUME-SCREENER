export const analyzeResume = async (resume, jobDescription) => {
  const formData = new FormData();
  formData.append("resume", resume);
  formData.append("job_description", jobDescription);

  const response = await fetch("http://127.0.0.1:8000/analyze", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    const errorText = await response.text();
    console.error("Backend error:", errorText);
    throw new Error("Backend error");
  }

  // ✅ IMPORTANT: return JSON
  return await response.json();
};
