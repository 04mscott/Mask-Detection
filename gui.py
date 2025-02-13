from taipy import Gui
from mask_predictor import predict_with_model
from tensorflow.keras import models
from PIL import Image

model = models.load_model('/Users/masonscott/git-repos/Python-Projects/Face-Mask-Image-Classification/Models/mask_classifier.keras')

img_path = '/Users/masonscott/git-repos/Python-Projects/Face-Mask-Image-Classification/assets/imgs/placeholder_image.png'
content = ''
prob = 0
pred = ''

index = """
<|text-center|
# Mask Detection Model

<|{content}|file_selector|extensions=.png|>
Upload Image of a Person's Face

## <|{pred}|>

<|{img_path}|image|>

<|{prob}|indicator|value={prob}|min=0|max=100|width=25vw|>
>
"""



def on_change(state, var_name, var_val):
    if var_name == "content":
        top_prob, pred = predict_with_model(model, var_val)
        state.img_path = var_val
        state.prob = top_prob * 100
        state.pred = pred


app = Gui(page=index)

if __name__=='__main__':
    app.run(use_reloader=True, port='auto')