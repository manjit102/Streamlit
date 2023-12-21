import streamlit as st
import pandas as pd

st.subheader('Uploading the csv file')
df = st.file_uploader('Upload the CSV file', type = ['csv','xlsx'])
#st.dataframe(df)

# data = pd.read_csv('C:\\Users\\manji\\OneDrive\\Desktop\\Streamlit\\sleep.csv')
# st.table(data.head())
# st.dataframe(data.head())

st.subheader('Uploading the csv file')
df = pd.read_csv(r'C:\Users\manji\OneDrive\Desktop\Streamlit\sleep.csv')
if df is not None:
    st.table(df.head())
else:
    st.write('File is having no data')

st.subheader('Uploading the image')
#st.image(file_pathof image), is not working thats why i am using following code.
from PIL import Image
# Open and resize the image
original_image = Image.open(r'C:\Users\manji\OneDrive\Desktop\Streamlit\img.jpg')
resized_image = original_image.resize((1200, 600))
# Display the resized image
st.image(resized_image, caption='Resized Image', use_column_width=True)

st.subheader('Uploading the image')
img = st.file_uploader('browse your image', type = ['jpg','png','jpeg'])
if img is not None:
    st.image(img)
else:
    st.text('image is not there.')



st.subheader('working with video file')
video_file = st.file_uploader('Upload the video', type = ['mkv', 'mp4'])
if video_file is not None:
    st.video(video_file, start_time = 0)
else:
    st.text('Video is not uploaded or empty file uploaded.')


st.subheader('working with Audio file')
audio_file = st.file_uploader('Upload the audio file', type = ['mp3','wav'])
if audio_file is not None:
    st.audio(audio_file.read())
else:
    st.write('audio file is not supporting or missing.')
