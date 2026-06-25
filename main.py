from fastapi import FastAPI, UploadFile 
from PIL import Image
import tensorflow as tf
import numpy as np

app = FastAPI()
model = tf.keras.models.load_model("digit_model.h5")
 
@app.post("/predict")
async def predict(file: UploadFile):
    image = Image.open(file.file)
    image = image.convert("L")
    image = image.resize((28,28))
    img = np.array(image)
    img = 255 - img
    img = img / 255
    img = img.reshape(1,28,28)
    prediction = model.predict(img)
    digit = int(np.argmax(prediction))
    confidence = float(np.max(prediction))

    return{
        "digit" : digit, 
        "confidence" : confidence    } 