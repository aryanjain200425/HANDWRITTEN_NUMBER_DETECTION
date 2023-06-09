import tensorflow as tf
from keras.datasets import mnist
import random
from PIL import Image


(train_data, train_labels), (test_data, test_labels) = mnist.load_data()


#Simplifying the data
train_data = train_data / 255
test_data = test_data / 255


for i in range(len(train_data)):
   pil_image = Image.fromarray(train_data[i])
   randDeg = random.randint(-30,30)
   pil_image = pil_image.rotate(randDeg)
   train_data[i] = pil_image


model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dense(10)
])


model.compile(optimizer = 'adam',
              loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
              metrics = ['accuracy'])

model.fit(train_data, train_labels, epochs = 8)

#TO TEST THE MODEL
# test_loss, test_acc = model.evaluate(test_data,  test_labels, verbose=2)

# print('\nTest accuracy:', test_acc)


#TO SAVE THE CREATED MODEL
model.save("model.h5")