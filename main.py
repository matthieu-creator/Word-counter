from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# uvicorn main:app --host 127.0.0.1 --port 8000 --reload




app = FastAPI(
    title="Word Counter",
    description="API that counts the number of words in a given text"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model
class TextInput(BaseModel):
    text: str

@app.get("/")
async def index():
    return {"message": "This API counts the number of words in a text"}

@app.post("/count")
async def count_words(input: TextInput):
    words = input.text.split()
    return {"word_count": len(words)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
