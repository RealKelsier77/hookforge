import streamlit as st
import random
import io

# Streamlit page configuration
st.set_page_config(page_title="HookForge", page_icon="🎥", layout="wide")

# Initialize session state for theme
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Custom CSS for light and dark themes
def get_theme_css():
    if st.session_state.theme == "dark":
        return """
        <style>
        .main { background-color: #1e1e1e; color: #ffffff; }
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
            background-color: #2a2a2a;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            margin-bottom: 10px;
        }
        .hook-title { color: #ffffff; font-size: 18px; font-weight: bold; }
        .idea-card {
            background-color: #2a2a2a;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            margin-bottom: 10px;
        }
        .sidebar .sidebar-content { background-color: #2a2a2a; }
        </style>
        """
    else:
        return """
        <style>
        .main { background-color: #f5f5f5; color: #333333; }
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
        .idea-card {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 10px;
        }
        .sidebar .sidebar-content { background-color: #ffffff; }
        </style>
        """

st.markdown(get_theme_css(), unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.header("HookForge Settings")
    st.image("https://i.imgur.com/0nKz4lE.png", caption="HookForge Logo")  # Free-hosted image
    language = st.selectbox("Language", ["English", "Spanish", "French", "German", "Italian", "Portuguese"])
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
    # Theme toggle
    theme = st.selectbox("Theme", ["Light", "Dark"], index=0 if st.session_state.theme == "light" else 1)
    if theme.lower() != st.session_state.theme:
        st.session_state.theme = theme.lower()
        st.experimental_rerun()

# Main content
st.title("🎥 HookForge: Viral YouTube Hook Generator")
st.markdown("Generate **10 viral hooks** and **3 video ideas** for your YouTube videos! Choose your language, niche, tone, and video type, then hit **Generate Hooks**.")

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
    },
    "Italian": {
        "Exciting": [
            "Non crederai a questo {keyword} che cambierà il tuo gioco in {niche}!",
            "Questo {video_type} rivela il {keyword} di cui tutti parlano!",
            "Preparati per un {keyword} in {niche} che DEVI conoscere!",
            "Il {keyword} che sta conquistando {niche}!"
        ],
        "Suspenseful": [
            "E se {keyword} potesse rovinare il tuo {niche} per sempre?",
            "Il {keyword} dietro questo {video_type} ti sconvolgerà!",
            "Questo segreto di {niche} su {keyword} cambia tutto...",
            "Questo {keyword} è la fine di {niche} come lo conosciamo?"
        ],
        "Relatable": [
            "In difficoltà con {niche}? Questo {keyword} è per TE!",
            "Ho provato {keyword} nel mio {video_type} ed era così reale!",
            "Ogni fan di {niche} si riconoscerà in questo {keyword}!",
            "Questo {keyword} è il motivo per cui amo {niche}!"
        ],
        "Controversial": [
            "È {keyword} la più grande bugia in {niche}?",
            "Questo {video_type} espone il {keyword} di cui nessuno parla!",
            "Perché {keyword} sta dividendo la comunità di {niche}!",
            "La verità su {keyword} che {niche} non vuole che tu sappia!"
        ],
        "Funny": [
            "Ho provato {keyword} in {niche} ed è stato ESILARANTE!",
            "Questo {video_type} su {keyword} ti farà ridere a crepapelle!",
            "Chi avrebbe mai pensato che {niche} potesse essere così {keyword} divertente?",
            "Il fallimento di {keyword} che ha spaccato internet!"
        ],
        "Dramatic": [
            "Il {keyword} che ha distrutto il mio percorso in {niche}!",
            "Questo {video_type} scopre un {keyword} che non puoi ignorare!",
            "Come {keyword} ha capovolto il mio {niche}!",
            "Il {keyword} che ha cambiato {niche} per sempre!"
        ]
    },
    "Portuguese": {
        "Exciting": [
            "Você não vai acreditar neste {keyword} que vai mudar seu jogo em {niche}!",
            "Este {video_type} revela o {keyword} que todos estão falando!",
            "Prepare-se para um {keyword} em {niche} que você PRECISA conhecer!",
            "O {keyword} que está tomando {niche} de assalto!"
        ],
        "Suspenseful": [
            "E se {keyword} pudesse arruinar seu {niche} para sempre?",
            "O {keyword} por trás deste {video_type} vai te chocar!",
            "Este segredo de {niche} sobre {keyword} muda tudo...",
            "Este {keyword} é o fim de {niche} como conhecemos?"
        ],
        "Relatable": [
            "Com dificuldades em {niche}? Este {keyword} é para VOCÊ!",
            "Eu tentei {keyword} no meu {video_type} e pareceu tão real!",
            "Todo fã de {niche} vai se identificar com este {keyword}!",
            "Este {keyword} é por que eu amo {niche}!"
        ],
        "Controversial": [
            "É {keyword} a maior mentira em {niche}?",
            "Este {video_type} expõe o {keyword} que ninguém fala!",
            "Por que {keyword} está dividindo a comunidade de {niche}!",
            "A verdade sobre {keyword} que {niche} não quer que você saiba!"
        ],
        "Funny": [
            "Eu tentei {keyword} em {niche} e foi HILÁRIO!",
            "Este {video_type} sobre {keyword} vai te fazer rir muito!",
            "Quem diria que {niche} poderia ser tão {keyword} engraçado?",
            "A falha de {keyword} que quebrou a internet!"
        ],
        "Dramatic": [
            "O {keyword} que destruiu minha jornada em {niche}!",
            "Este {video_type} descobre um {keyword} que você não pode ignorar!",
            "Como {keyword} virou meu {niche} de cabeça para baixo!",
            "O {keyword} que mudou {niche} para sempre!"
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
    },
    "Italian": {
        "Finance": ["trucco per milioni", "hack di investimento", "errore finanziario", "lavoretto extra", "trappola di debiti"],
        "Fitness": ["segreto di allenamento", "hack di dieta", "mito muscolare", "trucco cardio", "fallimento fitness"],
        "Gaming": ["consiglio pro", "codice cheat", "glitch di gioco", "fallimento epico", "uovo di Pasqua"],
        "Tech": ["hack di gadget", "segreto di app", "mito tecnologico", "trucco di IA", "fallimento di dispositivo"],
        "Motivation": ["cambio di mentalità", "segreto di successo", "hack di vita", "trucco di obiettivi", "spinta ispiratrice"],
        "Self-Improvement": ["hack di abitudini", "consiglio di produttività", "mito di mentalità", "segreto di crescita", "fallimento di autocura"],
        "Education": ["hack di studio", "trucco di apprendimento", "segreto di esami", "mito della conoscenza", "fallimento scolastico"],
        "Vlogs": ["hack quotidiano", "momento di vita", "segreto di vlog", "consiglio di viaggio", "fallimento di routine"],
        "Reactions": ["momento virale", "fattore shock", "segreto di meme", "hack di tendenza", "fallimento di reazione"],
        "True Crime": ["segreto del caso", "hack di mistero", "mito criminale", "rivelazione di colpo di scena", "fallimento di sospetto"],
        "Cooking": ["hack di ricetta", "consiglio di cucina", "fallimento in cucina", "segreto di sapore", "trucco di pasto"],
        "Travel": ["hack di destinazione", "consiglio di viaggio", "segreto di budget", "fallimento di avventura", "trucco culturale"],
        "Beauty": ["hack di trucco", "segreto di cura della pelle", "mito di bellezza", "trucco di stile", "fallimento di glamour"],
        "DIY": ["hack di artigianato", "consiglio di progetto", "fallimento di fai-da-te", "segreto di riciclo", "trucco di costruzione"],
        "Parenting": ["hack di genitorialità", "consiglio per bambini", "segreto familiare", "trucco per piccoli", "fallimento di mamma"]
    },
    "Portuguese": {
        "Finance": ["truque para milhões", "hack de investimento", "erro financeiro", "renda extra", "armadilha de dívidas"],
        "Fitness": ["segredo de treino", "hack de dieta", "mito muscular", "truque de cardio", "falha de fitness"],
        "Gaming": ["dica pro", "código de trapaça", "falha do jogo", "fracasso épico", "ovo de Páscoa"],
        "Tech": ["hack de gadget", "segredo de aplicativo", "mito tecnológico", "truque de IA", "falha de dispositivo"],
        "Motivation": ["mudança de mentalidade", "segredo de sucesso", "hack de vida", "truque de metas", "impulso inspirador"],
        "Self-Improvement": ["hack de hábitos", "dica de produtividade", "mito de mentalidade", "segredo de crescimento", "falha de autocuidado"],
        "Education": ["hack de estudo", "truque de aprendizado", "segredo de exames", "mito do conhecimento", "falha escolar"],
        "Vlogs": ["hack diário", "momento de vida", "segredo de vlog", "dica de viagem", "falha de rotina"],
        "Reactions": ["momento viral", "fator de choque", "segredo de meme", "hack de tendência", "falha de reação"],
        "True Crime": ["segredo do caso", "hack de mistério", "mito criminal", "revelação de reviravolta", "falha de suspeito"],
        "Cooking": ["hack de receita", "dica de cozinha", "falha na cozinha", "segredo de sabor", "truque de refeição"],
        "Travel": ["hack de destino", "dica de viagem", "segredo de orçamento", "falha de aventura", "truque cultural"],
        "Beauty": ["hack de maquiagem", "segredo de cuidados com a pele", "mito de beleza", "truque de estilo", "falha de glamour"],
        "DIY": ["hack de artesanato", "dica de projeto", "falha de faça-você-mesmo", "segredo de reciclagem", "truque de construção"],
        "Parenting": ["hack de parentalidade", "dica para crianças", "segredo familiar", "truque para bebês", "falha de mãe"]
    }
}

# Video idea templates
video_idea_templates = {
    "Tutorial": [
        "Teach viewers how to master {keyword} in {niche} with a step-by-step guide.",
        "Create a {tone} tutorial on using {keyword} to improve your {niche} skills.",
        "Show beginners how to get started with {keyword} in {niche}."
    ],
    "Listicle": [
        "Rank the top 5 {keyword} tips for {niche} in a {tone} list.",
        "Compile a {tone} list of the best {keyword} hacks for {niche} fans.",
        "Share a {tone} countdown of {keyword} mistakes to avoid in {niche}."
    ],
    "Storytelling": [
        "Tell a {tone} story about how {keyword} transformed your {niche} journey.",
        "Share a personal {tone} tale of overcoming {keyword} challenges in {niche}.",
        "Craft a {tone} narrative around a {keyword} moment in {niche}."
    ],
    "Commentary": [
        "Give a {tone} take on the latest {keyword} trends in {niche}.",
        "Analyze the impact of {keyword} on {niche} with a {tone} perspective.",
        "Discuss why {keyword} is shaking up {niche} in a {tone} commentary."
    ],
    "Day in the Life": [
        "Show a {tone} day incorporating {keyword} into your {niche} routine.",
        "Document how {keyword} shapes a {tone} day in {niche}.",
        "Create a {tone} vlog of using {keyword} in your {niche} lifestyle."
    ],
    "Challenge": [
        "Take on a {tone} {keyword} challenge in {niche} and share the results.",
        "Try a {tone} 30-day {keyword} challenge for {niche}.",
        "Invite viewers to join a {tone} {keyword} challenge in {niche}."
    ],
    "Podcast Clip": [
        "Share a {tone} podcast clip discussing {keyword} in {niche}.",
        "Highlight a {tone} conversation about {keyword} from your {niche} podcast.",
        "Extract a {tone} moment about {keyword} from a {niche} podcast episode."
    ],
    "Review": [
        "Review a {keyword} product or tool for {niche} with a {tone} perspective.",
        "Test and share a {tone} review of {keyword} in {niche}.",
        "Compare {keyword} options for {niche} in a {tone} review."
    ],
    "Interview": [
        "Interview a {niche} expert on {keyword} with a {tone} approach.",
        "Host a {tone} chat with a {niche} pro about {keyword}.",
        "Ask a {niche} influencer about their {keyword} experience in a {tone} interview."
    ],
    "Q&A": [
        "Answer viewer questions about {keyword} in {niche} with a {tone} vibe.",
        "Host a {tone} Q&A session on {keyword} for {niche} fans.",
        "Tackle common {keyword} queries in {niche} with a {tone} Q&A."
    ],
    "Unboxing": [
        "Unbox a {keyword} product for {niche} with a {tone} reaction.",
        "Showcase a {tone} unboxing of a {keyword} item in {niche}.",
        "Reveal a {keyword} package for {niche} in a {tone} unboxing video."
    ]
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

# Function to generate video ideas
def generate_video_ideas(niche, tone, video_type):
    templates = video_idea_templates.get(video_type, video_idea_templates["Tutorial"])
    keywords = keywords_by_niche.get("English", {}).get(niche, keywords_by_niche["English"]["Motivation"])  # Use English for ideas
    ideas = []
    for _ in range(3):  # Generate 3 ideas
        template = random.choice(templates)
        keyword = random.choice(keywords)
        idea = template.format(keyword=keyword, niche=niche.lower(), tone=tone.lower())
        ideas.append(idea)
    return ideas

# Generate hooks and ideas button
if st.button("Generate Hooks & Ideas"):
    hooks = generate_hooks(language, niche, tone, video_type)
    ideas = generate_video_ideas(niche, tone, video_type)
    
    # Display hooks
    st.subheader("Your Viral Hooks")
    hook_text = ""
    for i, hook in enumerate(hooks, 1):
        hook_text += f"Hook {i}: {hook}\n"
        with st.container():
            st.markdown(f"<div class='hook-card'><p class='hook-title'>Hook {i}</p>{hook}</div>", unsafe_allow_html=True)
            col1, col2 = st.columns([3, 1])
            with col1:
                st.code(hook, language="text")  # Copyable text block
            with col2:
                # JavaScript for copying text
                st.markdown(f"""
                    <button onclick="navigator.clipboard.writeText('{hook}')">Copy Hook</button>
                    <script>
                    document.querySelectorAll('button').forEach(button => {{
                        button.addEventListener('click', () => {{
                            navigator.clipboard.writeText(button.innerText.replace('Copy Hook', '{hook}'));
                            button.innerText = 'Copied!';
                            setTimeout(() => {{ button.innerText = 'Copy Hook'; }}, 2000);
                        }});
                    }});
                    </script>
                """, unsafe_allow_html=True)
    
    # Download hooks button
    st.download_button(
        label="Download Hooks",
        data=hook_text,
        file_name="hookforge_hooks.txt",
        mime="text/plain"
    )
    
    # Display video ideas
    st.subheader("Video Ideas")
    for i, idea in enumerate(ideas, 1):
        with st.container():
            st.markdown(f"<div class='idea-card'><p class='hook-title'>Idea {i}</p>{idea}</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by HookForge | Powered by [Streamlit](https://streamlit.io)", unsafe_allow_html=True)
