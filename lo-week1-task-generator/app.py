"""
Interface Streamlit pour le Task Generator.
Lance avec : streamlit run app.py
"""

import asyncio
import os
import streamlit as st
from dotenv import load_dotenv
from main import generer_taches

# Charger les variables d'environnement
load_dotenv()

# --- Configuration de la page ---
st.set_page_config(page_title="Task Generator", page_icon="✅")
st.title("✅ Task Generator")
st.markdown("*Donne-moi un objectif, je le découpe en tâches concrètes.*")

# --- Vérifier que la clé API est configurée ---
if not os.getenv("OPENAI_API_KEY"):
    st.info(
        "🔑 Clé API manquante ! Crée un fichier `.env` à la racine du projet "
        "avec : `OPENAI_API_KEY=ta-clé-ici`"
    )
    st.stop()  # Arrête l'app ici, pas besoin d'aller plus loin

# --- Champ de saisie ---
objectif = st.text_area(
    "Ton objectif :",
    placeholder="Ex : Lancer une boutique en ligne en 1 mois",
    height=100,
)

# --- Bouton de génération ---
if st.button("Générer les tâches", type="primary"):
    if not objectif.strip():
        st.warning("Écris un objectif d'abord !")
    else:
        with st.spinner("L'agent réfléchit..."):
            try:
                resultat = asyncio.run(generer_taches(objectif))
            except Exception as e:
                # Message orange discret au lieu du gros traceback rouge
                st.warning(f"Oups, l'API a renvoyé une erreur : {e}")
                st.stop()

        st.subheader("📋 Tes tâches :")
        st.markdown(resultat)
