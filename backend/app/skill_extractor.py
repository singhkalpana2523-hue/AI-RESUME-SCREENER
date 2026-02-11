MASTER_SKILLS = [
    "Python", "Java", "SQL", "Javascript",
    "Machine Learning", "Deep Learning",
    "Statistics", "Probability",
    "Data Structures", "Algorithms",
    "NLP", "React", "Node",
    "PyTorch", "Keras", "Scikit-learn",
    "Data Analysis", "Data Modeling"
]

REQUIRED_HINTS = ["required", "must have", "mandatory"]
PREFERRED_HINTS = ["preferred", "nice to have", "plus", "good to have"]

def extract_resume_skills(text: str):
    text = text.lower()
    return list({
    skill for skill in MASTER_SKILLS
    if skill.lower() in text
})



def extract_jd_skills(text: str):
    text = text.lower()
    required = []
    preferred = []

    for skill in MASTER_SKILLS:
        if skill.lower() in text:
            # crude but effective heuristic
            if any(hint in text for hint in REQUIRED_HINTS):
                required.append(skill)
            else:
                preferred.append(skill)

    return list(set(required)), list(set(preferred))
