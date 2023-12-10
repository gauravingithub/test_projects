import tensorflow as tf
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

image_path = 'test_images'

model = tf.keras.models.load_model('digitRecogModel')

for image_num in range(1,10):
    img = cv.imread(f'{image_path}/{image_num}.png')[:,:,0]
    img = np.invert(np.array([img]))
    prediction = model.predict(img)
    print(f'Prediction is: {np.argmax(prediction)}')
    plt.imshow(img[0], cmap=plt.cm.binary)
    plt.show()