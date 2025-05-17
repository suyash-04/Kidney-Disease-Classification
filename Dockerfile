
FROM python:3.11-slim-buster
WORKDIR /app
COPY . /app/

RUN  pip install --no-cache-dir -r requirements.txt

# Verify model file exists and is readable
RUN python -c "import h5py; h5py.File('artifacts/training/model.h5', 'r')"

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]