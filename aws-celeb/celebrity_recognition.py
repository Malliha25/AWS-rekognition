import streamlit as st
import boto3
st.title("Celebrity recognition using AWS")
img_file=st.file_uploader("Upload Face Image",type=['png','jpg','jpeg','wepb'])
if img_file is not None:
    file_details={}
    file_details['name']=img_file.name
    file_details['type']=img_file.type
    file_details['size']=img_file.size
    #st.write(file_details)

    with open("new.png",'wb') as f:
        f.write(img_file.getbuffer())

    client=boto3.client('rekognition')
    image=open("new.png",'rb')
    response=client.recognize_celebrities(
        Image={'Bytes':image.read()}
    )
    #st.write(response)
    if (len(response['CelebrityFaces'])>0):
        st.success("celebrity found")          
        st.write('Name: ' + response["CelebrityFaces"][0]['Name'])
        st.write('KnownGender: ' + response["CelebrityFaces"][0]['KnownGender']['Type'])
        st.write("URL: "+response["CelebrityFaces"][0]['Urls'][0])
    else:
        st.error("Celebrity Not found")