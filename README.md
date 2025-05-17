# Kidney Disease Classification

A deep learning-based system for classifying kidney disease from medical images using TensorFlow and Flask.

## Overview

This project implements a CNN-based classifier for kidney disease detection from medical images. It uses transfer learning with pre-trained models and provides both training and prediction capabilities through a web interface.

## Features

- Deep learning model for kidney disease classification
- Web interface for easy interaction
- Training pipeline with MLflow integration
- DVC for data version control
- Docker support for containerization
- REST API endpoints for predictions

## Technical Stack

- **Deep Learning**: TensorFlow 2.12.0
- **Web Framework**: Flask
- **Data Version Control**: DVC
- **Experiment Tracking**: MLflow
- **Containerization**: Docker
- **Additional Libraries**: 
  - pandas, numpy for data manipulation
  - matplotlib, seaborn for visualization
  - scipy for scientific computing
  - joblib for model persistence

## Project Structure

```
Kidney-Disease-Classification/
├── artifacts/          # Model artifacts and saved models
├── config/            # Configuration files
├── logs/              # Training and application logs
├── research/          # Research notebooks and experiments
├── src/               # Source code
├── templates/         # Flask HTML templates
├── app.py            # Flask application
├── main.py           # Training pipeline
├── params.yaml       # Model parameters
├── requirements.txt  # Project dependencies
└── Dockerfile        # Docker configuration
```

## Setup and Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Kidney-Disease-Classification
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up DVC (if using data version control):
```bash
dvc pull
```

## Usage

### Training the Model

1. Start the training process:
```bash
python main.py
```

Or use the web interface:
- Navigate to `http://localhost:5000/train`

### Making Predictions

1. Start the Flask application:
```bash
python app.py
```

2. Access the web interface:
- Open `http://localhost:5000` in your browser
- Upload an image for prediction

### API Endpoints

- `GET /`: Home page
- `GET /predict`: Prediction page
- `POST /predict`: Submit image for prediction
- `GET/POST /train`: Trigger model training

## Model Parameters

The model can be configured through `params.yaml`:
- EPOCHS: 20
- IMAGE_SIZE: [299, 299, 3]
- BATCH_SIZE: 10
- LEARNING_RATE: 0.01
- CLASSES: 2

## Docker Support

Build and run the Docker container:
```bash
docker build -t kidney-disease-classifier .
docker run -p 5000:5000 kidney-disease-classifier
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the terms of the license included in the repository.

## Acknowledgments

- TensorFlow team for the deep learning framework
- Flask team for the web framework
- All contributors and maintainers