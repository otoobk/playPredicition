from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from models import PlayerXY

# Create App instance
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to allow specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (HTML/CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

db = []

# Create route for GET request
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/data")
async def fetch_data():
    return db

@app.post("/api/data")
async def submit_data(request_data: PlayerXY):
    data = request_data.data
    db.append(data)
    return {"message": "Data recieved"}