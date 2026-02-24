from ollama import chat

response = chat(
    model="qwen3",
    messages=[{"role": "user", "content": "Explain local LLMs in one sentence."}],
)
print(response["message"]["content"])