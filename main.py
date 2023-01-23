"""
tutorial
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """

    top level endpoint to test server
    """
    return {"message": "Hello World"}


def test(arr):
    """
    function to test pylint
    """
    for i in range(len(arr)):
        print(i)

    return 0
