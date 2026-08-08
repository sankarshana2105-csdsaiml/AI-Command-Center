import ollama

from app.config.settings import AI_MODEL


def generate_response(prompt: str) -> str:
    response = ollama.chat(
        model=AI_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]