from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

from app.schemas import BuildingData, PredictionResponse
from app.model_service import ModelService

app = FastAPI(title="Earthquake Response API")
model_service = ModelService()
current_dir = Path(__file__).resolve().parent

@app.post("/predict", response_model=PredictionResponse)
async def get_prediction(building: BuildingData):
    # Now passing the Pydantic object directly to match your new model_service
    result = model_service.predict(building)
    
    # FastAPI automatically converts this dict into the PredictionResponse schema
    return result

@app.get("/")
async def root():
    return FileResponse(current_dir / "index.html")



### Deploying to railway using dockerfile ##
import os

if __name__ == "__main__":
    import uvicorn
    # Railway assigns a dynamic PORT. Fallback to 8000 for local testing.
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)