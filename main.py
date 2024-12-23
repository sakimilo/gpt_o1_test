import os
from openai import OpenAI

client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.chat.completions.create(
    model="o1-mini",
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "hihi"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "Hello! 😊 How can I help you today?"
            }
        ]
        }
    ]
)