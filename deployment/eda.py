#import libraries
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run():
    #introduction
    st.title("Exploratory Data Analysis of Student Performance")
    #konsep markdown
    st.write('This page containts Exploratory Data Analysis of Student Performance based on previous model')
    st.write('---')

    #memasukan gambar
    link_gambar = 'https://tse4.mm.bing.net/th?id=OIP.2z-TeTNwM-ATHuzdStRADgHaDt&pid=Api&P=0&h=220'
    st.image(link_gambar, caption='source:google.com', use_container_width=True)

    #menampilkan dataframe
    st.write('## Dataframe')

    teams = pd.read_csv('StudentPerformanceFactors.csv')
    st.dataframe(teams.head())

    st.write('''
            Indonesia menduduki peringkat 68 dari 81 negara di dunia dalam kemampuan matematika yang erat hubungannya dengan kemampuan bernalar.
            Hal ini cukup mengkhawatirkan karena Indonesia sendiri digadang-gadang akan memiliki bonus demografi di tahun 2045 di mana 
            jumlah penduduk yang berusia muda akan lebih banyak dari jumlah penduduk yang berusia senja. Generasi muda  akan mulai mengambil alih kendali 
            atas negeri ini yang mana akan sangat berbahaya apabila generasi penerus tidak memiliki kemampuan bernalar yang mumpuni. Sebagai tambahan, 
            tidak seimbangnya kemampuan bernalar dengan kebutuhan industri di masa depan akan menyebabkan lebih banyak pengangguran yang akan membebani ekonomi 
            baik bagi negara maupun bagi individu itu sendiri. Program yang akan dibuat ini akan membantu untuk memprediksi performa matematika seorang pelajar yang 
            dinyatakan dalam skor berdasarkan beberapa faktor diantaranya latar belakang keluarga, pengaruh teman sejawat, jarak antara rumah dan sekolah, serta fasilitas 
            pendukung proses belajar anak seperti diadakannya kegiatan ektrakurikuler. 
            - Bagi orang tua, program ini bisa dijadikan acuan untuk pertimbangan memilih sekolah dan acuan untuk lebih memperhatikan fasilitas dan dukungan mental yang dapat meningkatkan performa anak-anaknya. 
            - Bagi pelajar, program ini bisa dijadikan acuan untuk menjaga diri dari hal-hal yang mungkin dapat berpengaruh terhadap performanya di sekolah, khususnya di bidang matematika. 
            ''')

    #sub bab visualisasi

    st.write('### Persentase Jarak Rumah ke Sekolah')
    percentage = teams['Distance_from_Home'].value_counts(normalize=True) * 100

   
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(percentage, labels=percentage.index, autopct='%1.1f%%', startangle=90,
        colors=['#66c2a5', '#fc8d62', '#8da0cb'])

    ax.set_title('Percentage of Home-to-School Distance')
    ax.set_ylabel('')  

    
    st.pyplot(fig)


    st.write('**Insight:**')
    st.write('Sebanyak 10.1% orang tua memilih menyekolahkan anaknya di sekolah yang jauh dan sebanyak 30.6% memilih sekolah yang tidak terlalu jauh maupun tidak terlalu dekat dengan rumah. Hal ini bisa jadi karena faktor kualitas sekolah menjadi hal utama dalam pengambilan keputusan')

    # Visualisasi menggunakan boxplot
    st.write('### Distribusi Performa Anak Berdasarkan Keterlibatan Orang Tua')
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Parental_Involvement', y='Exam_Score', data=teams, palette='Set2')
    plt.title('Distribusi Skor Ujian Berdasarkan Keterlibatan Orang Tua', fontsize=16)
    plt.xlabel('Tingkat Keterlibatan Orang Tua', fontsize=12)
    plt.ylabel('Skor Ujian', fontsize=12)
    st.pyplot(plt)
    st.write('**Insight:**')
    st.write('Dari analisa di atas, dapat disimpulkan bahwa semakin tinggi keterlibatan orang tua, semakin tinggi performa anak di sekolah. Artinya antara keterlibatan orang tua dengan performa anak memiliki korelasi yang positif. Keterlibatan yang dimaksud adalah berupa pemberian dukungan mental dan fasilitas yang menunjang performa anak')

    #dynamic hystogram
    st.write('### Distribusi Data')

    opsi=st.selectbox('Pilih Data:',
                    ('Hours_Studied', 'Attendance', 'Parental_Involvement',
        'Access_to_Resources', 'Extracurricular_Activities', 'Sleep_Hours',
        'Previous_Scores', 'Motivation_Level', 'Tutoring_Sessions',
        'Family_Income', 'Teacher_Quality', 'School_Type', 'Peer_Influence',
        'Physical_Activity', 'Learning_Disabilities',
        'Parental_Education_Level', 'Distance_from_Home'))

    fig = plt.figure(figsize=(8,5))
    sns.histplot(teams[opsi], bins=20, kde=True)
    st.pyplot(fig)

    #latar belakang ekonomi terhadap motivasi anak
    st.write('### Latar Belakang Ekonomi Keluarga terhadap Motivasi Anak')
    # Membuat Tabel Kontingensi
    contingency_table = pd.crosstab(teams['Family_Income'], teams['Motivation_Level'])
    # Membuat Heatmap
    figure = plt.figure(figsize=(8, 6))
    sns.heatmap(contingency_table, annot=True, fmt="d", cmap="Blues", cbar=False)
    plt.title("Distribusi Motivasi Berdasarkan Latar Belakang Ekonomi Keluarga")
    plt.ylabel("Latar Belakang Ekonomi")
    plt.xlabel("Motivasi Anak")
    st.pyplot(figure)
    st.write('**Insight:**')
    st.write('Dari hasil di atas dapat motivasi belajar yang tinggi cenderung didorong dari latar belakang ekonomi yang medium. Sedangkan motivasi belajar yang rendah cenderung didapati dari anak-anak yang memiliki latar belakang ekonomi yang rendah')

    #Kualitas pengajar terhadap tipe sekolah
    st.write('### Kualitas Pengajar Berdasarkan Tipe Sekolah')
    # Membuat figure untuk visualisasi
    gambar=plt.figure(figsize=(10, 6))
    # Grouping data berdasarkan Tipe Sekolah dan Kualitas Pengajar
    grouped = teams.groupby(['School_Type', 'Teacher_Quality']).size().unstack()
    # Menampilkan pie chart untuk setiap Tipe Sekolah
    for i, school_type in enumerate(grouped.index):
        plt.subplot(1, len(grouped.index), i+1)  # Menentukan jumlah subplots berdasarkan jumlah Tipe Sekolah
        data = grouped.loc[school_type]  # Data untuk tipe sekolah tertentu
        data.plot(kind='pie', autopct='%1.1f%%', legend=False)
        plt.title(f'Tipe Sekolah: {school_type}')
    # Menambahkan judul umum
    plt.suptitle('Distribusi Kualitas Pengajar Berdasarkan Tipe Sekolah')
    # Menampilkan plot
    plt.tight_layout()
    st.pyplot(gambar)
    st.write('**Insight:**')
    st.write('Dari hasil uji di atas dapat dilihat bahwa sekolah swasta lebih banyak memiliki kualitas pengajar yang tinggi dibandingkan sekolah negeri. Hal ini bisa menjadi acuan bagi para orang tua terutama untuk pendidikan dasar')

    link_gambar = 'https://tse1.mm.bing.net/th?id=OIP.L0QriE9s9rT43YdhQX5JggHaE8&pid=Api&P=0&h=220'
    st.image(link_gambar, use_container_width=True)


if __name__ == '__main__':
    run()
