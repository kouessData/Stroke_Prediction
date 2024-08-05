#1 IMPORTATION DES LIBRAIRIES

import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl

#2 DESCRIPTION DU PROJET
st.title(" PREDICTION SUR LES ACCIDENTS CARDIO VASCULAIRES")
st.write(" DESCRIPTION DU JEUX DE DONNEES : Selon l'Organisation mondiale de la santé (OMS), l'accident cardio vasculaire cérébral est la deuxième cause de décès dans le monde, responsable d'environ 11 du total des décès. \n Cet ensemble de données fournit des informations pertinentes sur le patient  en fonction de paramètres d'entrée tels que le sexe, l'âge, diverses maladies et le statut tabagique.\n OBJECTIF : L'objectif de notre analyse sera de prédire si un patient est susceptible de subir un accident vasculaire cérébral.")
#SIDEBAR
st.sidebar.markdown("### Réalisé par: KOUASSI N'DOUA CAMILLE ESTHER ")

st.sidebar.image('C:/Users/HP/Desktop/Projet/Accident_cardio_vasculaire/Diabetes Self-Management.jpeg')
st.sidebar.subheader(" Ce modèle prédictif peut détecter à 75% qu'un patient ne risque pas d'avoir d'accident cardio vasculaire")

#3 CHARGEMENT DU MODELE
file = open("model_accident_Vasculaire.pkl","rb")
model = pkl.load(file)
file.close()

files = open("scaler_vas.pkl","rb")
scaler = pkl.load(files)
files.close()


#4 DEFINITION DE LA FONCTION D'INTERFERENCE(PERMET DE FAIRE LA PREDICTION)

def interference(age,avg_glucose_level,bmi,smoking_status_neversmoked,smoking_status_Unknown,smoking_status_formerlysmoked,smoking_status_smokes) :
    
    if model is not None:
        df = np.array([age, avg_glucose_level, bmi, smoking_status_neversmoked, smoking_status_Unknown, smoking_status_formerlysmoked, smoking_status_smokes])
        df = pd.DataFrame([[age, avg_glucose_level, bmi, smoking_status_neversmoked, smoking_status_Unknown, smoking_status_formerlysmoked, smoking_status_smokes]],columns=["age", "avg_glucose_level", "bmi", "smoking_status_never smoked", "smoking_status_Unknown", "smoking_status_formerly smoked", "smoking_status_smokes"])
        try:
            
#.reshape(1, -1)
            pred = model.predict(df)
            return pred
        except AttributeError as e:
            st.error(f"Erreur de prédiction: {e}")
            return None
    else:
        st.error("Modèle non chargé correctement.")
        return None
    
#5 SAISIE DES INFORMATIONS DU CLIENT

    

st.write('Entrez les informations du patient')


age = st.number_input(label="AGE")

avg_glucose_level = st.number_input(label="TAUX DE GLUCOSE")

bmi =st.number_input(label="MASSE CORPORELLE")



check = ["Ancien fumeur","***jamais fumé***","fumeur"]

selected_option = st.radio("Etes-vous fumeur?", check,index=None)

if selected_option == "Ancien fumeur":
    
    smoking_status_formerlysmoked = 1
    smoking_status_neversmoked = 0
    smoking_status_Unknown =0
    smoking_status_smokes = 0 

elif selected_option == "***jamais fumé***":

    
    smoking_status_neversmoked = 1
    smoking_status_formerlysmoked = 0
    smoking_status_Unknown =0
    smoking_status_smokes = 0

elif selected_option == "fumeur" :
    smoking_status_smokes = 1
    smoking_status_formerlysmoked = 0
    smoking_status_neversmoked = 0
    smoking_status_Unknown =0
else :

    smoking_status_Unknown = 1
    smoking_status_formerlysmoked = 0
    smoking_status_neversmoked = 0
    smoking_status_smokes = 0



#6 CREATION DU BOUTON DE PREDICTION

if st.button('predict'):
    result_pred = interference(age,avg_glucose_level,bmi,smoking_status_neversmoked,smoking_status_Unknown,smoking_status_formerlysmoked,smoking_status_smokes)
    if result_pred[0]==0:
        st.success("Vous ne risquez pas d'avoir un accident cardio vasculaire ",icon="✅")
        

    elif result_pred[0]==1:
        st.warning("Malheureusement vous êtes susceptible d'avoir un accident cardio vasculaire ",icon="🔥")
        

