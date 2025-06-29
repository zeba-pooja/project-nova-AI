from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import random

app = Flask(__name__)

# 🔑 Use your real Gemini API key
genai.configure(api_key="AIzaSyDBSQuLwBOgggQ0S1P-fYBe_MzrlrbAxyI")
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    
    if "recommend" in user_input.lower():
        topics = {
            "movie": ["Inception", "La La Land", "Interstellar"],
            "book": ["Atomic Habits", "The Alchemist", "Ikigai"],
            "food": ["Pizza", "Biryani", "Sushi"]
        }
        for key in topics:
            if key in user_input.lower():
                return jsonify({"reply": f"You should try '{random.choice(topics[key])}'!"})
        return jsonify({"reply": "I recommend trying something new today!"})
    
    try:
        response = model.generate_content([user_input])
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Gemini Error: {e}"})

if __name__ == "__main__":
    app.run(debug=True)