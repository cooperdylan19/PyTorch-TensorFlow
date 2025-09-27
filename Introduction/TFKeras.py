import tensorflow

from keras import Sequential, Input
from keras.layers import Dense

model = Sequential([
    Input(shape=(784,)),                     # define and compile a model
    Dense(units=64, activation='relu'),
    Dense(units=10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
