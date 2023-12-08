from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from web_api import make_plan
from model.target import Target
from model.plan import Plan
from service.client import get_completion
from service.prompt import *

app = FastAPI();

mock_target = Target(
    goal="build a professional network",
    situation="at a conference",
    occupation="software engineer",
    relationship="stranger",
    activity="standing alone",

);

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://conversational-repertoire.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
);

app.include_router(make_plan.router);

@app.get("/")
def hello():
    return "Welcome to the backend!"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)