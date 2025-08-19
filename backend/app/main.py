from fastapi import FastAPI
from app.routes import rag_routes,user_routes

app = FastAPI()
app.include_router(user_routes.app, prefix="/user", tags=["user"])
app.include_router(rag_routes.app, prefix="/rag", tags=["rag"])


@app.get("/")
async def root():
    return {"message": "Hello World"}