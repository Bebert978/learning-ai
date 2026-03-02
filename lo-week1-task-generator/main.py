"""
Agent "Task Generator" — Transforme un objectif en liste de tâches concrètes.
Utilise le OpenAI Agents SDK.
"""

import os
from dotenv import load_dotenv
from agents import Agent, Runner

# Charger les variables d'environnement (.env)
load_dotenv()

# Instructions système de l'agent
INSTRUCTIONS = """Tu es "Task Generator", un assistant spécialisé dans la planification.

Ton UNIQUE rôle :
- Recevoir un objectif de l'utilisateur
- Le découper en tâches concrètes et actionnables
- Donner des délais estimés quand c'est possible
- Numéroter chaque tâche clairement

Règles strictes :
- Réponds UNIQUEMENT en français
- Ne réponds JAMAIS à des questions hors sujet (politique, météo, blagues, etc.)
- Si la demande n'est pas un objectif à découper, réponds :
  "Je suis un générateur de tâches. Donne-moi un objectif et je le découperai en étapes concrètes."
- Chaque tâche doit commencer par un verbe d'action
- Ajoute une estimation de temps quand c'est réaliste

Format de réponse :
1. [Tâche] — [Délai estimé]
2. [Tâche] — [Délai estimé]
...
"""

# Création de l'agent
task_agent = Agent(
    name="Task Generator",
    instructions=INSTRUCTIONS,
)


async def generer_taches(objectif: str) -> str:
    """
    Envoie un objectif à l'agent et retourne la liste de tâches.
    """
    result = await Runner.run(task_agent, objectif)
    return result.final_output


# Test rapide si on lance directement ce fichier
if __name__ == "__main__":
    import asyncio

    objectif_test = "Apprendre les bases de Python en 2 semaines"
    print(f"Objectif : {objectif_test}\n")

    reponse = asyncio.run(generer_taches(objectif_test))
    print(reponse)
