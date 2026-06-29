# Use a lightweight Python base
FROM python:3.11-slim-bookworm

# Download the latest uv binary from the official Astral image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory
WORKDIR /app

# --- OPTION A: If you are using pyproject.toml and uv.lock ---
# Copy dependency files first (to cache the installation step)
COPY pyproject.toml uv.lock ./
# Install dependencies securely and cleanly
RUN uv sync --frozen --no-install-project --no-dev

# --- OPTION B: If you are just using a requirements.txt ---
# COPY requirements.txt ./
# RUN uv pip install --system -r requirements.txt

# Copy your actual application code (ml_artifacts, app, etc.)
COPY . .

# Start the FastAPI server using uv run, binding to Railway's $PORT
CMD sh -c "uv run uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"