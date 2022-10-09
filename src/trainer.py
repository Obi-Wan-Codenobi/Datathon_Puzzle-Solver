import numpy as np
import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
import keras
import os
from glob import glob
from keras import layers
from PIL import Image
from keras.utils import load_img, img_to_array
import keras.optimizers
import keras.losses
import keras.metrics
from sklearn.model_selection import train_test_split

ansToClass = {'0123': 0, '0132': 1, '0213': 2, '0231': 3, '0312': 4, '0321': 5, '1023': 6, '1032': 7, '1203': 8, '1230': 9, '1302': 10, '1320': 11, '2013': 12, '2031': 13, '2103': 14, '2130': 15, '2301': 16, '2310': 17, '3012': 18, '3021': 19, '3102': 20, '3120': 21, '3201': 22, '3210': 23}
x_train = []
x_test = []
x_val = []
y_train = []
y_test = []
y_val = []
# i = 0

# for img_name in glob('train\\0123\\*'):
#     image = load_img(f'{img_name}', target_size=(128, 128))
#     img_arr = img_to_array(image)
#     if i % 10 == 9:
#         if i % 20 == 19:
#             x_val.append(img_arr)
#             y_val.append(0)
#         else:
#             x_test.append(img_arr)
#             y_test.append(0)
#     else:
#         x_train.append(img_arr)
#         y_train.append(0)
#     i += 1
for root,dirs,files in os.walk('/mnt/c/Users/devon/PycharmProjects/puzzle/train', topdown=True):
    curDir = root[root.rfind('/')+1:]
    i = 0
    if len(curDir) != 4:
        continue
    print(curDir)
    # print(dirs)
    # print(files)
    print('----------------')
    for img_name in glob(root + '/*'):
        if i > 1500:
            break
        image = load_img(f'{img_name}', target_size=(128, 128))
        img_arr = img_to_array(image)
        if i % 10 == 9:
            if i % 20 == 19:
                x_val.append(img_arr)
                y_val.append(ansToClass[curDir])
            else:
                x_test.append(img_arr)
                y_test.append(ansToClass[curDir])
        else:
            x_train.append(img_arr)
            y_train.append(ansToClass[curDir])
        image.close()
        i += 1
if len(x_train) == 0:
    print("error: x_train empty")
    exit(255)
if len(x_test) == 0:
    print("error: x_test empty")
    exit(255)
if len(x_val) == 0:
    print("error: x_val empty")
    exit(255)
if len(y_train) == 0:
    print("error: y_train empty")
    exit(255)
if len(y_test) == 0:
    print("error: y_test empty")
    exit(255)
if len(y_val) == 0:
    print("error: y_val empty")
    exit(255)
print(i)
# print(x_train)
# print(y_train)
x_train = np.array(x_train)
x_test = np.array(x_test)
x_val = np.array(x_val)
y_train = np.array(y_train)
y_test = np.array(y_test)
y_val = np.array(y_val)
# model = keras.models.load_model('example_model.h5')
# inputs = keras.Input(shape=(128,128,3), name="image")
# # x = layers.Conv2D(2, 3, activation="relu", name="conv2d_1", input_shape=(128,128,3))(inputs)
# # x = layers.Conv2D(2, 3, activation="relu", name="conv2d_2")(x)
# x = layers.Dense(64, activation="relu", name="dense_1")(inputs)
# x = layers.Dense(64, activation="relu", name="dense_2")(x)
# outputs = layers.Dense(24, activation="softmax", name="predictions")(x)

# model = keras.Model(inputs=inputs, outputs=outputs)
old_model = keras.models.load_model('example_model.h5')
model = keras.models.clone_model(old_model)

# for img_name in glob('train\\0123\\*'):
#     image = load_img(f'{img_name}', target_size=(128, 128))
#     img_arr = img_to_array(image)
#     if i % 10 == 9:
#         if i % 20 == 19:
#             x_val.append(img_arr)
#             y_val.append(0)
#         else:
#             x_test.append(img_arr)
#             y_test.append(0)
#     else:
#         x_train.append(img_arr)
#         y_train.append(0)
#     i += 1
# print(y_train)
# print(y_test)
# print(x_test)
# print(x_train)


model.compile(
    optimizer=keras.optimizers.Adam(),
    loss=keras.losses.SparseCategoricalCrossentropy(),
    metrics=[keras.metrics.SparseCategoricalAccuracy()],
)
history = model.fit(
    x_train,
    y_train,
    batch_size=32,
    epochs=10,
    validation_data=(x_val, y_val),
)
model.save("training_model")
model.save("training_model.h5", save_format='h5')
