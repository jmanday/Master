import numpy as np
import os
import cv2
import sys
import glob
import pandas as pd
from PIL import Image
from keras.datasets import cifar10
from multiprocessing import Pool, cpu_count, freeze_support
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.constraints import maxnorm
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.core import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.utils import np_utils
from keras import backend as K
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from checkScore2 import getScore

SEED = 14

NUM_EPOCHS = 10
BATCH_SIZE = 15

SIZE = 64
NUM_CLASSES = 3

SOLUTION_SGT1 = "solution_stg1_release.csv"

# get the size of image
def im_multi(path):
    try:
        im_stats_im_ = Image.open(path)
        return [path, {'size': im_stats_im_.size}]
    except:
        print(path)
        return [path, {'size': [0, 0]}]

# add a new field (size) to dataset
def im_stats(im_stats_df):
    im_stats_d = {}
    p = Pool(cpu_count())
    ret = p.map(im_multi, im_stats_df['path'])
    for i in range(len(ret)):
        im_stats_d[ret[i][0]] = ret[i][1]
    im_stats_df['size'] = im_stats_df['path'].map(lambda x: ' '.join(str(s) for s in im_stats_d[x]['size']))
    return im_stats_df

# get cv2 each image
def get_im_cv2(path):
    img = cv2.imread(path)
    resized = cv2.resize(img, (SIZE, SIZE), cv2.INTER_LINEAR)
    return [path, resized]


def normalize_image_features(paths):
    imf_d = {}
    p = Pool(cpu_count())
    ret = p.map(get_im_cv2, paths)
    for i in range(len(ret)):
        imf_d[ret[i][0]] = ret[i][1]
    ret = []
    fdata = [imf_d[f] for f in paths]
    fdata = np.array(fdata, dtype=np.uint8)
    fdata = fdata.astype('float32')
    fdata = fdata / 255
    return fdata


# create file "train.npy" with the datas of normalized image
def load_data_train():
    train = glob.glob('./input2/train/**/*.jpg')
    #train_additional = glob.glob('./input/additional/**/*.jpg')
    #train = train + train_additional
    train = pd.DataFrame([[p.split('/')[3],p.split('/')[4],p] for p in train], columns = ['type','image','path'])
    train = im_stats(train)
    train = train[train['size'] != '0 0'].reset_index(drop=True) #remove bad images
    train_data = normalize_image_features(train['path'])
    np.save('train.npy', train_data, allow_pickle=True, fix_imports=True)
    return train

# create file "test.npy" with the datas of normalized image
def load_data_test():
    test = glob.glob('./input2/test/*.jpg')
    test = pd.DataFrame([[p.split('/')[3],p] for p in test], columns = ['image','path']) #[::20] #limit for Kaggle Demo
    test_data = normalize_image_features(test['path'])
    np.save('test.npy', test_data, allow_pickle=True, fix_imports=True)
    return test

# create the model to CNN
def create_model(opt_='adamax'):
    if K.image_data_format() == 'channels_first':
        input_shape_aux = (3, SIZE, SIZE)
    else:
        input_shape_aux = (SIZE, SIZE, 3)
    model = Sequential()
    model.add(Conv2D(16, (3, 3), input_shape=input_shape_aux, padding='same', activation='relu', kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.2))
    model.add(Conv2D(16, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.5))
    model.add(Dense(NUM_CLASSES, activation='softmax'))
    model.compile(optimizer=opt_, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model


# create file "train_target.npy" with the types of class
def get_class(train):
    le = LabelEncoder()
    train_target = le.fit_transform(train['type'].values)
    #print(le.classes_) #in case not 1 to 3 order
    np.save('train_target.npy', train_target, allow_pickle=True, fix_imports=True)
    #return train_target

if __name__ == "__main__":

    name_file_csv = sys.argv[1]

    print("\n- Load datas ...")

    test_data = load_data_test() # get dataset with values of test images

    train = load_data_train() # get dataset with values of train images

    get_class(train) # get the class



    test_id = test_data.image.values
    np.save('test_id.npy', test_id, allow_pickle=True, fix_imports=True)

    train_data = np.load('train.npy') # load data train images
    test_data = np.load('test.npy')
    train_target = np.load('train_target.npy')

    print('Generating validation data...')
    x_train, x_val_train, y_train, y_val_train = train_test_split(train_data, train_target, test_size=0, random_state=SEED)

    print('Data augmentation...')
    datagen = ImageDataGenerator(rotation_range=0.3, zoom_range=0.3)
    datagen.fit(train_data)

    print('Training model...')
    model = create_model()
    print(model.summary())
    model.fit_generator(generator=datagen.flow(x_train, y_train, batch_size=BATCH_SIZE, shuffle=True),
                        validation_data=(x_val_train, y_val_train),
                        epochs=NUM_EPOCHS, steps_per_epoch=len(x_train))

    print('Predicting...')
    pred = model.predict_proba(test_data)

    print('Exporting to CSV...')
    df = pd.DataFrame(pred, columns=['Type_1', 'Type_2', 'Type_3'])
    df['image_name'] = test_id

    df.to_csv(name_file_csv, index=False)
    getScore(name_file_csv)
