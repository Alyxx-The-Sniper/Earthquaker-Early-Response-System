import os
from pathlib import Path

# Resolve base directories safely assuming execution from the ROOT/EARTHQUAKE folder
BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = BASE_DIR / "ml_artifacts"

# Paths to ML Artifacts
MODEL_PATH = ARTIFACTS_DIR / "pipeline_xgb_tuned_recall_threshold.pkl"
METADATA_PATH = ARTIFACTS_DIR / "metadata.json"

# Create directories if they don't exist to prevent path errors
# ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)