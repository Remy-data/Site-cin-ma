import streamlit as st
import pandas as pd
st.write("Hello World")
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv'
data = pd.read_csv(url)
data2 = data['pickup_borough'].fillna('nan').unique()
st.title("Bienvenue sur le site web de Rémy")

selection = st.selectbox("Indiquez votre arrondissement de récupération ?",
data2)
st.write('___')

if selection == 'Bronx':
    st.write('Tu as choisi: le Bronx')
    st.image('https://thegoodlife.fr/wp-content/uploads/sites/2/2016/03/TGL-P-022-188-V-H-06.jpg')
elif selection == 'nan' :
    st.write('Tu as choisi: nan')
    st.image('https://st2.depositphotos.com/4242631/6430/v/450/depositphotos_64302369-stock-illustration-map-icon-with-pin-pointer.jpg')
elif selection == 'Manhattan':
    st.write('Tu as choisi: Manhattan')
    st.image('https://www.new-york.fr/f/estados-unidos/nueva-york/guia/manhattan-m.jpg')
elif selection == 'Queens':
    st.write('Tu as choisi: Queens')
    st.image('https://media.istockphoto.com/id/497096734/fr/photo/m%C3%A9tro-train-%C3%A0-grande-vitesse-sur-piste-sur%C3%A9lev%C3%A9e-dans-le-queens-%C3%A0-new-york.jpg?s=612x612&w=0&k=20&c=6-RgJCrnazCSxbSSIEh8fVKPhCrqdeExY4EmukYzUr8=')
elif selection == 'Brooklyn':
    st.write('Tu as choisi: Brooklyn')
    st.image('https://a.travel-assets.com/findyours-php/viewfinder/images/res70/252000/252364-New-York.jpg')
