import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense

(X_train,y_train),(X_test,y_test) = mnist.load_data()

X_train = X_train/255
X_test = X_test/255

model = Sequential([
    Flatten(input_shape = (28,28)),
    Dense(128 , activation= 'relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')

])

model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])

model.fit(X_train,y_train,epochs = 5)

loss,accuracy = model.evaluate(X_test,y_test)

print ("Accuracy:" , accuracy)

model.save("digit_model.h5")


