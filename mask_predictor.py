import tensorflow as tf
import numpy as np

def predict_with_model(model, img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_png(img, channels=3)
    img = tf.image.convert_image_dtype(img, dtype=tf.float32)
    img = tf.image.resize(img, [128,128]) # tensor with shape: (128,128,3) <-- (height, width, channels)
    img = tf.expand_dims(img, axis=0) # tensor with shape: (1,128,128,3) <-- (batch size, height, width, channels)

    classes = ['Mask Worn Incorrectly', 'Mask Worn Correctly', 'No Mask']

    probs = model.predict(img) # Returns list of probabilities of img belonging to each class
    top_prob = probs.max()
    pred = classes[np.argmax(probs)] # Index of max value

    return top_prob, pred

if __name__=='__main__':
    img_path = '/Users/masonscott/git-repos/Python-Projects/Face-Mask-Image-Classification/Dataset/test/without_mask/90.png'
    model = tf.keras.models.load_model('/Users/masonscott/git-repos/Python-Projects/Face-Mask-Image-Classification/Models/mask_classifier.keras')
    top_prob, pred = predict_with_model(model, img_path)

    print(f'prediction = {pred}')