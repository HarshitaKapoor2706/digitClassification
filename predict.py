import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("digit_model.h5")

(_,_),(X_test,y_test) = tf.keras.datasets.mnist.load_data()


X_test = X_test / 255

predication = model.predict(X_test)
digit = np.argmax(predication , axis =1)
print("predicted", digit[0])
print("actual:",y_test[0])

print("searching for model mistakes")
mistake_count =0

for i in range(len(X_test)):
    if digit[i] != y_test[i]:
        print(f"Mistake at img #{i}: model guessed {digit[i]} but actual was {y_test[i]}")
        mistake_count +=1

        if mistake_count >= 20 :
            print("and more...")
            break
