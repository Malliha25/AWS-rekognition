from http import client
import streamlit as st
import boto3
st.title("Face recognition using AWS")
img_file=st.file_uploader("Upload Face Image",type=['png','jpg','jpeg'])
if img_file is not None:
    file_details={}
    file_details['name']=img_file.name
    file_details['type']=img_file.type
    file_details['size']=img_file.size
    st.write(file_details)

    with open("new.png",'wb') as f:
        f.write(img_file.getbuffer())

    client=boto3.client('rekognition')
    imageSource=open("new.png",'rb')
    imageTarget=open("target.png",'rb')
    response=client.compare_faces(
        SimilarityThreshold=80,
        SourceImage={'Bytes':imageSource.read()},
        TargetImage={'Bytes':imageTarget.read()}
    )
    #st.write(response)
    if len(response["FaceMatches"])>0:
        st.success("Face matched")
    else:
        st.error("face not matched")