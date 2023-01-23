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
    
def test():
    """
    function to test pylint
    """
    pass
