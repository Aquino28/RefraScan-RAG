import ollama


response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "In one short sentence, what is RefraScan?"
        }
    ]
)

print("\nOLLAMA RESPONSE:")
print(response["message"]["content"])