FROM python:3.11-slim-buster

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create necessary directories
RUN mkdir -p artifacts/training

# Copy the model file first
COPY artifacts/training/model.h5 artifacts/training/

# Copy the rest of the application
COPY . .

# Verify model file exists and is readable
RUN python -c "import h5py; h5py.File('artifacts/training/model.h5', 'r')"

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]