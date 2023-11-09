from fastapi import FastAPI
from web_api import test_router

app = FastAPI();

app.include_router(test_router.router);

@app.get("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    import uvicorn;
    uvicorn.run("main:app", reload=True);
