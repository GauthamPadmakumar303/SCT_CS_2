import streamlit as st
from PIL import Image
import numpy as np
import io

st.set_page_config(page_title="Image Encryption Tool", layout="centered")

st.title("🔐 Image Encryption & Decryption Tool")
st.write("Encrypt or decrypt any image using simple pixel-level XOR operations.")

# User input
operation = st.selectbox("Choose Operation", ["Encrypt", "Decrypt"])
uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
key = st.number_input("Enter key (0-255)", min_value=0, max_value=255, value=123)

def process_image(img, key):
    img = img.convert('RGB')
    img_array = np.array(img)
    processed_array = img_array ^ key  # XOR operation
    return Image.fromarray(processed_array.astype('uint8'))

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 Uploaded Image", use_column_width=True)

    # Encrypt or Decrypt
    result_image = process_image(image, key)
    st.image(result_image, caption="🔄 Processed Image", use_column_width=True)

    # Download button
    buf = io.BytesIO()
    result_image.save(buf, format='PNG')
    byte_im = buf.getvalue()
    st.download_button(
        label="📥 Download Result Image",
        data=byte_im,
        file_name="result.png",
        mime="image/png"
    )
