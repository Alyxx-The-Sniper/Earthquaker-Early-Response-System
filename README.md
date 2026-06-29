# Earthquake Early Response Simulator

A production-grade Proof of Concept (PoC) system designed to predict structural building damage after seismic events.

This project uses a machine learning pipeline powered by **XGBoost** to process geotechnical, seismic, and structural building data. The goal is to help Local Government Units (LGUs) prioritize rescue, inspection, and emergency response efforts in near real-time after an earthquake.

Projects Reseach link: [meduim_post](https://medium.com/@kaikuh/earthquake-early-response-simulator-a337f7fbd4a8?postPublishedType=repub)

---

##  Features

### Dynamic Physics Engine

Calculates earthquake intensity values such as **Peak Ground Acceleration (PGA)** based on user-defined magnitude and epicenter coordinates.

### XGBoost Damage Classification

Uses a trained machine learning model to classify buildings into five structural damage levels:

* Class 0: No Damage
* Class 1: Light Damage
* Class 2: Moderate Damage
* Class 3: Severe Damage
* Class 4: Collapse

### Recall-Optimized Model

The model is tuned to prioritize recall for high-severity damage classes. This helps reduce the risk of classifying dangerous structures as safe.

### Interactive Dashboard

Includes a Leaflet-based map interface for visualizing predicted building damage and affected zones.

### FastAPI Backend

Provides API endpoints for real-time prediction requests.

---

##  Tech Stack

### Machine Learning

* XGBoost
* Scikit-learn
* Pandas
* Joblib

### Backend

* FastAPI
* Uvicorn
* Pydantic

### Frontend

* HTML
* Tailwind CSS
* JavaScript
* Leaflet.js

### Tooling and Deployment

* uv
* Docker
* Railway

---

##  Project Structure

```plaintext
EARTHQUAKE/
├── app/
│   ├── main.py              # FastAPI app and route definitions
│   ├── schemas.py           # Pydantic request and response validation
│   ├── model_service.py     # XGBoost model inference logic
│   └── index.html           # Frontend dashboard
│
├── ml_artifacts/
│   ├── model.joblib         # Serialized ML pipeline
│   └── metadata.json        # Model metadata and target mapping
│
├── Dockerfile               # Deployment configuration
├── pyproject.toml           # Project dependencies
├── uv.lock                  # Locked dependency versions
└── README.md
```

---

##  Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/Alyxx-The-Sniper/Earthquaker-Early-Response-System.git
cd Earthquaker-Early-Response-System
```

### 2. Install dependencies using uv

```bash
uv sync
```

### 3. Run the local development server

```bash
uv run uvicorn app.main:app --reload
```

### 4. Open the application

Visit:

```plaintext
http://127.0.0.1:8000
```

---

##  API Endpoints

### Home Page

```http
GET /
```

Returns the frontend dashboard.

### Prediction Endpoint

```http
POST /predict
```

Accepts building and seismic data, then returns the predicted structural damage class.

Example response:

```json
{
  "bldg_id": "ANT-001",
  "predicted_damage": "Class 2: Moderate Damage",
  "chosen_probability": 0.742,
  "all_probabilities": {
    "Class 0: No Damage": 0.031,
    "Class 1: Light Damage": 0.114,
    "Class 2: Moderate Damage": 0.742,
    "Class 3: Severe Damage": 0.086,
    "Class 4: Collapse": 0.027
  }
}
```

---

##  Methodology

Standard accuracy alone is not enough for disaster response systems. In this project, model evaluation focuses on reducing dangerous false negatives.

The model prioritizes:

* **Recall for high-severity classes**
  Reduces the chance of missing buildings that may have severe damage or collapse risk.

* **Macro-averaged F1-score**
  Measures balanced performance across all damage classes.

* **Class weighting**
  Helps the model pay more attention to severe and minority damage classes.

---

##  Important Limitation

This project is a prototype decision-support system. It does not replace certified structural inspections or official disaster assessment procedures.

A major limitation is the lack of publicly available building-level post-earthquake damage datasets for Philippine LGUs. Because of this, the model may rely on synthetic or simulation-based data to demonstrate the workflow.

The prediction output should be interpreted as an early response estimate, not a final engineering judgment.

---

##  Deployment

This project is configured for deployment on Railway.

The included `Dockerfile` uses `uv` for faster dependency installation and reproducible builds.

To deploy:

1. Push the project to GitHub.
2. Connect the repository to Railway.
3. Let Railway build and deploy the app automatically.

---

##  Purpose

This project was created for Disaster Risk Reduction and Management (DRRM) research.

Its purpose is to demonstrate how LGUs could combine seismic event data, building inventory, geotechnical features, and machine learning to support faster post-earthquake response and inspection prioritization.

---

## Author

Developed by Alexis Mandario.
