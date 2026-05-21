# # from fastapi import FastAPI
# # from fastapi.middleware.cors import CORSMiddleware
# # from pydantic import BaseModel
# # from groq import Groq
# # from pymongo import MongoClient
# # from dotenv import load_dotenv
# # import os

# # # Load env
# # load_dotenv()

# # # Groq Client
# # client = Groq(
# #     api_key=os.getenv("GROQ_API_KEY")
# # )

# # # MongoDB
# # mongo_client = MongoClient(
# #     os.getenv("MONGO_URI")
# # )

# # db = mongo_client["codeevalai"]

# # submissions = db["submissions"]

# # # FastAPI app
# # app = FastAPI()

# # # CORS
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # # Request Model
# # class CodeRequest(BaseModel):
# #     question: str
# #     code: str
# #     language: str

# # # Home Route

# # # @app.get("/")
# # # def home():
# # #     return {
# # #         "message": "CodeEvalAI Backend Running"
# # #     }

# # # # AI Evaluation Route
# # # @app.post("/evaluate")
# # # async def evaluate_code(data: CodeRequest):

# # #     try:

# # #         prompt = f"""
# # #         You are an AI coding evaluator.

# # #         Analyze this coding solution.

# # #         Question:
# # #         {data.question}

# # #         Language:
# # #         {data.language}

# # #         Code:
# # #         {data.code}

# # #         Give:
# # #         1. Code Quality Score out of 100
# # #         2. Time Complexity
# # #         3. Space Complexity
# # #         4. Bugs
# # #         5. Optimization Suggestions
# # #         6. Strengths
# # #         7. Final Feedback
# # #         """

# # #         completion = client.chat.completions.create(
# # #             model="llama-3.3-70b-versatile",
# # #             messages=[
# # #                 {
# # #                     "role": "user",
# # #                     "content": prompt
# # #                 }
# # #             ],
# # #             temperature=0.5,
# # #             max_tokens=1024
# # #         )

# # #         result = completion.choices[0].message.content

# # #         # Store in MongoDB
# # #         submissions.insert_one({
# # #             "question": data.question,
# # #             "language": data.language,
# # #             "code": data.code,
# # #             "result": result
# # #         })

# # #         return {
# # #             "evaluation": result
# # #         }

# # #     except Exception as e:

# # #         return {
# # #             "error": str(e)
# # #         }

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from groq import Groq
# from pymongo import MongoClient
# from dotenv import load_dotenv
# import os

# # ==============================
# # LOAD ENV VARIABLES
# # ==============================

# load_dotenv()

# # ==============================
# # GROQ CLIENT
# # ==============================

# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY")
# )

# # ==============================
# # MONGODB CONNECTION
# # ==============================

# mongo_client = MongoClient(
#     os.getenv("MONGO_URI")
# )

# db = mongo_client["codeevalai"]

# submissions = db["submissions"]

# questions_collection = db["questions"]

# # ==============================
# # FASTAPI APP
# # ==============================

# app = FastAPI()

# # ==============================
# # CORS
# # ==============================

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ==============================
# # REQUEST MODELS
# # ==============================

# class CodeRequest(BaseModel):
#     question: str
#     code: str
#     language: str


# class QuestionRequest(BaseModel):
#     topic: str
#     difficulty: str
#     language: str

# # ==============================
# # HOME ROUTE
# # ==============================

# @app.get("/")
# def home():

#     return {
#         "message": "CodeEvalAI Backend Running"
#     }

# # ==============================
# # AI QUESTION GENERATION
# # ==============================

# @app.post("/generate-question")
# async def generate_question(data: QuestionRequest):

#     try:

#         prompt = f"""
#         Generate a HackerRank-style coding question.

#         Topic: {data.topic}
#         Difficulty: {data.difficulty}
#         Programming Language: {data.language}

#         Generate:

#         1. Title
#         2. Problem Statement
#         3. Constraints
#         4. Input Format
#         5. Output Format
#         6. Sample Input
#         7. Sample Output
#         8. Example Explanation
#         9. Edge Cases
#         """

#         completion = client.chat.completions.create(

#             model="llama-3.3-70b-versatile",

#             messages=[
#                 {
#                     "role": "user",
#                     "content": prompt
#                 }
#             ],

#             temperature=0.7,

#             max_tokens=1200
#         )

#         generated_question = completion.choices[0].message.content

#         # STORE QUESTION IN MONGODB

#         questions_collection.insert_one({

#             "topic": data.topic,
#             "difficulty": data.difficulty,
#             "language": data.language,
#             "question": generated_question

#         })

#         return {

#             "question": generated_question

#         }

#     except Exception as e:

#         return {

#             "error": str(e)

#         }

# # ==============================
# # AI CODE EVALUATION
# # ==============================

# @app.post("/evaluate")
# async def evaluate_code(data: CodeRequest):

#     try:

#         prompt = f"""
#         You are an expert AI coding evaluator.

#         Analyze this coding solution.

#         Coding Question:
#         {data.question}

#         Programming Language:
#         {data.language}

#         User Code:
#         {data.code}

#         Give detailed analysis in markdown format.

#         Include:

#         1. Code Quality Score out of 100
#         2. Time Complexity
#         3. Space Complexity
#         4. Bugs or Issues
#         5. Optimization Suggestions
#         6. Strengths
#         7. Edge Case Analysis
#         8. Final Feedback
#         """

# #         prompt = f"""
# # You are an expert coding platform question generator like LeetCode and HackerRank.

# # Generate ONE completely UNIQUE coding problem.

# # Requirements:
# # - Topic: {data.topic}
# # - Difficulty: {data.difficulty}
# # - Programming Language: {data.language}

# # IMPORTANT:
# # - NEVER repeat previous questions
# # - Create a fresh new problem every time
# # - Avoid common examples like simple string reverse repeatedly
# # - Use different scenarios, constraints, and examples
# # - Question must feel like real coding assessment platforms
# # - Include:
# #   1. Title
# #   2. Problem Statement
# #   3. Input Format
# #   4. Output Format
# #   5. Constraints
# #   6. Example Input
# #   7. Example Output
# #   8. Explanation

# # Make the question professional and interview-level.
# # """

#         completion = client.chat.completions.create(

#             model="llama-3.3-70b-versatile",

#             messages=[
#                 {
#                     "role": "user",
#                     "content": prompt
#                 }
#             ],

#             temperature=0.5,

#             max_tokens=1200
#         )

#         result = completion.choices[0].message.content

#         # STORE SUBMISSION

#         submissions.insert_one({

#             "question": data.question,
#             "language": data.language,
#             "code": data.code,
#             "evaluation": result

#         })

#         return {

#             "evaluation": result

#         }

#     except Exception as e:

#         return {

#             "error": str(e)

#         }

# # ==============================
# # FETCH STORED QUESTIONS
# # ==============================

# @app.get("/questions")
# def get_questions():

#     try:

#         questions = []

#         all_questions = questions_collection.find()

#         for q in all_questions:

#             questions.append({

#                 "id": str(q["_id"]),
#                 "topic": q["topic"],
#                 "difficulty": q["difficulty"],
#                 "language": q["language"],
#                 "question": q["question"]

#             })

#         return {

#             "questions": questions

#         }

#     except Exception as e:

#         return {

#             "error": str(e)

#         }

# # ==============================
# # FETCH SUBMISSIONS
# # ==============================

# @app.get("/submissions")
# def get_submissions():

#     try:

#         results = []

#         all_submissions = submissions.find()

#         for s in all_submissions:

#             results.append({

#                 "id": str(s["_id"]),
#                 "question": s["question"],
#                 "language": s["language"],
#                 "code": s["code"],
#                 "evaluation": s["evaluation"]

#             })

#         return {

#             "submissions": results

#         }

#     except Exception as e:

#         return {

#             "error": str(e)

#         }

# first commit crt code

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import random

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

db = mongo_client["codemindai"]

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
        "message": "CodeMindAI Backend Running"
    }

# ==============================
# AI QUESTION GENERATION
# ==============================

@app.post("/generate-question")
async def generate_question(data: QuestionRequest):

    try:

        random_number = random.randint(1, 100000)

        prompt = f"""
You are an expert coding assessment platform like LeetCode and HackerRank.

Generate ONE completely UNIQUE coding problem.

IMPORTANT RULES:
- NEVER repeat previous problems
- DO NOT generate simple reverse string repeatedly
- Create a fresh new coding problem every time
- Problem must feel realistic and interview-level
- Topic: {data.topic}
- Difficulty: {data.difficulty}
- Language: {data.language}
- Random Seed: {random_number}

STRICTLY FOLLOW:

1. Give ONLY the problem statement
2. DO NOT provide solution code
3. DO NOT provide answer
4. DO NOT explain full logic
5. DO NOT provide completed implementation
6. DO NOT provide hidden hints
7. Keep it professional

FORMAT:

# Title

## Problem Statement

## Input Format

## Output Format

## Constraints

## Example Input

## Example Output

## Explanation

## Edge Cases
"""

        completion = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=1,

            max_tokens=1200
        )

        generated_question = completion.choices[0].message.content

        # STORE QUESTION

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
You are an expert AI coding evaluator like LeetCode / HackerRank judge.

Analyze the submitted solution AND simulate test execution.

Coding Question:
{data.question}

Programming Language:
{data.language}

User Submitted Code:
{data.code}

---

STRICT INSTRUCTIONS:

1. First, evaluate the solution quality.
2. Then generate 3 to 5 relevant test cases based on the problem.
3. For each test case, simulate execution mentally and decide output.
4. Mark each test as PASS or FAIL based on correctness.

---

OUTPUT FORMAT (VERY IMPORTANT):

# Code Quality Score
(0–10 score)

# Time Complexity

# Space Complexity

# Bugs / Issues

# Optimization Suggestions

# Test Cases Evaluation

For each test case:

- Input: ...
- Expected Output: ...
- Actual Output (from user's code): ...
- Status: pass/fail

# Final Feedback

Give short final verdict.

---

RULES:
- DO NOT give full corrected code
- DO NOT solve the problem fully
- MUST include test cases section
- MUST include pass/fail evaluation
- MUST simulate user code logically (do not execute)

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
