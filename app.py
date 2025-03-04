import os
import shutil
from taipy.gui import Gui
from tensorflow.keras import models
from mask_predictor import predict_with_model

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
# Set base directory for accessing files in venv/deployed application
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load Model
print('Loading Keras Model...')
model_path = os.path.join(base_dir, 'Models', 'mask_classifier.keras')
model = models.load_model(model_path)
print("Model Successfully Loaded")

# Placeholder image file path
temp_img = ''
img_path = os.path.join(base_dir, 'assets', 'imgs', 'placeholder_image.png')
prediction = ""
prob = 0
pred = ""

index = """
<|text-center|
# Face Mask Image Classifier

<|{img_path}|image|width=25vw|>

<|{temp_img}|file_selector|extensions=.png|>
Upload an Image

<|{prob}|indicator|value={prob}|min=0|max=100|width=25vw|>

<|{pred}|>
|>
"""

def on_change(state, var_name, var_val):
    if var_name == 'temp_img':
        # Remove old image from temp directory
        if 'placeholder_image.png' not in state.img_path:
            os.remove(state.img_path)

        # Create a temp directory to save image
        temp_dir = os.path.join(base_dir, 'temp')
        os.makedirs(temp_dir, exist_ok=True)

        # Save the image
        temp_img = os.path.join(temp_dir, os.path.basename(var_val))
        shutil.copy(var_val, temp_img)

        # Update state to display image
        state.img_path = temp_img

        # Run prediction model
        top_prob, prediction = predict_with_model(model, temp_img)

        state.prob = round(top_prob * 100, 2)
        state.pred = "Prediction: " + prediction

app = Gui(page=index)

if __name__=='__main__':
    app.run(title="Face Mask Classifier", host="0.0.0.0", port=8000, mode='rest')