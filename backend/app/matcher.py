from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(resume_text: str, jd_text: str) -> float:
    embeddings = model.encode([resume_text, jd_text])
    emb1 = embeddings[0].reshape(1, -1)
    emb2 = embeddings[1].reshape(1, -1)

    similarity = cosine_similarity(emb1, emb2)[0][0]
    return round(float(similarity) * 100, 2)

