from rag_pipeline import generate_answer


query = "What are the three refractive status classes?"

answer, results = generate_answer(query)

print("\nQUESTION:")
print(query)

print("\nRETRIEVED INFORMATION:")

for i, result in enumerate(results, start=1):
    print(f"\n--- Retrieved Chunk {i} ---")
    print(f"Similarity: {result['score']:.4f}")
    print(result["text"])

print("\n" + "=" * 70)
print("RAG ANSWER")
print("=" * 70)
print(answer)