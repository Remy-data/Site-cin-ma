import streamlit as st
import pandas as pd

# Charger les données (assurez-vous que le chemin du fichier est correct)
df = pd.read_csv("C:/Users/devea/Downloads/table_globale.csv")

st.markdown("""
    <style>
        .stApp {
            background-image: url("https://img.freepik.com/free-vector/cinematography-banner-with-film-tape-strip-roll_107791-30373.jpg");
            background-size: cover;  /* L'image couvre toute la surface sans pixellisation */
            background-position: center center;  /* L'image est centrée */
            background-attachment: fixed;  /* L'image reste fixe lors du défilement */
            background-repeat: no-repeat;  /* L'image ne se répète pas */
            color: white;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
        /* Changer l'arrière-plan de la sidebar */
        .css-1d391kg {
            background-color: # FF00FF; /* Couleur de fond de la sidebar */
            color: white; /* Couleur du texte */
        } </style>
""", unsafe_allow_html=True)

# --- Menu latéral pour saisir le nom du film ---
st.sidebar.title("Rechercher un film 🍿")
films = df['originalTitle']
film_input = st.sidebar.selectbox('Entrez le nom du film',(films),index=0 )



# --- Affichage du Top 10 films par note pondérée ---
top_films = df.sort_values(by='note_ponderee', ascending=False).head(10)

base_url = "https://image.tmdb.org/t/p/w500"

# Affichage du top 10 dans le contenu principal
st.title("Top 10 des films les plus populaire")
for index, row in top_films.iterrows():
    image_url = base_url + row['poster_path'] 
    st.subheader(f"{row['originalTitle']}")
    st.image(image_url, width=100)
    st.write(f"**Note Pondérée:** {round(row['note_ponderee'], 2)}")
    st.write(f"**Genre(s):** {row['genres_x']}")
    st.write(f"**Durée:** {row['runtimeMinutes']} min")
    st.write(f"**Synopsis:** {row['overview']}")
    st.write("---")

# --- Affichage des recommandations (au moment où tu auras intégré le modèle ML) ---
if film_input:
    # Ici, tu utiliseras ton modèle de ML pour générer des recommandations
    st.subheader(f"Recommandations pour : {film_input}")
    
    # Exemple de ce que tu peux faire pour afficher des recommandations (à remplacer par ton modèle ML)
    # Ici, on filtre les films dont le titre contient la recherche de l'utilisateur.
    film_input_lower = film_input.lower()
    recommendations = df[df['originalTitle'].str.contains(film_input_lower, case=False)].head(5)
    
    if not recommendations.empty:
        for index, row in recommendations.iterrows():
            image_url = base_url + row['poster_path'] 
            st.write(f"🎥 **{row['originalTitle']}**")
            st.image(image_url, width=100)
            st.write(f"**Genre(s):** {row['genres_x']}")
            st.write(f"**Synopsis:** {row['overview']}")
            st.write(f"**Note Pondérée:** {round(row['note_ponderee'], 2)}")
            st.write("---")
    else:
        st.write("Désolé, aucun film trouvé pour cette recherche.")
