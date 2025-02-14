import os
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import tensorflow as tf

from my_utils import split_data, create_generators
from learning_model import mask_classifier

if __name__=='__main__':

    path_to_train = '/Users/masonscott/git-repos/Python-Projects/Face-Mask-Image-Classification/Dataset/train'
    path_to_val = '/Users/masonscott/git-repos/Python-Projects/Face-Mask-Image-Classification/Dataset/val'
    path_to_test = '/Users/masonscott/git-repos/Python-Projects/Face-Mask-Image-Classification/Dataset/test'
    batch_size = 16
    epochs = 20
    lr = 0.0001 # default learning rate

    train_generator, val_generator, test_generator = create_generators(batch_size, path_to_train, path_to_val, path_to_test)
    num_classes = train_generator.num_classes

    TRAIN = False
    TEST = True
    SPLIT_DATA = False
    

    if SPLIT_DATA:
            path_to_data = '/Users/masonscott/git-repos/Python-Projects/Face-Mask-Image-Classification/Dataset'
            path_to_save_train = '/Users/masonscott/git-repos/Python-Projects/Face-Mask-Image-Classification/Dataset/train'
            path_to_save_val = '/Users/masonscott/git-repos/Python-Projects/Face-Mask-Image-Classification/Dataset/val'
            path_to_save_test = '/Users/masonscott/git-repos/Python-Projects/Face-Mask-Image-Classification/Dataset/test'
            split_data(path_to_data, path_to_save_train, path_to_save_val, path_to_save_test)


    if TRAIN:

        # Saves the best model from the validation accuracy during training
        checkpoint_path = '/Users/masonscott/git-repos/Python-Projects/Face-Mask-Image-Classification/Models/mask_classifier.keras'
        checkpoint_dir = os.path.dirname(checkpoint_path)
        checkpoint_saver = ModelCheckpoint(
            checkpoint_path,
            monitor='val_accuracy',
            # max for val_accuracy, min for val_loss
            mode='max',
            save_best_only=True,
            save_freq='epoch',
            verbose=1
        )

        early_stop = EarlyStopping(monitor='val_accuracy', patience=10)

        model = mask_classifier(num_classes)

        optimizer = tf.keras.optimizers.Adam(learning_rate=lr)
        model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

        model.fit(
            train_generator,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=val_generator,
            callbacks=[checkpoint_saver, early_stop]
        )


    if TEST:
        model = tf.keras.models.load_model('/Users/masonscott/git-repos/Python-Projects/Face-Mask-Image-Classification/Models/mask_classifier.keras')
        model.summary()

        print('Evaluating Validation Set:')
        model.evaluate(val_generator)

        print('Evaluating Test Set:')
        model.evaluate(test_generator) 