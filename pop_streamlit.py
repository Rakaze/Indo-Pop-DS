import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

data = 'D:\\ITDP\\Data Science\\new_pop.csv'
df = pd.read_csv(data, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')

st.set_page_config(page_title='Data Population of Indonesia', layout="wide", page_icon=':bar_chart:')
hide_menu = """
<style>
#MainMenu {
    visibility:hidden;
}
footer{
    visibility:hidden;
}
"""
st.write('''
# Data Populasi Indonesia 🧍🧍🏻‍♀️
Menampilkan data Populasi di Indonesia
''')

st.write("Made with :heart: by Raka, Nobel dan Odita")
st.write("Data from: Bjorka")
st.write("Tech: Python, Streamlit, Pandas and Plotly")
st.write('---')

st.subheader("Sebaran Populasi")

kol1, kol2, kol3, kol4 = st.columns(4)

with kol1:
    banyak_orang = df['no_nik'].count()
    kol1.metric('Banyak Penduduk', banyak_orang)

with kol2:
    banyak_provinsi = df['provinsi'].nunique()
    kol2.metric('Banyak Provinsi', banyak_provinsi)

with kol3:
    banyak_kabupaten = df['kabupaten'].nunique()
    kol3.metric('Banyak Kabupaten', banyak_kabupaten)

with kol4:
    banyak_kecamatan = df['kecamatan'].nunique()
    kol4.metric('Banyak Kecamatan', banyak_kecamatan)
st.write('---')
st.write('Sebaran data wilayah (Provinsi, Kecamatan, Kabupaten)')
option1 = st.selectbox(
     'Pilih data wilayah',
     ('Provinsi', 'Kecamatan', 'Kabupaten'))

st.write('Memilih data provinsi:', option1)
if option1=='Provinsi':
    # modeAmount = df.groupby('provinsi')[['no_nik']].count().sort_values(by=['no_nik'],ascending=[True]).tail(10).reset_index()

    labels = df['provinsi'].value_counts().index
    values = df['provinsi'].value_counts().values
    fig = px.bar(df, x=values, y=labels, height=600, title='Sebaran Provinsi', text_auto='.2f')
    fig.layout.update(xaxis_title="Total", yaxis_title="Provinsi", yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)
elif option1=='Kecamatan':
    modeAmount = df.groupby('kecamatan')[['no_nik']].count().sort_values(by=['no_nik'],ascending=[True]).tail(10).reset_index()
    fig = px.bar(modeAmount, x='no_nik', y='kecamatan', height=600, title='Sebaran Kecamatan', text_auto='.2f')
    fig.layout.update(xaxis_title="Total", yaxis_title="Kecamatan")
    st.plotly_chart(fig, use_container_width=True)
else:
    modeAmount = df.groupby('kabupaten')[['no_nik']].count().sort_values(by=['no_nik'],ascending=[True]).tail(10).reset_index()
    fig = px.bar(modeAmount, x='no_nik', y='kabupaten', height=600, title='Sebaran Kabupaten', text_auto='.2f')
    fig.layout.update(xaxis_title="Total", yaxis_title="Kabupaten")
    st.plotly_chart(fig, use_container_width=True)


col1, col2 = st.columns(2)
with col1:
    option = st.selectbox(
        'Pilih data wilayah provinsi',
        ('NASIONAL', 'ACEH', 'SUMATERA UTARA', 'SUMATERA BARAT', 'RIAU', 'JAMBI', 'SUMATERA SELATAN', 'BENGKULU', 'LAMPUNG','KEPULAUAN BANGKA BELITUNG', 'KEPULAUAN RIAU', 'DKI JAKARTA', 'JAWA BARAT', 'JAWA TENGAH', 'DAERAH ISTIMEWA YOGYAKARTA', 'JAWA TIMUR', 'BANTEN', 'BALI', 'NUSA TENGGARA BARAT', 'NUSA TENGGARA TIMUR', 'KALIMANTAN BARAT', 'KALIMANTAN TENGAH', 'KALIMANTAN SELATAN','KALIMANTAN TIMUR', 'KALIMANTAN UTARA', 'SULAWESI UTARA', 'SULAWESI TENGAH', 'SULAWESI SELATAN', 'SULAWESI TENGGARA', 'GORONTALO', 'SULAWESI BARAT', 'MALUKU', 'MALUKU UTARA', 'PAPUA', 'PAPUA BARAT'))

    st.write('Memilih data provinsi:', option)

with col2:
    option2 = st.selectbox(
        'Pilih jenis data',
        ('Jenis Kelamin', 'TPS', 'Disabilitas'))
    st.write('Memilih data provinsi:', option2)


if (option=='NASIONAL' and option2=='Jenis Kelamin'):
    banyak_orang = df['no_nik'].count()
    st.write('Terdapat: ' + str(banyak_orang) +' orang')

    labels = df['jns_kelamin'].value_counts().index
    values = df['jns_kelamin'].value_counts().values

    # modeAmount = df.groupby('jns_kelamin')[['no_nik']].count().sort_values(by=['no_nik'],ascending=[True]).tail(10).reset_index()
    # fig = px.bar(modeAmount, x='no_nik', y='jns_kelamin', height=600, title='Sebaran Tempat Lahir')
    # fig.layout.update(xaxis_title="Total", yaxis_title="Tempat Lahir")
    fig = px.pie(df, values=values, names=labels, title=('Sebaran Data Jenis Kelamin di ' + option))
    st.plotly_chart(fig, use_container_width=True)

elif (option!='NASIONAL' and option2=='Jenis Kelamin'):
    banyak_orang = df[df['provinsi']==option]['no_nik'].count()
    st.write('Terdapat: ' + str(banyak_orang) +' orang')
    labels = df[df['provinsi']==option]['jns_kelamin'].value_counts().index
    values = df[df['provinsi']==option]['jns_kelamin'].value_counts().values

    fig = px.pie(df, values=values, names=labels, title=('Sebaran Data Jenis Kelamin di ' + option))
    st.plotly_chart(fig, use_container_width=True)

elif (option=='NASIONAL' and option2=='TPS'):
    tps = df.groupby('tps_id')[['provinsi']].count().sort_values(by=['provinsi'],ascending=[False]).reset_index()
    fig = px.bar(tps, x='tps_id', y='provinsi', height=600, title=('Sebaran Data TPS di '+option))
    fig.layout.update(xaxis_title="Total", yaxis_title="Kabupaten")
    st.plotly_chart(fig, use_container_width=True)

elif (option!='NASIONAL' and option2=='TPS'):
    tps = df[df.provinsi == option].groupby('tps_id').count().sort_values(by=['provinsi'],ascending=[False]).reset_index() 
    fig = px.bar(tps, x='tps_id', y='no_nik', height=600, title=('Sebaran Data TPS di '+option), text_auto='.2s')
    fig.layout.update(xaxis_title="Total", yaxis_title="Provinsi")
    st.plotly_chart(fig, use_container_width=True)

elif (option=='NASIONAL' and option2=='Disabilitas'):
    labels = df['disabilitas'].value_counts().index
    values = df['disabilitas'].value_counts().values

    # modeAmount = df.groupby('jns_kelamin')[['no_nik']].count().sort_values(by=['no_nik'],ascending=[True]).tail(10).reset_index()
    # fig = px.bar(modeAmount, x='no_nik', y='jns_kelamin', height=600, title='Sebaran Tempat Lahir')
    # fig.layout.update(xaxis_title="Total", yaxis_title="Tempat Lahir")
    fig = px.pie(df, values=values, names=labels, title=('Sebaran Data Disabilitas di ' + option))
    st.plotly_chart(fig, use_container_width=True)

elif (option!='NASIONAL' and option2=='Disabilitas'):
    labels = df[df['provinsi']==option]['disabilitas'].value_counts().index
    values = df[df['provinsi']==option]['disabilitas'].value_counts().values

    fig = px.pie(df, values=values, names=labels, title=('Sebaran Data Disabilitas di ' + option))
    st.plotly_chart(fig, use_container_width=True)
    
st.markdown(hide_menu, unsafe_allow_html=True)