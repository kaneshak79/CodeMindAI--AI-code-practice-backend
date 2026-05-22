# 🧠 CodeMindAI Backend

AI-powered coding assessment backend built using **FastAPI**, **Groq LLM**, and **MongoDB**.

It generates coding problems and evaluates user code using AI-based test simulation (LeetCode-style experience).

---

# 🚀 Features

- AI-powered coding question generation (Arrays, Strings, Linked List, etc.)
- AI-based code evaluation system
- Automatic test case generation using AI
- Pass / Fail analysis per test case
- AI explanation of code quality
- Stores questions and submissions in MongoDB
- REST API backend for frontend integration
- Lightweight and fast FastAPI service

---

# 🏗️ Tech Stack

FastAPI, Python 3.10+, Groq LLM (LLaMA 3.3 70B), MongoDB, python-dotenv

---

# 📁 Project Structure

backend/

│── main.py

│── .env

│── requirements.txt

│── README.md

---

# ⚙️ Setup Instructions

Clone repository:

```bash

git clone https://github.com/your-username/codemindai-backend.git

cd codemindai-backend

Create virtual environment:

python -m venv venv

Activate environment:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

Install dependencies:

pip install fastapi uvicorn pymongo groq python-dotenv

Create .env file:

GROQ_API_KEY=your_groq_api_key

MONGO_URI=your_mongodb_connection_string

Run server:

uvicorn main:app --reload

Server runs at:

http://127.0.0.1:8000

📡 API Endpoints

GET /

Health check endpoint.

Response:

{
  "message": "CodeMindAI Backend Running"
}

POST /generate-question

Generates a new coding problem.

Request:

{
  "topic": "Arrays",
  "difficulty": "Easy",
  "language": "Python"
}

Response:

{
  "question": "Generated coding problem..."
}

POST /evaluate

Evaluates user code using AI-based judge simulation.

Request:

{
  "question": "Problem statement",
  "code": "user code",
  "language": "Python"
}

Response:

{
  "evaluation": {
    "aiResponse": "Short explanation of evaluation",
    "results": [
      {
        "id": 1,
        "input": "[1,2,3]",
        "expected": "3",
        "output": "3",
        "status": "pass"
      },
      {
        "id": 2,
        "input": "[2,3,4]",
        "expected": "4",
        "output": "3",
        "status": "fail"
      }
    ],
    "summary": {
      "total": 2,
      "passed": 1,
      "failed": 1
    }
  }
}
GET /questions

Returns all stored AI-generated questions.

GET /submissions

Returns all user submissions with evaluation history.

🗄️ Database Schema

Questions Collection

{
  "topic": "Arrays",
  "difficulty": "Easy",
  "language": "Python",
  "question": "..."
}

Submissions Collection

{
  "question": "...",
  "language": "Python",
  "code": "...",
  "evaluation": {
    "aiResponse": "...",
    "results": [],
    "summary": {}
  }
}

🔥 Future Improvements

Real code execution system

Hidden test case support

User authentication system

Leaderboard system

Performance analytics dashboard

Code runtime execution

👨‍💻 Author

CodeMindAI Project

📜 License

This project is for educational purposes only.
