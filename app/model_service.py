import json
import pandas as pd
import joblib
from app.config import MODEL_PATH, METADATA_PATH
from app.schemas import BuildingData

class ModelService:
    def __init__(self):
        # load the model
        self.model = joblib.load(MODEL_PATH)

        # load meta data
        with open(METADATA_PATH, 'r') as f:
            self.metadata = json.load(f)

        # target map int to str from metadata   
        self.target_mapping = self.metadata['target_mapping']

  
    def predict(self, inputdata: BuildingData) -> dict:
        """ Takes in raw Pydantic data, handles parsing, and returns prediction details """
        
        data_dict = inputdata.model_dump()
        bldg_id = data_dict['bldg_id']
        
        # note: this predict method should only take features that our model was trained on
        # Strip out the identifiers before passing to the ML model!
        # XGBoost expects exactly the features it was trained on.
        ml_features = {k: v for k, v in data_dict.items() if k not in ['bldg_id', 'latitude', 'longitude']}
        
        # Convert to a DataFrame 
        df = pd.DataFrame([ml_features])
        
        # Predict the chosen class and the raw probabilities
        prediction_int = self.model.predict(df)[0]
        probabilities = self.model.predict_proba(df)[0]
        
        # Map output integer to human-readable strings
        predicted_damage_str = self.target_mapping.get(str(prediction_int), "Unknown")
        chosen_probability = round(float(probabilities[prediction_int]), 3)
        
        # Create a dictionary mapping all classes to their probabilities
        all_probs = {
            self.target_mapping[str(i)]: round(float(prob), 3)
            for i, prob in enumerate(probabilities)
        }

        return {
            "bldg_id": bldg_id, 
            "predicted_damage": predicted_damage_str,
            "chosen_probability": chosen_probability,
            "all_probabilities": all_probs
        }