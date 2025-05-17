# 🏥 Kidney Disease Classification

A deep learning-based system for classifying kidney disease from medical images using TensorFlow and Flask. This project aims to assist medical professionals in the early detection and diagnosis of kidney diseases through automated image analysis.

## 📋 Overview

Kidney disease is a significant global health concern, and early detection is crucial for effective treatment. This project addresses this challenge by implementing an advanced deep learning solution for kidney disease classification from medical images.

### 🎯 Problem Statement
Kidney diseases often require careful analysis of medical images for diagnosis. Traditional methods can be time-consuming and may lead to delayed diagnosis. Our system aims to:
- Automate the process of kidney disease detection
- Reduce the time required for diagnosis
- Provide consistent and reliable results
- Support medical professionals in their decision-making process

### 🔬 Solution Approach
Our solution leverages state-of-the-art deep learning techniques to analyze kidney medical images:
1. **Image Processing**: Pre-processing of medical images to enhance quality and standardize format
2. **Deep Learning Model**: Implementation of a CNN-based classifier using transfer learning
3. **Web Interface**: User-friendly platform for easy interaction and quick results
4. **Model Management**: Comprehensive tracking and versioning of models and experiments

### 💡 Key Innovations
- Transfer learning approach for better accuracy with limited data
- Real-time prediction capabilities
- Integration of multiple medical imaging modalities
- Automated quality assessment of input images
- Comprehensive logging and monitoring system

### 🎯 Target Users
- Medical professionals and radiologists
- Healthcare institutions
- Medical research organizations
- Healthcare technology developers

### 🌟 Impact
This project has the potential to:
- Improve early detection of kidney diseases
- Reduce diagnosis time
- Enhance treatment planning
- Support medical research
- Contribute to better patient outcomes

## ✨ Features

- 🤖 Deep learning model for kidney disease classification
- 🌐 Web interface for easy interaction
- 📊 Training pipeline with MLflow integration
- 🔄 DVC for data version control
- 🐳 Docker support for containerization
- 🔌 REST API endpoints for predictions

## 🛠️ Technical Stack

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

## 📁 Project Structure

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

## 🚀 Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/suyash-04/Kidney-Disease-Classification.git
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

## 💻 Usage

### 🎯 Training the Model

1. Start the training process:
```bash
python main.py
```

Or use the web interface:
- Navigate to `http://localhost:5000/train`

### 🔮 Making Predictions

1. Start the Flask application:
```bash
python app.py
```

2. Access the web interface:
- Open `http://localhost:5000` in your browser
- Upload an image for prediction

### 🔌 API Endpoints

- `GET /`: Home page
- `GET /predict`: Prediction page
- `POST /predict`: Submit image for prediction
- `GET/POST /train`: Trigger model training

## ⚙️ Model Parameters

The model can be configured through `params.yaml`:
- EPOCHS: 20
- IMAGE_SIZE: [299, 299, 3]
- BATCH_SIZE: 10
- LEARNING_RATE: 0.01
- CLASSES: 2

## 🐳 Docker Support

Build and run the Docker container:
```bash
docker build -t kidney-disease-classifier .
docker run -p 5000:5000 kidney-disease-classifier
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the terms of the license included in the repository.

## 🙏 Acknowledgments

- TensorFlow team for the deep learning framework
- Flask team for the web framework
- All contributors and maintainers