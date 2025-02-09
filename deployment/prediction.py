import pandas as pd
import numpy as np
import streamlit as st
import pickle

#load model
with open('best_pipeline.pkl', 'rb') as file:
    model = pickle.load(file)

def run():
    #set title
    st.title('Student Performance')
    st.write('---')

    link_gambar = 'https://tse2.mm.bing.net/th?id=OIP.-i29HcwAtH6ZUfKAXVLYSQHaEK&pid=Api&P=0&h=220'
    st.image(link_gambar, caption = 'source: google.com', use_container_width=True)

    #deskripsi
    st.write('This page contents prediction model that can predict student performance based on attributes required')

    #buat form
    with st.form(key='form parameters'):
        jam_belajar = st.number_input('Hours Studied: ', min_value=0, max_value=44, value=8)
        kehadiran = st.slider('Attendences: ', min_value=0, max_value=100, value=60)
        keterlibatan_ortu = st.selectbox('Parental Involvement: ', ('Low','Medium', 'High'))
        akses_sumber =  st.selectbox('Access to Resources: ', ('Low','Medium', 'High'))
        ekstrakurikuler = st.selectbox('Extracuriccular Activities: ', ('Yes', 'No'))
        jam_tidur = st.slider('Sleep Hours: ', min_value=0, max_value=10, value=6)
        nilai_sebelumnya = st.number_input('Previous Scores: ', min_value=0, max_value=100, value=70)
        motivasi = st.selectbox('Motivation Level: ', ('Low','Medium', 'High'))
        sesi_tutor = st.slider('Tutoring Sessions: ', min_value=0, max_value=8, value=0)
        income = st.selectbox('Family Income: ', ('Low','Medium', 'High'))
        kualitas_guru = st.selectbox('Teacher Quality: ', ('Low','Medium', 'High'))
        sekolah = st.selectbox('School Type: ', ('Private', 'Public'))
        pengaruh = st.selectbox('Peer Influence: ', ('Positive', 'Negative'))
        aktivitas_fisik = st.slider('Physical Activity: ', min_value=0, max_value=6, value=3)
        disabilitas = st.selectbox('Learning Disabilities: ', ('Yes', 'No'))
        pendidikan_orang_tua = st.selectbox('Parental Educational Level: ', ('High School', 'College', 'Postgraduate'))
        jarak = st.selectbox('Distances from Home: ', ('Near', 'Moderate', 'Far'))

        submit=st.form_submit_button('Prediksi')

    data_raw={'Hours_Studied': jam_belajar,
    'Attendance': kehadiran,
    'Parental_Involvement': keterlibatan_ortu,
    'Access_to_Resources': akses_sumber,
    'Extracurricular_Activities': ekstrakurikuler,
    'Sleep_Hours': jam_tidur,
    'Previous_Scores': nilai_sebelumnya,
    'Motivation_Level': motivasi,
    'Tutoring_Sessions': sesi_tutor,
    'Family_Income': income,
    'Teacher_Quality': kualitas_guru,
    'School_Type': sekolah,
    'Peer_Influence': pengaruh,
    'Physical_Activity': aktivitas_fisik,
    'Learning_Disabilities': disabilitas,
    'Parental_Education_Level': pendidikan_orang_tua,
    'Distance_from_Home': jarak
    }

    data = pd.DataFrame([data_raw])
    st.dataframe(data) 

    if submit:
        result = model.predict(data)
        st.write(f'### Scores predicted: {result[0]:.2f}')
    
    link_gambar = 'https://tse3.mm.bing.net/th?id=OIP.msh4Ra07_Lg4qsipBvRdLQHaEL&pid=Api&P=0&h=220'
    st.image(link_gambar, caption = 'Education Moto', use_container_width=True)

if __name__ == '__main__':
    run()