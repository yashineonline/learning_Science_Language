# generate_lessons.py

"""
This script uses OpenAI (or other LLM APIs) to generate multilingual, topic-based
language learning lessons from real-life examples.
Each lesson includes:
- 1-2 line scenario sentences in Spanish, Portuguese, French, Italian
- English translation
- Optional expandable metadata (grammar, word focus, pronunciation, science concept)

Free version: Use mock responses or GPT-4o-mini via UI/API.
"""

import os
import json
import random
from datetime import datetime

# Optional: If you want to call OpenAI, uncomment this
# import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")

LANGS = ["Spanish", "Portuguese", "French", "Italian"]

TOPICS = {
    "driving": "A car brakes suddenly on a wet road.",
    "digestion": "Someone eats fruit before rice to feel lighter after a meal.",
    "cleaning": "You place heavy dishes carefully to avoid breaking them.",
    "helping": "You smile at a stranger and feel better inside.",
    "daily_habits": "You drink water slowly instead of gulping it."
}

# Mock LLM function (replace with real LLM call later)
def generate_lesson(topic, scenario):
    base_text = {
        "Spanish": "", "Portuguese": "", "French": "", "Italian": ""
    }

    # Pretend LLM output
    if topic == "driving":
        base_text = {
            "Spanish": "El coche tardó más en frenar porque la carretera estaba mojada.",
            "Portuguese": "O carro demorou mais para parar porque a estrada estava molhada.",
            "French": "La voiture a mis plus de temps à s’arrêter parce que la route était mouillée.",
            "Italian": "L’auto ha impiegato più tempo a fermarsi porque la strada era bagnata."
        }

    explanation = (
        "All sentences describe how wet roads make stopping slower. You’ll notice: reflexive verbs (e.g., 's’arrêter'), "
        "past tense structures, and the common word for 'wet road'."
    )

    return {
        "topic": topic,
        "scenario": scenario,
        "datetime": datetime.utcnow().isoformat(),
        "sentences": base_text,
        "english": "The car took longer to stop because the road was wet.",
        "notes": {
            "grammar_focus": "Past tense, reflexive verbs",
            "vocab_highlight": ["frenar", "parar", "s’arrêter", "fermarsi"],
            "science_link": "Heavier objects take longer to stop."
        }
    }

def save_lesson(lesson):
    folder = f"content/{lesson['topic']}"
    os.makedirs(folder, exist_ok=True)
    
    filename = os.path.join(folder, "lesson.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(lesson, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved lesson to {filename}")

def main():
    for topic, scenario in TOPICS.items():
        lesson = generate_lesson(topic, scenario)
        save_lesson(lesson)

if __name__ == "__main__":
    main()


# Define some initial lesson themes and example data
lessons = [
    {
        "topic": "driving",
        "examples": [
            {
                "sentence_en": "I am driving to the city.",
                "sentence_fr": "Je conduis vers la ville.",
                "sentence_es": "Estoy conduciendo a la ciudad.",
                "sentence_pt": "Estou dirigindo para a cidade.",
                "verb_root": "to drive / conduire / conducir / dirigir",
                "structure_notes": "Present continuous in ES/PT uses 'estar' + gerund; FR uses simple present.",
                "pronunciation": {
                    "fr": "con-du-ee",
                    "es": "con-doo-thee-en-do (Spain) / con-doo-see-en-do (LatAm)",
                    "pt": "djee-ree-zhen-doo"
                }
            }
        ]
    },
    {
        "topic": "digestion",
        "examples": [
            {
                "sentence_en": "Digestion starts in the mouth.",
                "sentence_fr": "La digestion commence dans la bouche.",
                "sentence_es": "La digestión comienza en la boca.",
                "sentence_pt": "A digestão começa na boca.",
                "verb_root": "to start / commencer / comenzar / começar",
                "structure_notes": "All use simple present. Gender of nouns differs across languages.",
                "pronunciation": {
                    "fr": "dee-zhe-styon",
                    "es": "dee-hes-tyon",
                    "pt": "djee-zhe-stão"
                }
            }
        ]
    },
    {
        "topic": "emotion",
        "examples": [
            {
                "sentence_en": "I feel happy today.",
                "sentence_fr": "Je me sens heureux aujourd’hui.",
                "sentence_es": "Me siento feliz hoy.",
                "sentence_pt": "Eu me sinto feliz hoje.",
                "verb_root": "to feel / se sentir / sentirse / sentir-se",
                "structure_notes": "Reflexive verbs in FR/ES/PT; EN does not use reflexive for 'feel'.",
                "pronunciation": {
                    "fr": "zhe muh sahn",
                    "es": "meh syen-to",
                    "pt": "ay-oo mee seen-too"
                }
            }
        ]
    }
]

# Create content folders and JSON lesson files
base_path = "/mnt/data/content"
os.makedirs(base_path, exist_ok=True)

for lesson in lessons:
    topic = lesson["topic"]
    os.makedirs(os.path.join(base_path, topic), exist_ok=True)
    with open(os.path.join(base_path, topic, "lesson.json"), "w", encoding="utf-8") as f:
        json.dump(lesson, f, ensure_ascii=False, indent=2)

os.listdir(base_path)  # Confirm created folders










