import tensorflow as tf
from keras.datasets import mnist


(train_data, train_labels), (test_data, test_labels) = mnist.load_data()


#Simplifying the data
train_data = train_data / 255
test_data = test_data / 255


model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dense(10)
])


model.compile(optimizer = 'adam',
              loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
              metrics = ['accuracy'])

model.fit(train_data, train_labels, epochs = 8)

model.save('model.h5')