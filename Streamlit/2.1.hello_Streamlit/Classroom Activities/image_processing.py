import cv2 
import numpy as np
from PIL import Image
import streamlit as st

st.title("Image Blur App")

with st.sidebar:
    blur_image= st.slider('چقدر میخواهی تصویر مات بشه ؟ ', 1, 199,21,2)

upload_file = st.file_uploader("Choose an Image ",type=["jpg","png","jpeg"])
if upload_file is not None:
    st.success("فایل با موفقیت آپلود شد")
    image = Image.open(upload_file)
    st.image(image,"Input")
    image = np.array(image)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

    result_image = cv2.blur(image,(blur_image,blur_image))
    result_image = cv2.cvtColor(result_image,cv2.COLOR_BGR2RGB)
    result_image = Image.fromarray(result_image)
   
    st.image(result_image ,"Output")
else:
    st.info("هیچ فایل آپلود نشده")