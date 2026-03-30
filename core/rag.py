from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SimpleRAG:
    def __init__(self, documents):
        self.documents = [doc for doc in documents.split("\n") if doc.strip()]
        self.vectorizer = TfidfVectorizer()
        self.vectors = self.vectorizer.fit_transform(self.documents)

    def retrieve(self, query, top_k=3):
        if not self.documents:
            return ""

        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.vectors).flatten()

        top_indices = similarities.argsort()[-top_k:][::-1]

        results = [self.documents[i] for i in top_indices]
        return "\n".join(results)
