import streamlit as st
import random
import io
import urllib.parse
import base64

# Streamlit page configuration
st.set_page_config(page_title="HookForge", page_icon="🎥", layout="wide")

# Initialize session state
if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "mode" not in st.session_state:
    st.session_state.mode = "YouTube"

# Base64-encoded sound effects (click and ding sounds)
click_sound_base64 = "data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YSQUAAAAAA=="  # Placeholder base64 for a click sound
ding_sound_base64 = "data:audio/wav;base64,UklGRiYAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YSYUAAAAAA=="  # Placeholder base64 for a ding sound

# Custom CSS for themes and UI enhancements
def get_theme_css():
    themes = {
        "light": """
            .main { 
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); 
                color: #333; 
                position: relative; 
                overflow: hidden; 
            }
            #particles-js { 
                position: absolute; 
                width: 100%; 
                height: 100%; 
                top: 0; 
                left: 0; 
                z-index: 0; 
            }
            .main > * { 
                position: relative; 
                z-index: 1; 
            }
            .sidebar .sidebar-content { background: #ffffff; }
            .hook-card, .idea-card {
                background: white;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 6px 12px rgba(0,0,0,0.1);
                margin-bottom: 15px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                opacity: 0;
                animation: fadeIn 0.5s forwards;
            }
            .hook-card:hover, .idea-card:hover { 
                transform: translateY(-5px); 
                box-shadow: 0 8px 20px rgba(0,0,0,0.2), 0 0 10px rgba(0,0,0,0.1); 
            }
            .stButton>button {
                background: #ff4b4b;
                color: white;
                border-radius: 10px;
                padding: 12px 24px;
                font-weight: bold;
                transition: transform 0.2s ease, background 0.2s ease;
            }
            .stButton>button:hover { 
                background: #e04343; 
                transform: scale(1.05); 
            }
            .hook-title, .idea-title { color: #333; font-size: 20px; font-weight: bold; }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
        """,
        "dark": """
            .main { 
                background: linear-gradient(135deg, #1e1e1e 0%, #434343 100%); 
                color: #fff; 
                position: relative; 
                overflow: hidden; 
            }
            #particles-js { 
                position: absolute; 
                width: 100%; 
                height: 100%; 
                top: 0; 
                left: 0; 
                z-index: 0; 
            }
            .main > * { 
                position: relative; 
                z-index: 1; 
            }
            .sidebar .sidebar-content { background: #2a2a2a; }
            .hook-card, .idea-card {
                background: #2a2a2a;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 6px 12px rgba(0,0,0,0.3);
                margin-bottom: 15px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                opacity: 0;
                animation: fadeIn 0.5s forwards;
            }
            .hook-card:hover, .idea-card:hover { 
                transform: translateY(-5px); 
                box-shadow: 0 8px 20px rgba(0,0,0,0.4), 0 0 10px rgba(0,0,0,0.2); 
            }
            .stButton>button {
                background: #ff4b4b;
                color: white;
                border-radius: 10px;
                padding: 12px 24px;
                font-weight: bold;
                transition: transform 0.2s ease, background 0.2s ease;
            }
            .stButton>button:hover { 
                background: #e04343; 
                transform: scale(1.05); 
            }
            .hook-title, .idea-title { color: #fff; font-size: 20px; font-weight: bold; }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
        """,
        "neon": """
            .main { 
                background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%); 
                color: #fff; 
                position: relative; 
                overflow: hidden; 
            }
            #particles-js { 
                position: absolute; 
                width: 100%; 
                height: 100%; 
                top: 0; 
                left: 0; 
                z-index: 0; 
            }
            .main > * { 
                position: relative; 
                z-index: 1; 
            }
            .sidebar .sidebar-content { background: #1a2a44; }
            .hook-card, .idea-card {
                background: #1a2a44;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 0 15px rgba(0,255,255,0.5);
                margin-bottom: 15px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                opacity: 0;
                animation: fadeIn 0.5s forwards;
            }
            .hook-card:hover, .idea-card:hover { 
                transform: translateY(-5px); 
                box-shadow: 0 8px 20px rgba(0,255,255,0.7), 0 0 15px rgba(0,255,255,0.3); 
            }
            .stButton>button {
                background: #00ffcc;
                color: #000;
                border-radius: 10px;
                padding: 12px 24px;
                font-weight: bold;
                transition: transform 0.2s ease, background 0.2s ease;
            }
            .stButton>button:hover { 
                background: #00ccaa; 
                transform: scale(1.05); 
            }
            .hook-title, .idea-title { color: #00ffcc; font-size: 20px; font-weight: bold; }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
        """,
        "creator": """
            .main { 
                background: linear-gradient(135deg, #ff0000 0%, #ff4b4b 50%, #000000 100%); 
                color: #fff; 
                box-shadow: inset 0 0 50px rgba(255,0,0,0.5); 
                position: relative; 
                overflow: hidden; 
            }
            #particles-js { 
                position: absolute; 
                width: 100%; 
                height: 100%; 
                top: 0; 
                left: 0; 
                z-index: 0; 
            }
            .main > * { 
                position: relative; 
                z-index: 1; 
            }
            .sidebar .sidebar-content { background: #1a1a1a; }
            .hook-card, .idea-card {
                background: #2a2a2a;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 0 20px rgba(255,0,0,0.7);
                margin-bottom: 15px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                opacity: 0;
                animation: fadeIn 0.5s forwards;
            }
            .hook-card:hover, .idea-card:hover { 
                transform: translateY(-5px); 
                box-shadow: 0 8px 20px rgba(255,0,0,0.9), 0 0 15px rgba(255,0,0,0.5); 
            }
            .stButton>button {
                background: #ff0000;
                color: white;
                border-radius: 10px;
                padding: 12px 24px;
                font-weight: bold;
                transition: transform 0.2s ease, background 0.2s ease;
            }
            .stButton>button:hover { 
                background: #cc0000; 
                transform: scale(1.05); 
            }
            .hook-title, .idea-title { color: #ff4b4b; font-size: 20px; font-weight: bold; }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
        """
    }
    return f"<style>{themes.get(st.session_state.theme, themes['light'])}</style>"

# Add particles.js and sound effects
st.markdown("""
    <div id="particles-js"></div>
    <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
    <script>
        particlesJS("particles-js", {
            "particles": {
                "number": { "value": 50, "density": { "enable": true, "value_area": 800 } },
                "color": { "value": "#ffffff" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.5, "random": true },
                "size": { "value": 3, "random": true },
                "line_linked": { "enable": false },
                "move": { "enable": true, "speed": 1, "direction": "none", "random": true }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": { "onhover": { "enable": false }, "onclick": { "enable": false }, "resize": true }
            },
            "retina_detect": true
        });
    </script>
    <audio id="click-sound" src="{click_sound_base64}"></audio>
    <audio id="ding-sound" src="{ding_sound_base64}"></audio>
""".format(click_sound_base64=click_sound_base64, ding_sound_base64=ding_sound_base64), unsafe_allow_html=True)

st.markdown(get_theme_css(), unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.header("🎬 HookForge Settings")
    st.image("https://via.placeholder.com/150.png?text=HookForge", caption="HookForge Logo")
    language = st.selectbox("🌐 Language", ["English", "Spanish", "French", "German", "Italian", "Portuguese"])
    niche = st.selectbox("🎯 Niche", [
        "Finance", "Fitness", "Gaming", "Tech", "Motivation", "Self-Improvement",
        "Education", "Vlogs", "Reactions", "True Crime", "Cooking", "Travel",
        "Beauty", "DIY", "Parenting"
    ])
    tone = st.selectbox("😎 Tone", [
        "Exciting", "Suspenseful", "Relatable", "Controversial", "Funny", "Dramatic"
    ])
    video_type = st.selectbox("🎥 Video Type", [
        "Tutorial", "Listicle", "Storytelling", "Commentary", "Day in the Life",
        "Challenge", "Podcast Clip", "Review", "Interview", "Q&A", "Unboxing"
    ])
    mode = st.selectbox("📱 Platform", ["YouTube", "TikTok/Shorts"], index=0 if st.session_state.mode == "YouTube" else 1)
    if mode != st.session_state.mode:
        st.session_state.mode = mode
        st.rerun()
    theme = st.selectbox("🎨 Theme", ["Light", "Dark", "Neon", "Creator Mode"], index=["light", "dark", "neon", "creator"].index(st.session_state.theme))
    if theme.lower() != st.session_state.theme:
        st.session_state.theme = theme.lower()
        st.rerun()
    video_brief = st.text_area("📝 Video Brief (Optional)", placeholder="E.g., A tutorial on budgeting for beginners", height=100)

# Main content
st.title("🎥 HookForge: Viral Video Hook Generator")
st.markdown("Generate **10 viral hooks** and **3 video ideas** for your videos! Add a video brief for smarter hooks. Toggle **TikTok/Shorts** for shorter hooks.")

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

# TikTok-specific hook templates (shorter, punchier)
tiktok_hook_templates = {
    "English": {
        "Exciting": ["{keyword} will blow your {niche} mind!", "This {keyword} changes {niche}!", "{keyword} in {niche}? Wow!"],
        "Suspenseful": ["{keyword} could ruin {niche}!", "Shocking {keyword} in {niche}!", "Is {keyword} {niche}’s end?"],
        "Relatable": ["{keyword} hits every {niche} fan!", "I get {keyword} in {niche}!", "{keyword} is so {niche}!"],
        "Controversial": ["{keyword}: {niche}’s big lie?", "{keyword} splits {niche}!", "{keyword} shocks {niche}!"],
        "Funny": ["{keyword} in {niche}? LOL!", "{keyword} {niche} fail!", "This {keyword} is hilarious!"],
        "Dramatic": ["{keyword} broke my {niche}!", "{keyword} flips {niche}!", "{keyword} changes {niche}!"]
    },
    "Spanish": {
        "Exciting": ["¡{keyword} te sorprenderá en {niche}!", "¡{keyword} cambia {niche}!", "¡{keyword} en {niche}? Wow!"],
        "Suspenseful": ["¡{keyword} puede arruinar {niche}!", "¡Impactante {keyword} en {niche}!", "¿Es {keyword} el fin de {niche}?"],
        "Relatable": ["¡{keyword} conecta con {niche}!", "¡Entiendo {keyword} en {niche}!", "¡{keyword} es tan {niche}!"],
        "Controversial": ["¿{keyword}: la gran mentira de {niche}?", "¡{keyword} divide {niche}!", "¡{keyword} sacude {niche}!"],
        "Funny": ["¡{keyword} en {niche}? Jaja!", "¡Fallo de {keyword} en {niche}!", "¡Este {keyword} es gracioso!"],
        "Dramatic": ["¡{keyword} rompió mi {niche}!", "¡{keyword} da un giro a {niche}!", "¡{keyword} cambia {niche}!"]
    },
    "French": {
        "Exciting": ["{keyword} va secouer {niche} !", "Ce {keyword} change {niche} !", "{keyword} en {niche} ? Wow !"],
        "Suspenseful": ["{keyword} peut ruiner {niche} !", "Choquant {keyword} en {niche} !", "{keyword}, fin de {niche} ?"],
        "Relatable": ["{keyword} touche tout fan de {niche} !", "Je comprends {keyword} en {niche} !", "{keyword} est si {niche} !"],
        "Controversial": ["{keyword} : le grand mensonge de {niche} ?", "{keyword} divise {niche} !", "{keyword} choque {niche} !"],
        "Funny": ["{keyword} en {niche} ? MDR !", "Échec de {keyword} en {niche} !", "Ce {keyword} est hilarant !"],
        "Dramatic": ["{keyword} a brisé mon {niche} !", "{keyword} bouleverse {niche} !", "{keyword} change {niche} !"]
    },
    "German": {
        "Exciting": ["{keyword} wird {niche} umhauen!", "Dieser {keyword} ändert {niche}!", "{keyword} in {niche}? Wow!"],
        "Suspenseful": ["{keyword} könnte {niche} ruinieren!", "Schockierender {keyword} in {niche}!", "Ist {keyword} das Ende von {niche}?"],
        "Relatable": ["{keyword} trifft jeden {niche}-Fan!", "Ich verstehe {keyword} in {niche}!", "{keyword} ist so {niche}!"],
        "Controversial": ["Ist {keyword} die große Lüge von {niche}?", "{keyword} spaltet {niche}!", "{keyword} schockiert {niche}!"],
        "Funny": ["{keyword} in {niche}? LOL!", "{keyword} {niche}-Fail!", "Dieser {keyword} ist urkomisch!"],
        "Dramatic": ["{keyword} zerstörte mein {niche}!", "{keyword} dreht {niche} um!", "{keyword} ändert {niche}!"]
    },
    "Italian": {
        "Exciting": ["{keyword} ti sconvolgerà in {niche}!", "Questo {keyword} cambia {niche}!", "{keyword} in {niche}? Wow!"],
        "Suspenseful": ["{keyword} potrebbe rovinare {niche}!", "Scioccante {keyword} in {niche}!", "{keyword} è la fine di {niche}?"],
        "Relatable": ["{keyword} colpisce ogni fan di {niche}!", "Capisco {keyword} in {niche}!", "{keyword} è così {niche}!"],
        "Controversial": ["{keyword}: la grande bugia di {niche}?", "{keyword} divide {niche}!", "{keyword} sconvolge {niche}!"],
        "Funny": ["{keyword} in {niche}? LOL!", "Fallimento di {keyword} in {niche}!", "Questo {keyword} è esilarante!"],
        "Dramatic": ["{keyword} ha distrutto il mio {niche}!", "{keyword} capovolge {niche}!", "{keyword} cambia {niche}!"]
    },
    "Portuguese": {
        "Exciting": ["{keyword} vai te surpreender em {niche}!", "Este {keyword} muda {niche}!", "{keyword} em {niche}? Nossa!"],
        "Suspenseful": ["{keyword} pode arruinar {niche}!", "Chocante {keyword} em {niche}!", "{keyword} é o fim de {niche}?"],
        "Relatable": ["{keyword} conecta todo fã de {niche}!", "Entendo {keyword} em {niche}!", "{keyword} é tão {niche}!"],
        "Controversial": ["{keyword}: a grande mentira de {niche}?", "{keyword} divide {niche}!", "{keyword} choca {niche}!"],
        "Funny": ["{keyword} em {niche}? Haha!", "Falha de {keyword} em {niche}!", "Este {keyword} é hilário!"],
        "Dramatic": ["{keyword} destruiu meu {niche}!", "{keyword} vira {niche} de cabeça para baixo!", "{keyword} muda {niche}!"]
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

# A/B test variations
ab_test_variations = {
    "Exciting": ["More Urgent: {hook} NOW!", "Softer: Curious about {keyword}? Check this {niche} {video_type}!"],
    "Suspenseful": ["More Intense: {hook} You CAN’T ignore this!", "Milder: Wondering about {keyword} in {niche}? Find out!"],
    "Relatable": ["More Personal: {hook} It’s my {niche} story!", "Broader: {keyword} speaks to all {niche} fans!"],
    "Controversial": ["Stronger: {hook} The TRUTH revealed!", "Toned Down: {keyword} in {niche}—what’s the real story?"],
    "Funny": ["Exaggerated: {hook} You’ll DIE laughing!", "Subtle: {keyword} in {niche}—pretty funny stuff!"],
    "Dramatic": ["More Epic: {hook} A {niche} game-changer!", "Calmer: {hook} It shook up my {niche}."]
}

# Function to extract keywords from brief
def extract_brief_keywords(brief):
    if not brief:
        return []
    words = brief.lower().split()
    return [word for word in words if len(word) > 3 and word not in ["this", "that", "with", "from", "about", "your", "video"]][:3]

# Function to generate hooks
def generate_hooks(language, niche, tone, video_type, brief, mode):
    templates = tiktok_hook_templates if mode == "TikTok/Shorts" else hook_templates
    templates = templates.get(language, {}).get(tone, hook_templates["English"]["Exciting"])
    keywords = keywords_by_niche.get(language, {}).get(niche, keywords_by_niche["English"]["Motivation"])
    brief_keywords = extract_brief_keywords(brief)
    if brief_keywords:
        keywords = brief_keywords + keywords[:3]  # Prioritize brief keywords
    hooks = []
    for _ in range(10):
        template = random.choice(templates)
        keyword = random.choice(keywords)
        hook = template.format(keyword=keyword, niche=niche.lower(), video_type=video_type.lower())
        if mode == "TikTok/Shorts" and len(hook.split()) > 15:
            hook = " ".join(hook.split()[:12]) + "..."  # Truncate for TikTok
        ab_variations = []
        for var_template in ab_test_variations.get(tone, []):
            var = var_template.format(hook=hook, keyword=keyword, niche=niche.lower(), video_type=video_type.lower())
            ab_variations.append(var)
        hooks.append((hook, ab_variations))
    return hooks

# Function to generate video ideas
def generate_video_ideas(niche, tone, video_type, brief):
    templates = video_idea_templates.get(video_type, video_idea_templates["Tutorial"])
    keywords = keywords_by_niche.get("English", {}).get(niche, keywords_by_niche["English"]["Motivation"])
    brief_keywords = extract_brief_keywords(brief)
    if brief_keywords:
        keywords = brief_keywords + keywords[:3]
    ideas = []
    for _ in range(3):
        template = random.choice(templates)
        keyword = random.choice(keywords)
        idea = template.format(keyword=keyword, niche=niche.lower(), tone=tone.lower())
        ideas.append(idea)
    return ideas

# Function to calculate virality score
def calculate_virality_score(hook, tone):
    score = 50  # Base score
    words = hook.lower().split()
    length = len(words)
    emotional_words = ["shock", "secret", "hack", "fail", "reveal", "truth", "believe", "hilarious", "change", "forever"]
    if st.session_state.mode == "TikTok/Shorts":
        if length <= 12:
            score += 20
        elif length <= 15:
            score += 10
    else:
        if 10 <= length <= 20:
            score += 15
        elif length < 10:
            score += 5
    for word in emotional_words:
        if word in hook.lower():
            score += 10
    if tone in ["Exciting", "Suspenseful", "Controversial"]:
        score += 10
    elif tone == "Funny":
        score += 5
    score = min(score, 100)
    if score >= 80:
        return score, "🔥 High potential for 3s retention!"
    elif score >= 60:
        return score, "👍 Solid hook, great for engagement!"
    elif score >= 40:
        return score, "🤖 Sounds a bit robotic — tweak the tone?"
    else:
        return score, "😕 Needs more punch for virality."

# Generate hooks and ideas
if st.button("🚀 Generate Hooks & Ideas"):
    hooks = generate_hooks(language, niche, tone, video_type, video_brief, st.session_state.mode)
    ideas = generate_video_ideas(niche, tone, video_type, video_brief)
    
    # Create shareable link
    query_params = {
        "language": language,
        "niche": niche,
        "tone": tone,
        "video_type": video_type,
        "mode": st.session_state.mode,
        "hooks": "|".join([hook[0] for hook in hooks]),
        "ideas": "|".join(ideas)
    }
    shareable_link = f"https://hookforge-yourname.streamlit.app/?{urllib.parse.urlencode(query_params)}"
    
    # Display hooks
    st.subheader("🎣 Your Viral Hooks")
    hook_text = ""
    for i, (hook, ab_variations) in enumerate(hooks, 1):
        hook_text += f"Hook {i}: {hook}\n"
        score, feedback = calculate_virality_score(hook, tone)
        with st.container():
            st.markdown(f"<div class='hook-card'><p class='hook-title'>Hook {i} (Virality Score: {score}/100)</p>{hook}<br>{feedback}</div>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.code(hook, language="text")
            with col2:
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
            with col3:
                st.markdown(f"""
                    <a href="https://twitter.com/intent/tweet?text=Check%20out%20this%20viral%20hook%20I%20made%20with%20HookForge!%20{hook}%20{shareable_link}" target="_blank">
                        <button>Share on X</button>
                    </a>
                """, unsafe_allow_html=True)
            with st.expander("A/B Test Variations"):
                for j, var in enumerate(ab_variations, 1):
                    var_score, var_feedback = calculate_virality_score(var, tone)
                    st.markdown(f"**Variation {j} (Score: {var_score}/100):** {var} — {var_feedback}")
    
    # Download hooks
    st.download_button(
        label="📥 Download Hooks",
        data=hook_text,
        file_name="hookforge_hooks.txt",
        mime="text/plain"
    )
    
    # Shareable link
    st.markdown(f"🔗 **Shareable Link**: <a href='{shareable_link}' target='_blank'>Copy this link</a>", unsafe_allow_html=True)
    st.markdown(f"""
        <button onclick="navigator.clipboard.writeText('{shareable_link}')">Copy Link</button>
        <script>
        document.querySelectorAll('button').forEach(button => {{
            if (button.innerText === 'Copy Link') {{
                button.addEventListener('click', () => {{
                    navigator.clipboard.writeText('{shareable_link}');
                    button.innerText = 'Link Copied!';
                    setTimeout(() => {{ button.innerText = 'Copy Link'; }}, 2000);
                }});
            }}
        }});
        </script>
    """, unsafe_allow_html=True)
    
    # Display video ideas
    st.subheader("💡 Video Ideas")
    for i, idea in enumerate(ideas, 1):
        with st.container():
            st.markdown(f"<div class='idea-card'><p class='idea-title'>Idea {i}</p>{idea}</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by HookForge | Powered by [Streamlit](https://streamlit.io)", unsafe_allow_html=True)
