# This is the chatbot
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

print("API key loaded:", openai.api_key is not None)

# Defining the chatbot's role and scope. 
def chatWithGPT(prompt): 
    messages = [
        {
            "role": "system",
            "content": ("You are a patient and friendly language tutor who helps English speakers learn Japanese. "
            "When responding, explain Japanese words, grammar, or phrases in English. "
            "Provide examples, and use furigana with kanji and kana where helpful. "
            "Avoid speaking only in Japanese unless specifically asked to.")
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
        userInput = input("You: ")
        if userInput.lower() in ["quit", "exit", "bye"]: 
            break

        response = chatWithGPT(userInput)
        print("Chatbot: ", response)
        
