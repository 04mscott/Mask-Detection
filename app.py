from flask import Flask
from flask import jsonify
import os
import base64
from flask import request
from mask_predictor import predict_with_model
from tensorflow.keras import models

app = Flask(__name__)

def get_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    global model
    model_path = os.path.join(base_dir, 'Models', 'mask_classifier.keras')
    model = models.load_model(model_path)
    print("Model Successfully Loaded")

print('Loading Keras Model...')
get_model()

@app.route("/predict", methods = ['POST'])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    # Save file temporarily to pass to predict fxn
    temp_img_path = 'temp_img.png'
    with open(temp_img_path, 'wb') as img_file:
        img_file.write(decoded)

    top_prob, pred = predict_with_model(model, temp_img_path)
    # Remove file when finished
    os.remove(temp_img_path)

    response = {
        'prediction' : str(pred) + ', Confidence: ' + str(top_prob * 100) + '%'
    }

    return jsonify(response)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001)