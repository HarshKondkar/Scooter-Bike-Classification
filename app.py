
import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps
st.title('''Scooter or Motorcycle?????
Let's find out!''')
imag = st.file_uploader('Please upload the image file below:')
if imag is not None:
    img = Image.open(imag)
    st.image(img)
    data = np.ndarray(shape=(1, 256, 256, 3), dtype=np.float32)
    image = img
    #image sizing
    size = (256, 256)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    data[0] = image_array
    model = load_model('model.h5')
    val = model.predict(data)
    if val[0][0] >= 0.5:
        st.write('It is a **Scooter**')
    else:
        st.write('It is a **Motorcycle**')
