# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from groq import Groq
# from pymongo import MongoClient
# from dotenv import load_dotenv
# import os

# # Load env
# load_dotenv()

# # Groq Client
# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY")
# )

# # MongoDB
# mongo_client = MongoClient(
#     os.getenv("MONGO_URI")
# )

# db = mongo_client["codeevalai"]

# submissions = db["submissions"]

# # FastAPI app
# app = FastAPI()

# # CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Request Model
# class CodeRequest(BaseModel):
#     question: str
#     code: str
#     language: str

# # Home Route

# # @app.get("/")
# # def home():
# #     return {
# #         "message": "CodeEvalAI Backend Running"
# #     }

# # # AI Evaluation Route
# # @app.post("/evaluate")
# # async def evaluate_code(data: CodeRequest):

# #     try:

# #         prompt = f"""
# #         You are an AI coding evaluator.

# #         Analyze this coding solution.

# #         Question:
# #         {data.question}

# #         Language:
# #         {data.language}

# #         Code:
# #         {data.code}

# #         Give:
# #         1. Code Quality Score out of 100
# #         2. Time Complexity
# #         3. Space Complexity
# #         4. Bugs
# #         5. Optimization Suggestions
# #         6. Strengths
# #         7. Final Feedback
# #         """

# #         completion = client.chat.completions.create(
# #             model="llama-3.3-70b-versatile",
# #             messages=[
# #                 {
# #                     "role": "user",
# #                     "content": prompt
# #                 }
# #             ],
# #             temperature=0.5,
# #             max_tokens=1024
# #         )

# #         result = completion.choices[0].message.content

# #         # Store in MongoDB
# #         submissions.insert_one({
# #             "question": data.question,
# #             "language": data.language,
# #             "code": data.code,
# #             "result": result
# #         })

# #         return {
# #             "evaluation": result
# #         }

# #     except Exception as e:

# #         return {
# #             "error": str(e)
# #         }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# ==============================
# LOAD ENV VARIABLES
# ==============================

load_dotenv()

# ==============================
# GROQ CLIENT
# ==============================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ==============================
# MONGODB CONNECTION
# ==============================

mongo_client = MongoClient(
    os.getenv("MONGO_URI")
)

db = mongo_client["codeevalai"]

submissions = db["submissions"]

questions_collection = db["questions"]

# ==============================
# FASTAPI APP
# ==============================

app = FastAPI()

# ==============================
# CORS
# ==============================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# REQUEST MODELS
# ==============================

class CodeRequest(BaseModel):
    question: str
    code: str
    language: str


class QuestionRequest(BaseModel):
    topic: str
    difficulty: str
    language: str

# ==============================
# HOME ROUTE
# ==============================

@app.get("/")
def home():

    return {
        "message": "CodeEvalAI Backend Running"
    }

# ==============================
# AI QUESTION GENERATION
# ==============================

@app.post("/generate-question")
async def generate_question(data: QuestionRequest):

    try:

        prompt = f"""
        Generate a HackerRank-style coding question.

        Topic: {data.topic}
        Difficulty: {data.difficulty}
        Programming Language: {data.language}

        Generate:

        1. Title
        2. Problem Statement
        3. Constraints
        4. Input Format
        5. Output Format
        6. Sample Input
        7. Sample Output
        8. Example Explanation
        9. Edge Cases
        """

        completion = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7,

            max_tokens=1200
        )

        generated_question = completion.choices[0].message.content

        # STORE QUESTION IN MONGODB

        questions_collection.insert_one({

            "topic": data.topic,
            "difficulty": data.difficulty,
            "language": data.language,
            "question": generated_question

        })

        return {

            "question": generated_question

        }

    except Exception as e:

        return {

            "error": str(e)

        }

# ==============================
# AI CODE EVALUATION
# ==============================

@app.post("/evaluate")
async def evaluate_code(data: CodeRequest):

    try:

        prompt = f"""
        You are an expert AI coding evaluator.

        Analyze this coding solution.

        Coding Question:
        {data.question}

        Programming Language:
        {data.language}

        User Code:
        {data.code}

        Give detailed analysis in markdown format.

        Include:

        1. Code Quality Score out of 100
        2. Time Complexity
        3. Space Complexity
        4. Bugs or Issues
        5. Optimization Suggestions
        6. Strengths
        7. Edge Case Analysis
        8. Final Feedback
        """

        completion = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.5,

            max_tokens=1200
        )

        result = completion.choices[0].message.content

        # STORE SUBMISSION

        submissions.insert_one({

            "question": data.question,
            "language": data.language,
            "code": data.code,
            "evaluation": result

        })

        return {

            "evaluation": result

        }

    except Exception as e:

        return {

            "error": str(e)

        }

# ==============================
# FETCH STORED QUESTIONS
# ==============================

@app.get("/questions")
def get_questions():

    try:

        questions = []

        all_questions = questions_collection.find()

        for q in all_questions:

            questions.append({

                "id": str(q["_id"]),
                "topic": q["topic"],
                "difficulty": q["difficulty"],
                "language": q["language"],
                "question": q["question"]

            })

        return {

            "questions": questions

        }

    except Exception as e:

        return {

            "error": str(e)

        }

# ==============================
# FETCH SUBMISSIONS
# ==============================

@app.get("/submissions")
def get_submissions():

    try:

        results = []

        all_submissions = submissions.find()

        for s in all_submissions:

            results.append({

                "id": str(s["_id"]),
                "question": s["question"],
                "language": s["language"],
                "code": s["code"],
                "evaluation": s["evaluation"]

            })

        return {

            "submissions": results

        }

    except Exception as e:

        return {

            "error": str(e)

        }