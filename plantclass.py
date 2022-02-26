import streamlit as st
from PIL import Image
img =Image.open('download.jpg')
st.set_page_config(page_title='Plant Disease Classification  By Kabir Arya')
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown('<center><h1 class="font">Plant Disease Classificaton </center></h1>',unsafe_allow_html=True)
st.write("This project is made by 3 students of different collages in which all of them contributed with equal amount of time to solve plant related problem using this app people can upload their plant picture our app will tell all things realated \nEven This is Free")
st.write('1.Ayush Arya[Graphic Era Hill University : 2021-2025]')
st.write('2.SRIRAM[Sairam Engineering College : 2020-2024]')
st.write('3.Diksha Silawat[Bhopal Institute of Technology : 2020-2024]')
uploade=st.file_uploader("",type=['png','jpg','jpeg'])
if uploade is not None:
    image=Image.open(uploade)
    col1,col2=st.columns([0.5,0.5])
    import requests

    img = uploade.name

    url = 'https://pl-ml.herokuapp.com/api'
    my_img = {'image': open(img, 'rb')}
    r = requests.post(url, files=my_img)
    p = r.json()

    # convert server response into JSON format.
    # print(r.json())
    # convert server response into JSON format.
    # print(r.json())
    st.write(p)
    st.markdown('<center><h2 class="font">@Kabir_Arya001</center></h2>',
                unsafe_allow_html=True)

    # convert server response into JSON format.
    # print(r.json())
    with col1:
        st.markdown('<p style="text-align:center;"></p>', unsafe_allow_html=True)
        st.image(image, width=300)


