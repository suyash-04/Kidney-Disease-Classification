from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
from flask_cors import CORS, cross_origin
from src.cnnClassifier.utils.utils import decodeImage
from src.cnnClassifier.pipeline.predict import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('home.html')

@app.route("/predict", methods=['GET', 'POST'])
@cross_origin()
def predictRoute():
    if request.method == 'GET':
        return render_template('predict.html')

    if request.method == 'POST':
        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.classifier.predict()
        return jsonify(result)

@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"

if __name__ == "__main__":
    clApp = ClientApp()
    port  = int(os.environ.get("PORT", 5000))

    app.run(host='0.0.0.0', port=port, debug=True)
