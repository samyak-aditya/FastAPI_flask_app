from fastapi import FastAPI
from app.routes import router as user_router

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    print("Connecting to MongoDB...")

@app.on_event("shutdown")
async def shutdown_db_client():
    print("Disconnecting from MongoDB...")

app.include_router(user_router, prefix="/api/users")
