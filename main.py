from fastapi import FastAPI

# uvicorn main:app --host 127.0.0.1 --port 8000 --reload



# Initialiser FastAPI
description='Hello world'

app = FastAPI(title="Word counter",description=description)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/')
async def index():
    message = "This API counts the number of words in a text"
    return message  

@app.post("/count")
async def count(text):
    text = " ".join(text.strip().split('\t'))
    text = " ".join(text.strip().split('\n'))
    list_ = text.strip().split(' ')
    is_space = True
    while is_space:
        is_space = False 
        for elt in list_:
           if elt == '':
              list_.remove(elt)
              is_space = True
            
    return {"word_count":len(list_)} 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)