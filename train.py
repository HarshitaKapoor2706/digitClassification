import tensorflow as tf
import tensorflow.keras.datasets as mnist
import tensorflow.keras.models as Sequential
from tensorflow.keras.layers import Dense,Flatten

(X_train,y_train),(X_test,y_test) = mnist.load_data()

X_train = X_train/255
