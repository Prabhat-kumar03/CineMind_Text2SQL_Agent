from fastapi import FastAPI,Form
from generate_response import generate_response
from fastapi.responses import JSONResponse
app = FastAPI()

@app.post("/get-answer")
def user_query_handler(query : str = Form(...)):
    try:
        answer = generate_response(query)
        return JSONResponse(status_code=200 , content={"answer" : answer})
    except Exception as e :
        print(e)
        return JSONResponse(status_code=500,content={"message":"Internal Server Error"})