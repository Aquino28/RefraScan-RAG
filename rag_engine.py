from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_knowledge_base(path="knowledge_base.txt"):
    """Load the knowledge base and create meaningful text chunks."""
    text = Path(path).read_text(encoding="utf-8")

    # Split by blank lines
    sections = [
        section.strip()
        for section in text.split("\n\n")
        if section.strip()
    ]

    chunks = []

    # Combine very short heading-only sections with the next section
    i = 0

    while i < len(sections):
        current = sections[i]

        # If the section is only a short heading, combine it
        # with the following section.
        if (
            len(current.split()) <= 8
            and i + 1 < len(sections)
        ):
            combined = current + "\n" + sections[i + 1]
            chunks.append(combined)
            i += 2
        else:
            chunks.append(current)
            i += 1

    return chunks


class TfidfRetriever:
    def __init__(self, knowledge_base_path="knowledge_base.txt"):
        self.chunks = load_knowledge_base(knowledge_base_path)

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2)
        )

        self.matrix = self.vectorizer.fit_transform(self.chunks)

    def retrieve(self, query, top_k=3):
        """Return the most relevant knowledge-base chunks."""

        # Add related terms to improve retrieval for common thesis questions.
        query_lower = query.lower()

        expanded_query = query

        if "dataset" in query_lower or "data" in query_lower:
            expanded_query += " PAPILA AUFMC data sources"

        if "class" in query_lower or "refractive status" in query_lower:
            expanded_query += " myopia hyperopia emmetropia"

        if "final model" in query_lower or "selected" in query_lower:
            expanded_query += " ResNet50 Macro F1 Balanced Accuracy"

        query_vector = self.vectorizer.transform([expanded_query])

        similarities = cosine_similarity(
            query_vector,
            self.matrix
        ).flatten()

        top_indices = similarities.argsort()[::-1][:top_k]

        results = []

        for index in top_indices:
            results.append({
                "text": self.chunks[index],
                "score": float(similarities[index])
            })

        return results