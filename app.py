# This is the backend for the app
from flask import Flask, request, jsonify, render_template
import openai
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from your frontend

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

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
            "content": user_message
        }
    ]

    try:
        response = openai.ChatCompletion.create(
            model = "gpt-4o",
            messages = messages
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
