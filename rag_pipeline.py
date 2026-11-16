import ollama

from rag_engine import TfidfRetriever


MODEL_NAME = "llama3.2:3b"


def generate_answer(query, top_k=5):
    # Retrieve relevant information from the RefraScan knowledge base
    retriever = TfidfRetriever()
    results = retriever.retrieve(query, top_k=top_k)

    # Combine the retrieved chunks into context
    context = "\n\n".join(
        result["text"]
        for result in results
    )

    prompt = f"""
You are a thesis assistant for the RefraScan research project.

Answer the user's question using ONLY the information provided
in the context below.

If the answer is not found in the context, say:
"I could not find that information in the RefraScan knowledge base."

Do not invent or add unsupported information.

Context:
{context}

User question:
{query}

Answer:
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"], results