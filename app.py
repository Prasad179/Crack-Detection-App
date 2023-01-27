
import streamlit as st
from img_classification import teachable_machine_classification
from PIL import Image

app_mode = st.sidebar.selectbox('Select Page',['Home','Check for Cracks','Help']) #two pages


if app_mode=='Home':
    st.title("BRIDGE CRACK DETECTION SYSTEM")
    st.image('bridge_img.jpg')
    #st.header("Checking for crack availability in bridge walls")
    #st.text("Upload wall image")
elif app_mode == 'Check for Cracks':
    uploaded_file = st.file_uploader("Upload image ...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded photograph.', use_column_width=True)
        st.write("")
        st.write("Detecting...")
        label = teachable_machine_classification(image, 'model_ps1.h5')
        if label == 0:
            st.success("No Crack Detected!:white_check_mark:")
            
        else:
            st.warning("Crack Detected!!:warning:")
            
elif app_mode == 'Help':
    st.header("Help")
    st.write("Please contact for any quries:")
    st.write("email: prasaddevkar179@gmail.com")