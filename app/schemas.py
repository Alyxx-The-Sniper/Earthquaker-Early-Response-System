from pydantic import BaseModel, Field
from typing import Dict, Literal


# input data validation
class BuildingData(BaseModel):
    """
    Schema validating the incoming building data against the ML model metadata.
    Ensures the exact data types and bounds expected by the XGBoost pipeline.
    """
    # Identifiers (Will be logged but dropped before model inference)
    bldg_id: str
    latitude: float
    longitude: float
    
    # Numeric Expected Features
    year_built: int = Field(..., ge=1900, le=2026, description="Year of construction")
    floors: int = Field(..., ge=1, le=100, description="Total number of stories")
    vs30: int = Field(..., ge=100, le=1500, description="Soil shear-wave velocity (m/s)")
    magnitude: float = Field(..., ge=1.0, le=10.0, description="Event magnitude")
    dist_km: float = Field(..., ge=0.0, le=1000.0, description="Distance from epicenter")
    pga_g: float = Field(..., ge=0.0, le=3.0, description="Peak Ground Acceleration")
    pgv_cms: float = Field(..., ge=0.0, le=300.0, description="Peak Ground Velocity")
    
    # Categorical Expected Features
    barangay: Literal["Cupang","Dela Paz","San Luis","San Juan","San Isidro","Bagong Nayon","Mayamot","Dalig","Muntindilaw","Inarawan","San Jose","San Roque",]
    material: Literal['Steel','Concrete','Wood','Masonry_URM']
    occupancy: Literal['School','Industrial','Residential','Commercial','Hospital']

# output
class PredictionResponse(BaseModel):
    bldg_id: str
    predicted_damage: str
    chosen_probability: float
    all_probabilities: Dict[str, float]