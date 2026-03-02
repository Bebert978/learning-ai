# Task Generator — Lonely Octopus Week 1

Agent IA qui transforme un objectif en liste de tâches concrètes avec des délais.

## Ce que ça fait

Tu donnes un objectif → l'agent le découpe en étapes actionnables.

Exemple :
- **Input** : "Apprendre Python en 2 semaines"
- **Output** : Une liste numérotée de tâches avec des délais estimés

## Installation

```bash
# 1. Activer l'environnement virtuel
# Windows :
venv\Scripts\activate
# Mac/Linux :
source venv/bin/activate

# 2. Installer les dépendances
pip install streamlit python-dotenv openai openai-agents

# 3. Ajouter ta clé API OpenAI dans le fichier .env
# Ouvre .env et colle ta clé après OPENAI_API_KEY=
```

## Utilisation

### Interface web (Streamlit)
```bash
streamlit run app.py
```
→ Ouvre ton navigateur, tape un objectif, clique "Générer".

### En ligne de commande
```bash
python main.py
```
→ Lance un test rapide avec un objectif par défaut.

## Structure du projet

```
lo-week1-task-generator/
├── venv/           # Environnement virtuel Python
├── .env            # Clé API OpenAI (à remplir)
├── main.py         # L'agent Task Generator
├── app.py          # Interface Streamlit
└── README.md       # Ce fichier
```

## Stack

- **OpenAI Agents SDK** — pour créer l'agent
- **Streamlit** — pour l'interface web
- **python-dotenv** — pour charger la clé API depuis .env
