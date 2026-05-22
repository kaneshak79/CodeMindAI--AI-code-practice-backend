🧠 CodeMindAI Backend

AI-powered coding assessment platform backend built with FastAPI, Groq LLM, and MongoDB.
It generates coding problems and evaluates user solutions with AI-based test simulation.

🚀 Features
🧾 AI-powered coding question generation (LeetCode-style)
🤖 AI-based code evaluation
🧪 Automatic test case generation (AI simulated)
📊 Pass/Fail analysis of solutions
💾 Stores questions and submissions in MongoDB
🌐 REST API ready for frontend integration
⚡ FastAPI high-performance backend
🏗️ Tech Stack
Backend Framework: FastAPI
AI Model: Groq (LLaMA 3.3 70B)
Database: MongoDB
Language: Python 3.10+
Environment Manager: python-dotenv
📁 Project Structure
backend/
│── main.py
│── .env
│── requirements.txt
│── README.md
⚙️ Setup Instructions
1. Clone Repository
git clone https://github.com/your-username/codemindai-backend.git
cd codemindai-backend
2. Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3. Install Dependencies
pip install fastapi uvicorn pymongo groq python-dotenv
4. Setup Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key
MONGO_URI=your_mongodb_connection_string
5. Run Server
uvicorn main:app --reload

Server runs at:

http://127.0.0.1:8000
📡 API Endpoints
🏠 Health Check
GET /

Response

{
  "message": "CodeMindAI Backend Running"
}
🧠 Generate Coding Question
POST /generate-question

Request Body

{
  "topic": "Arrays",
  "difficulty": "Easy",
  "language": "Python"
}

Response

{
  "question": "Generated coding problem..."
}
🧪 Evaluate Code
POST /evaluate

Request Body

{
  "question": "...",
  "code": "...",
  "language": "Python"
}

Response

{
  "evaluation": {
    "aiResponse": "Explanation of performance",
    "results": [
      {
        "id": 1,
        "input": "[1,2,3]",
        "expected": "3",
        "output": "3",
        "status": "pass"
      }
    ],
    "summary": {
      "total": 3,
      "passed": 2,
      "failed": 1
    }
  }
}
📚 Get All Questions
GET /questions
📦 Get All Submissions
GET /submissions
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
  "evaluation": {}
}
⚠️ Important Notes
AI is used for simulation of test cases, not real code execution
Results are AI-generated (not deterministic like real judge systems)
For production-grade judging, integrate:
Judge0 API OR
Docker-based execution engine
🔥 Future Improvements
Real code execution engine (LeetCode-style judge)
Hidden test cases support
Authentication system
Leaderboard system
User submission history dashboard
👨‍💻 Author

Built by CodeMindAI Project

📜 License

This project is for educational purposes.
