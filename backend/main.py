from fastapi import FastAPI
from erp_assistant import get_erp_response

app = FastAPI()

@app.get("/generate/")
async def generate_text(query: str):
    return {"response": get_erp_response(query)}
