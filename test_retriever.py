from rag_engine import TfidfRetriever


retriever = TfidfRetriever()

queries = [
    "What datasets were used in RefraScan?",
    "What are the three refractive status classes?",
    "Why was ResNet50 selected as the final model?"
]

for query in queries:
    print("\n" + "=" * 70)
    print("QUERY:")
    print(query)
    print("=" * 70)

    results = retriever.retrieve(query, top_k=3)

    for i, result in enumerate(results, start=1):
        print(f"\n--- Result {i} ---")
        print(f"Similarity Score: {result['score']:.4f}")
        print(result["text"])