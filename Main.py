from fastapi import FastAPI
from admin_api_routes import router as admin_router

app = FastAPI()
app.include_router(admin_router)
