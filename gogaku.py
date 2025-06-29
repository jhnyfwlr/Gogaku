# This is the chatbot
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

print("API key loaded:", openai.api_key is not None)

def chat_with_gpt(prompt): 
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant specialized in teaching Japanese language. "
                       "Only answer questions about Japanese language and culture."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = openai.ChatCompletion.create(
        model = "gpt-4o",
        messages = messages
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__": 
    while True: 
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]: 
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
        