FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get -y install \
    build-essential \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code into the container
COPY puzzle_solver_api ./puzzle_solver_api
COPY puzzle_solver_core ./puzzle_solver_core

# Make sure Python can find both backend/ and core/
ENV PYTHONPATH=/app

# Move into backend/ to run FastAPI entry point (main.py)
WORKDIR /app/puzzle_solver_api

# Cloud Run requires the app to listen on port 8080
ENV PORT=8080

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]