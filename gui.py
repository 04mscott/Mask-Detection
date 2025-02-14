import os
import shutil
from taipy import Gui
from mask_predictor import predict_with_model
from tensorflow.keras import models


model = models.load_model('Models/mask_classifier.keras')

UPLOAD_DIR = 'tmp/uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

uploaded_file = None
img_path = 'assets/imgs/placeholder_img.png'
prob = 0
pred = ''

index = """
<|text-center|
# Mask Detection Model

<|{uploaded_file}|file_selector|extensions=.png|>
Upload Image of a Person's Face

## <|{pred}|>

<|{img_path}|image|>

<|{prob}|indicator|value={prob}|min=0|max=100|width=25vw|>
>
"""


def on_change(state, var_name, var_val):
    if var_name == "uploaded_file" and var_val:
        tmp_file_path = os.path.join(UPLOAD_DIR, os.path.basename(var_val))
        shutil.copy(var_val, tmp_file_path)

        top_prob, pred = predict_with_model(model, var_val)

        state.img_path = tmp_file_path
        state.prob = top_prob * 100
        state.pred = pred


app = Gui(page=index)

if __name__=='__main__':
    app.run(use_reloader=True, port='auto')