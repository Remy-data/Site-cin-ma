import streamlit as st
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
# importer les dataset disponible sur seaborn
datasets = sns.get_dataset_names()
st.title("Manipulation de données et création de graphiques")
# choix du dataset a utiliser
select_dataset = st.selectbox("Quel dataset veux-tu utiliser ?", datasets)
# charger les donnée
df = sns.load_dataset(select_dataset)
# afficher le dataset 
st.dataframe(df) 

x_column = st.selectbox("Choisissez la colonne X",df.columns )
y_column = st.selectbox("Choisissez la colonne Y",df.columns )

graphique = st.selectbox(" Quel graphique veux-tu utiliser ?", 
                     ["scatter_chart", "bar_chart", "line_chart"])
st.subheader(f"votre graphique :{graphique}")
if graphique == "scatter_chart":
    st.scatter_chart(df, x=x_column,y= y_column)
elif graphique == "bar_chart":
    st.bar_chart(df, x=x_column,y= y_column)
elif graphique == "line_chart":
    st.line_chart(df, x=x_column,y= y_column)

numeric_df = df.select_dtypes(include=['number'])
if st.checkbox("Afficher la matrice de corrélation"):
    st.subheader("Matrice de corrélation")
    fig, ax = plt.subplots()
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    st.pyplot(fig)