from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pipelinelogic import simulate_pipeline
from models import PipelineResponse

app = FastAPI()  # 👈 This is the key line FastAPI needs

# CORS setup so frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/pipeline", response_model=PipelineResponse)
def get_pipeline():
    data = simulate_pipeline()
    return {"data": data}