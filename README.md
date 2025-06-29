📘 NOVA - AI Assistant Agent (Internship Project)
----------------------------------------------
🎓 Student: Zeba Nargis T. M.  
📂 Project: Personal AI Assistant using Flask + Gemini AI  
📅 Submission Date: [30-6-2025]

----------------------------------------------
📄 PROJECT OVERVIEW
----------------------------------------------
"Nova" is a smart *AI-powered assistant* built using *Flask (Python)* and *Google Gemini AI*. It allows users to ask anything via a web interface and get intelligent answers or recommendations in real-time.

This is my internship project that demonstrates:
- Flask web development
- REST API integration with Gemini
- Basic AI interaction
- Clean frontend design using HTML + CSS

---

🧱 PROJECT STRUCTURE (FOLDER LAYOUT)
----------------------------------------------
Nova-AI-Project/
├── Website.py               👉 Flask backend & Gemini integration  
├── requirements.txt         👉 List of required Python packages  
│  
├── templates/
│   └── index.html           👉 User interface (HTML form + JS for fetch)  
│  
├── static/
│   └── style.css            👉 UI styling (modern, centered box, colors)  
│  
└── README.txt               👉 This description file

---

⚙ FILES EXPLAINED
----------------------------------------------

📌 Website.py  
> Main Python file. It:
- Creates the Flask app
- Configures Gemini API
- Handles routes / (frontend) and /ask (API)
- Includes recommendation logic (movies, books, food)

📌 index.html  
> Basic UI for the assistant where users type their questions. Uses:
- Input box + Ask button
- JavaScript fetch call to Flask /ask route
- Dynamic response update in the page

📌 style.css  
> Beautifies the page using:
- Center alignment
- Colorful buttons
- Rounded box & spacing
- Clean and modern layout

📌 requirements.txt  
> Required Python libraries:
> flask google-generativeai
> Install with:
- pip install -r requirements.txt

---

💡 FEATURES
----------------------------------------------
✔ Gemini AI integration  
✔ Smart Recommendations (books, movies, food)  
✔ Clean, centered UI  
✔ Interactive experience  
✔ Error-handling for API issues  
✔ Simple and lightweight project

---

🧪 HOW TO RUN
----------------------------------------------
1. Install Python 3  
2. Go to your project folder in terminal  
3. Install dependencies:
   pip install -r requirements.txt
4. Run the app
5. Open in browser:
   http://127.0.0.1:5000
   ---

📝 LEARNING OUTCOME
----------------------------------------------
✅ Learned Flask web app structure  
✅ Used REST API with Gemini AI  
✅ Designed front-end using HTML/CSS  
✅ Gained hands-on API, error handling, user interaction  
✅ Built a complete working AI assistant from scratch

---

🎯 FUTURE IDEAS
----------------------------------------------
- Add voice recognition  
- Enable dark mode toggle  
- Add memory / chat history  
- Save user preferences  

---

👩‍💻 SUBMITTED BY
----------------------------------------------
Zeba Nargis T. M  
B.Tech CSE  

