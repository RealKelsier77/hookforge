import streamlit as st
import random

# Streamlit page configuration
st.set_page_config(page_title="HookForge", page_icon="🎥", layout="wide")

# Custom CSS for enhanced UI
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #e04343;
    }
    .hook-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    .hook-title { color: #333; font-size: 18px; font-weight: bold; }
    .copy-code { background-color: #f0f0f0; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.header("HookForge Settings")
    st.image("https://i.imgur.com/0nKz4lE.png", caption="HookForge Logo")  # Free-hosted image
    language = st.selectbox("Language", ["English", "Spanish", "French", "German"])
    niche = st.selectbox("Niche", [
        "Finance", "Fitness", "Gaming", "Tech", "Motivation", "Self-Improvement",
        "Education", "Vlogs", "Reactions", "True Crime", "Cooking", "Travel",
        "Beauty", "DIY", "Parenting"
    ])
    tone = st.selectbox("Tone", [
        "Exciting", "Suspenseful", "Relatable", "Controversial", "Funny", "Dramatic"
    ])
    video_type = st.selectbox("Video Type", [
        "Tutorial", "Listicle", "Storytelling", "Commentary", "Day in the Life",
        "Challenge", "Podcast Clip", "Review", "Interview", "Q&A", "Unboxing"
    ])

# Main content
st.title("🎥 HookForge: Viral YouTube Hook Generator")
st.markdown("Generate **10 viral hooks** for your YouTube videos! Choose your language, niche, tone, and video type, then hit **Generate Hooks**.")

# Language-specific hook templates
hook_templates = {
    "English": {
        "Exciting": [
            "You won't believe {keyword} that will change your {niche} game!",
            "This {video_type} reveals the {keyword} everyone’s talking about!",
            "Get ready for a {niche} {keyword} you NEED to know!",
            "The {keyword} that’s taking {niche} by storm!"
        ],
        "Suspenseful": [
            "What if {keyword} could ruin your {niche} forever?",
            "The {keyword} behind this {video_type} will shock you!",
            "This {niche} secret about {keyword} changes everything...",
            "Is this {keyword} the end of {niche} as we know it?"
        ],
        "Relatable": [
            "Struggling with {niche}? This {keyword} is for YOU!",
            "I tried {keyword} in my {video_type} and it felt so real!",
            "Every {niche} fan will relate to this {keyword}!",
            "This {keyword} is why I love {niche}!"
        ],
        "Controversial": [
            "Is {keyword} the biggest lie in {niche}?",
            "This {video_type} exposes the {keyword} no one talks about!",
            "Why {keyword} is dividing the {niche} community!",
            "The {keyword} truth {niche} doesn’t want you to know!"
        ],
        "Funny": [
            "I tried {keyword} in {niche} and it was HILARIOUS!",
            "This {video_type} about {keyword} will make you LOL!",
            "Who knew {niche} could be this {keyword} funny?",
            "The {keyword} fail that broke the internet!"
        ],
        "Dramatic": [
            "The {keyword} that broke my {niche} journey!",
            "This {video_type} uncovers a {keyword} you can’t ignore!",
            "How {keyword} turned my {niche} upside down!",
            "The {keyword} that changed {niche} forever!"
        ]
    },
    "Spanish": {
        "Exciting": [
            "¡No creerás este {keyword} que cambiará tu juego en {niche}!",
            "¡Este {video_type} revela el {keyword} del que todos hablan!",
            "¡Prepárate para un {keyword} en {niche} que DEBES conocer!",
            "¡El {keyword} que está revolucionando {niche}!"
        ],
        "Suspenseful": [
            "¿Y si {keyword} pudiera arruinar tu {niche} para siempre?",
            "¡El {keyword} detrás de este {video_type} te sorprenderá!",
            "Este secreto de {niche} sobre {keyword} lo cambia todo...",
            "¿Es este {keyword} el fin de {niche} como lo conocemos?"
        ],
        "Relatable": [
            "¿Luchando con {niche}? ¡Este {keyword} es para TI!",
            "¡Probé {keyword} en mi {video_type} y fue tan real!",
            "¡Todo fan de {niche} se identificará con este {keyword}!",
            "¡Este {keyword} es por qué amo {niche}!"
        ],
        "Controversial": [
            "¿Es {keyword} la mayor mentira en {niche}?",
            "¡Este {video_type} expone el {keyword} del que nadie habla!",
            "¡Por qué {keyword} está dividiendo a la comunidad de {niche}!",
            "¡La verdad sobre {keyword} que {niche} no quiere que sepas!"
        ],
        "Funny": [
            "¡Probé {keyword} en {niche} y fue HILARANTE!",
            "¡Este {video_type} sobre {keyword} te hará reír a carcajadas!",
            "¿Quién diría que {niche} podía ser tan {keyword} divertido?",
            "¡El fallo de {keyword} que rompió internet!"
        ],
        "Dramatic": [
            "¡El {keyword} que rompió mi viaje en {niche}!",
            "¡Este {video_type} descubre un {keyword} que no puedes ignorar!",
            "¡Cómo {keyword} dio un giro a mi {niche}!",
            "¡El {keyword} que cambió {niche} para siempre!"
        ]
    },
    "French": {
        "Exciting": [
            "Vous ne croirez pas ce {keyword} qui va changer votre jeu en {niche} !",
            "Ce {video_type} révèle le {keyword} dont tout le monde parle !",
            "Préparez-vous pour un {keyword} en {niche} que vous DEVEZ connaître !",
            "Le {keyword} qui secoue {niche} !"
        ],
        "Suspenseful": [
            "Et si {keyword} pouvait ruiner votre {niche} pour toujours ?",
            "Le {keyword} derrière ce {video_type} va vous choquer !",
            "Ce secret de {niche} sur {keyword} change tout...",
            "Ce {keyword} est-il la fin de {niche} tel qu’on le connaît ?"
        ],
        "Relatable": [
            "En difficulté avec {niche} ? Ce {keyword} est pour VOUS !",
            "J’ai essayé {keyword} dans mon {video_type} et c’était si réel !",
            "Tous les fans de {niche} se reconnaîtront dans ce {keyword} !",
            "Ce {keyword} est pourquoi j’aime {niche} !"
        ],
        "Controversial": [
            "Est-ce que {keyword} est le plus grand mensonge en {niche} ?",
            "Ce {video_type} expose le {keyword} dont personne ne parle !",
            "Pourquoi {keyword} divise la communauté de {niche} !",
            "La vérité sur {keyword} que {niche} ne veut pas que vous sachiez !"
        ],
        "Funny": [
            "J’ai essayé {keyword} en {niche} et c’était HILARANT !",
            "Ce {video_type} sur {keyword} va vous faire rire aux éclats !",
            "Qui aurait cru que {niche} pouvait être aussi {keyword} drôle ?",
            "L’échec de {keyword} qui a cassé internet !"
        ],
        "Dramatic": [
            "Le {keyword} qui a brisé mon parcours en {niche} !",
            "Ce {video_type} révèle un {keyword} que vous ne pouvez ignorer !",
            "Comment {keyword} a bouleversé mon {niche} !",
            "Le {keyword} qui a changé {niche} pour toujours !"
        ]
    },
    "German": {
        "Exciting": [
            "Du wirst diesen {keyword} nicht glauben, der dein {niche}-Spiel verändern wird!",
            "Dieses {video_type} enthüllt den {keyword}, über den alle reden!",
            "Mach dich bereit für einen {keyword} in {niche}, den du WISSEN MUSST!",
            "Der {keyword}, der {niche} im Sturm erobert!"
        ],
        "Suspenseful": [
            "Was, wenn {keyword} dein {niche} für immer ruinieren könnte?",
            "Der {keyword} hinter diesem {video_type} wird dich schockieren!",
            "Dieses {niche}-Geheimnis über {keyword} ändert alles...",
            "Ist dieser {keyword} das Ende von {niche}, wie wir es kennen?"
        ],
        "Relatable": [
            "Probleme mit {niche}? Dieser {keyword} ist für DICH!",
            "Ich habe {keyword} in meinem {video_type} ausprobiert und es fühlte sich so echt an!",
            "Jeder {niche}-Fan wird sich mit diesem {keyword} identifizieren!",
            "Dieser {keyword} ist, warum ich {niche} liebe!"
        ],
        "Controversial": [
            "Ist {keyword} die größte Lüge in {niche}?",
            "Dieses {video_type} enthüllt den {keyword}, über den niemand spricht!",
            "Warum {keyword} die {niche}-Community spaltet!",
            "Die Wahrheit über {keyword}, die {niche} nicht wissen will!"
        ],
        "Funny": [
            "Ich habe {keyword} in {niche} ausprobiert und es war URKOMISCH!",
            "Dieses {video_type} über {keyword} bringt dich zum Lachen!",
            "Wer hätte gedacht, dass {niche} so {keyword} lustig sein kann?",
            "Der {keyword}-Fail, der das Internet sprengte!"
        ],
        "Dramatic": [
            "Der {keyword}, der meine {niche}-Reise zerstörte!",
            "Dieses {video_type} deckt einen {keyword} auf, den du nicht ignorieren kannst!",
            "Wie {keyword} mein {niche} auf den Kopf stellte!",
            "Der {keyword}, der {niche} für immer veränderte!"
        ]
    }
}

# Language-specific keywords by niche
keywords_by_niche = {
    "English": {
        "Finance": ["trick to millions", "investment hack", "money mistake", "side hustle", "debt trap"],
        "Fitness": ["workout secret", "diet hack", "muscle myth", "cardio trick", "fitness fail"],
        "Gaming": ["pro tip", "cheat code", "game glitch", "epic fail", "hidden easter egg"],
        "Tech": ["gadget hack", "app secret", "tech myth", "AI trick", "device fail"],
        "Motivation": ["mindset shift", "success secret", "life hack", "goal trick", "inspiration boost"],
        "Self-Improvement": ["habit hack", "productivity tip", "mindset myth", "growth secret", "self-care fail"],
        "Education": ["study hack", "learning trick", "exam secret", "knowledge myth", "school fail"],
        "Vlogs": ["daily hack", "life moment", "vlog secret", "travel tip", "routine fail"],
        "Reactions": ["viral moment", "shock factor", "meme secret", "trend hack", "reaction fail"],
        "True Crime": ["case secret", "mystery hack", "crime myth", "twist reveal", "suspect fail"],
        "Cooking": ["recipe hack", "cooking tip", "kitchen fail", "flavor secret", "meal trick"],
        "Travel": ["destination hack", "travel tip", "budget secret", "adventure fail", "culture trick"],
        "Beauty": ["makeup hack", "skincare secret", "beauty myth", "style trick", "glam fail"],
        "DIY": ["craft hack", "project tip", "DIY fail", "upcycle secret", "build trick"],
        "Parenting": ["parenting hack", "kid tip", "family secret", "toddler trick", "mom fail"]
    },
    "Spanish": {
        "Finance": ["truco para millones", "hack de inversión", "error financiero", "ingreso extra", "trampa de deudas"],
        "Fitness": ["secreto de ejercicio", "hack de dieta", "mito muscular", "truco de cardio", "fallo fitness"],
        "Gaming": ["consejo pro", "código trampa", "fallo del juego", "fracaso épico", "huevo de pascua"],
        "Tech": ["hack de gadget", "secreto de app", "mito tecnológico", "truco de IA", "fallo de dispositivo"],
        "Motivation": ["cambio de mentalidad", "secreto de éxito", "hack de vida", "truco de metas", "impulso inspirador"],
        "Self-Improvement": ["hack de hábitos", "consejo de productividad", "mito de mentalidad", "secreto de crecimiento", "fallo de autocuidado"],
        "Education": ["hack de estudio", "truco de aprendizaje", "secreto de exámenes", "mito del conocimiento", "fallo escolar"],
        "Vlogs": ["hack diario", "momento de vida", "secreto de vlog", "consejo de viaje", "fallo de rutina"],
        "Reactions": ["momento viral", "factor de shock", "secreto de meme", "hack de tendencia", "fallo de reacción"],
        "True Crime": ["secreto del caso", "hack de misterio", "mito criminal", "revelación de giro", "fallo de sospechoso"],
        "Cooking": ["hack de receta", "consejo de cocina", "fallo en la cocina", "secreto de sabor", "truco de comida"],
        "Travel": ["hack de destino", "consejo de viaje", "secreto de presupuesto", "fallo de aventura", "truco cultural"],
        "Beauty": ["hack de maquillaje", "secreto de cuidado de piel", "mito de belleza", "truco de estilo", "fallo de glamour"],
        "DIY": ["hack de manualidades", "consejo de proyecto", "fallo de bricolaje", "secreto de reciclaje", "truco de construcción"],
        "Parenting": ["hack de crianza", "consejo para niños", "secreto familiar", "truco para toddlers", "fallo de mamá"]
    },
    "French": {
        "Finance": ["astuce pour millions", "hack d’investissement", "erreur financière", "revenu supplémentaire", "piège de dettes"],
        "Fitness": ["secret d’entraînement", "hack de régime", "mythe musculaire", "astuce cardio", "échec fitness"],
        "Gaming": ["astuce pro", "code de triche", "bug du jeu", "échec épique", "œuf de Pâques"],
        "Tech": ["hack de gadget", "secret d’application", "mythe technologique", "astuce d’IA", "échec de dispositif"],
        "Motivation": ["changement de mentalité", "secret de succès", "hack de vie", "astuce d’objectifs", "élan inspirant"],
        "Self-Improvement": ["hack d’habitudes", "astuce de productivité", "mythe de mentalité", "secret de croissance", "échec d’autosoins"],
        "Education": ["hack d’étude", "astuce d’apprentissage", "secret d’examens", "mythe du savoir", "échec scolaire"],
        "Vlogs": ["hack quotidien", "moment de vie", "secret de vlog", "astuce de voyage", "échec de routine"],
        "Reactions": ["moment viral", "facteur de choc", "secret de mème", "hack de tendance", "échec de réaction"],
        "True Crime": ["secret de l’affaire", "hack de mystère", "mythe criminel", "révélation de rebondissement", "échec de suspect"],
        "Cooking": ["hack de recette", "astuce de cuisine", "échec en cuisine", "secret de saveur", "astuce de repas"],
        "Travel": ["hack de destination", "astuce de voyage", "secret de budget", "échec d’aventure", "astuce culturelle"],
        "Beauty": ["hack de maquillage", "secret de soin de peau", "mythe de beauté", "astuce de style", "échec de glamour"],
        "DIY": ["hack d’artisanat", "astuce de projet", "échec de bricolage", "secret de recyclage", "astuce de construction"],
        "Parenting": ["hack de parentalité", "astuce pour enfants", "secret familial", "astuce pour tout-petits", "échec de maman"]
    },
    "German": {
        "Finance": ["Trick für Millionen", "Investment-Hack", "Finanzfehler", "Nebenverdienst", "Schuldenfalle"],
        "Fitness": ["Workout-Geheimnis", "Diät-Hack", "Muskelmythos", "Cardio-Trick", "Fitness-Fehler"],
        "Gaming": ["Pro-Tipp", "Cheat-Code", "Spiel-Glitch", "episches Versagen", "verstecktes Osterei"],
        "Tech": ["Gadget-Hack", "App-Geheimnis", "Technik-Mythos", "KI-Trick", "Gerätefehler"],
        "Motivation": ["Mentalitätswandel", "Erfolgsgeheimnis", "Lebens-Hack", "Ziel-Trick", "Inspirationsschub"],
        "Self-Improvement": ["Gewohnheits-Hack", "Produktivitätstipp", "Mentalitätsmythos", "Wachstumsgeheimnis", "Selbstpflege-Fehler"],
        "Education": ["Lern-Hack", "Lerntrick", "Prüfungsgeheimnis", "Wissensmythos", "Schulfehler"],
        "Vlogs": ["täglicher Hack", "Lebensmoment", "Vlog-Geheimnis", "Reisetipp", "Routinenfehler"],
        "Reactions": ["viraler Moment", "Schockfaktor", "Meme-Geheimnis", "Trend-Hack", "Reaktionsfehler"],
        "True Crime": ["Fallgeheimnis", "Mysterium-Hack", "Kriminalmythos", "Wendungsenthüllung", "Verdächtigenfehler"],
        "Cooking": ["Rezept-Hack", "Kochtipp", "Küchenfehler", "Geschmacksgeheimnis", "Essenstrick"],
        "Travel": ["Reiseziel-Hack", "Reisetipp", "Budgetgeheimnis", "Abenteuerfehler", "Kulturtrick"],
        "Beauty": ["Make-up-Hack", "Hautpflegegeheimnis", "Schönheitsmythos", "Stiltrick", "Glamourfehler"],
        "DIY": ["Bastel-Hack", "Projekttipp", "DIY-Fehler", "Upcycling-Geheimnis", "Baukunsttrick"],
        "Parenting": ["Eltern-Hack", "Kinder-Tipp", "Familiengeheimnis", "Kleinkind-Trick", "Mama-Fehler"]
    }
}

# Function to generate hooks
def generate_hooks(language, niche, tone, video_type):
    templates = hook_templates.get(language, {}).get(tone, hook_templates["English"]["Exciting"])
    keywords = keywords_by_niche.get(language, {}).get(niche, keywords_by_niche["English"]["Motivation"])
    hooks = []
    for _ in range(10):  # Generate 10 hooks
        template = random.choice(templates)
        keyword = random.choice(keywords)
        hook = template.format(keyword=keyword, niche=niche.lower(), video_type=video_type.lower())
        hooks.append(hook)
    return hooks

# Generate hooks button
if st.button("Generate Hooks"):
    hooks = generate_hooks(language, niche, tone, video_type)
    st.subheader("Your Viral Hooks")
    for i, hook in enumerate(hooks, 1):
        with st.container():
            st.markdown(f"<div class='hook-card'><p class='hook-title'>Hook {i}</p>{hook}</div>", unsafe_allow_html=True)
            st.code(hook, language="text")  # Copyable text block

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by HookForge | Powered by [Streamlit](https://streamlit.io)", unsafe_allow_html=True)
