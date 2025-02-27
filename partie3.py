import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Géré automatiquement
            'logged_in': False,  # Géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Géré automatiquement
            'logged_in': False,  # Géré automatiquement
            'role': 'administrateur'
        }
    }
}

# Authentification
authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie_name",         # Le nom du cookie (un nom quelconque)
    "cookie_key",          # La clé du cookie (un clé quelconque)
    30,                    # Le nombre de jours avant que le cookie expire
)

# Connexion sans spécifier location
auth_status = authenticator.login("Login", "Mot de passe")

# Fonction d'accueil
def accueil():
    st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")

# Si l'utilisateur est authentifié
if auth_status:
    # Afficher la page d'accueil après la connexion
    accueil()

    # Création du menu qui va afficher les choix
    selection = option_menu(
        menu_title=None,
        options=["Accueil", "Photos"]
    )

    # Afficher le contenu de chaque page selon la sélection
    if selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil !")
    elif selection == "Photos":
        st.write("Bienvenue sur mon album photo")
    
    # Bouton de déconnexion
    authenticator.logout("Déconnexion")

# Si l'utilisateur n'est pas authentifié
elif auth_status is False:
    st.error("Le nom d'utilisateur ou le mot de passe est incorrect.")

# Si l'utilisateur n'a pas encore rempli les champs
elif auth_status is None:
    st.warning("Les champs 'nom d'utilisateur' et 'mot de passe' doivent être remplis")
