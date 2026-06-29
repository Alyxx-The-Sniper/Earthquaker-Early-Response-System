Earthquake Early Response Simulator
A production-grade Proof of Concept (PoC) system designed to predict structural building damage following seismic events. This project leverages a machine learning pipeline (XGBoost) to process geotechnical and structural data, allowing local government units (LGUs) to prioritize rescue and inspection efforts in real-time.

🚀 Features
Dynamic Physics Engine: Real-time calculation of earthquake intensity (PGA) based on user-defined Magnitude and Epicenter coordinates.

XGBoost Inference: A high-performance machine learning model trained to classify building vulnerability into 5 levels of structural damage.

Recall-Optimized: The model is weighted to prioritize Recall for high-severity classes, ensuring structures at risk of collapse are never misclassified as "safe."

Interactive Dashboard: A clean, leaflet-based map visualization for immediate field operations support.

🛠 Tech Stack
ML Pipeline: XGBoost, Scikit-Learn, Pandas

Backend: FastAPI (High-performance ASGI server)

Frontend: HTML

Tooling: uv (Fast dependency management)

📁 Project Structure
Plaintext
EARTHQUAKE/
├── app/
│   ├── main.py            # API Traffic Director
│   ├── schemas.py         # Pydantic data validation
│   ├── model_service.py   # XGBoost inference logic
│   └── index.html         # Frontend Dashboard
├── ml_artifacts/          # Serialized models & metadata
└── Dockerfile             # Deployment configuration
⚙️ Setup & Installation
Clone the repository:

Bash
git clone https://github.com/Alyxx-The-Sniper/Earthquaker-Early-Response-System.git
cd EARTHQUAKE
Install dependencies using uv:

Bash
uv sync
Run the local development server:

Bash
uv run uvicorn app.main:app --reload
🌐 Deployment
This project is configured for seamless deployment on Railway.

The Dockerfile is optimized to use uv for minimal build times.

Simply connect your GitHub repository to Railway, and the platform will automatically detect the build steps.

📈 Methodology
Standard accuracy metrics are insufficient for disaster response. Our model evaluates performance based on:

Recall for High-Severity Classes: Minimizing False Negatives in "Collapse" scenarios.

Macro-Averaged F1-Score: Ensuring uniform reliability across all five damage levels.

Class Weight Tuned prioritizing ordered target class category

Created for Disaster Risk Reduction and Management (DRRM) research.