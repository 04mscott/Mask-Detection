import os
import glob
from sklearn.model_selection import train_test_split
import shutil
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def split_data(path_to_data, path_to_save_train, path_to_save_val, path_to_save_test, test_size=0.2, split_size=0.1):
    
    folders = os.listdir(path_to_data)
    if '.DS_Store' in folders: folders.remove('.DS_Store')
    if 'test' in folders: folders.remove('test')
    if 'train' in folders: folders.remove('train')
    if 'val' in folders: folders.remove('val')

    for folder in folders:
        full_path = os.path.join(path_to_data, folder)
        images_path = glob.glob(os.path.join(full_path, '*.png'))

        # Split data into training, testing, and validation groups
        x_train, x_test = train_test_split(images_path, test_size=test_size)
        x_train, x_val = train_test_split(x_train, test_size=split_size)

        # Move training data to correct folder
        for x in x_train:
            path_to_folder = os.path.join(path_to_save_train, folder)

            if not os.path.isdir(path_to_folder):
                os.mkdir(path_to_folder)
            
            shutil.copy(x, path_to_folder)

        # Move testing data to correct folder
        for x in x_test:
            path_to_folder = os.path.join(path_to_save_test, folder)

            if not os.path.isdir(path_to_folder):
                os.mkdir(path_to_folder)
            
            shutil.copy(x, path_to_folder)

        # Move validation data to correct folder
        for x in x_val:
            path_to_folder = os.path.join(path_to_save_val, folder)

            if not os.path.isdir(path_to_folder):
                os.mkdir(path_to_folder)
            
            shutil.copy(x, path_to_folder)


def create_generators(batch_size, train_data_path, val_data_path, test_data_path):
    train_preprocessor = ImageDataGenerator(
        rescale = 1 / 255.,
        rotation_range=10,
        width_shift_range=0.1
    )

    test_preprocessor = ImageDataGenerator(
        rescale = 1 / 255.
    )

    train_generator = train_preprocessor.flow_from_directory(
        train_data_path,
        class_mode='categorical',
        target_size=(128, 128),
        color_mode='rgb',
        shuffle=True,
        batch_size=batch_size
    )

    val_generator = test_preprocessor.flow_from_directory(
        val_data_path,
        class_mode='categorical',
        target_size=(128, 128),
        color_mode='rgb',
        shuffle=False,
        batch_size=batch_size
    )

    test_generator = test_preprocessor.flow_from_directory(
        test_data_path,
        class_mode='categorical',
        target_size=(128, 128),
        color_mode='rgb',
        shuffle=False,
        batch_size=batch_size
    )

    return train_generator, val_generator, test_generator
