from fastapi import FastAPI
from app.server.routes.routes import router


app = FastAPI(title="FastAPI + MongoDB", )
app.include_router(router, prefix="/student", tags=["Student"])

@app.get("/", tags=['Root'])
async def root():
    return {"Message" : "FastAPI and MongoDB Application"}

