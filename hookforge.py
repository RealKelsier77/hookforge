import streamlit as st
import random

# Streamlit page configuration
st.set_page_config(page_title="HookForge", page_icon="🎥", layout="centered")

# Title and description
st.title("HookForge: Viral YouTube Hook Generator")
st.markdown("Create catchy video hooks for your YouTube content! Select your niche, tone, and video type, then hit 'Generate Hooks' to get 5 viral hook ideas.")

# Dropdowns for user inputs
niche = st.selectbox("Select Niche", [
    "Finance", "Fitness", "Gaming", "Tech", "Motivation", 
    "Self-Improvement", "Education", "Vlogs", "Reactions", "True Crime"
])
tone = st.selectbox("Select Tone", [
    "Exciting", "Suspenseful", "Relatable", "Controversial", "Funny", "Dramatic"
])
video_type = st.selectbox("Select Video Type", [
    "Tutorial", "Listicle", "Storytelling", "Commentary", 
    "Day in the Life", "Challenge", "Podcast Clip"
])

# Mock hook templates and keywords
hook_templates = {
    "Exciting": [
        "You won't believe {keyword} that will change your {niche} game!",
        "This {video_type} reveals the {keyword} everyone’s talking about!",
        "Get ready for a {niche} {keyword} you NEED to know!"
    ],
    "Suspenseful": [
        "What if {keyword} could ruin your {niche} forever?",
        "The {keyword} behind this {video_type} will shock you!",
        "This {niche} secret about {keyword} changes everything..."
    ],
    "Relatable": [
        "Struggling with {niche}? This {keyword} is for YOU!",
        "I tried {keyword} in my {video_type} and it felt so real!",
        "Every {niche} fan will relate to this {keyword}!"
    ],
    "Controversial": [
        "Is {keyword} the biggest lie in {niche}?",
        "This {video_type} exposes the {keyword} no one talks about!",
        "Why {keyword} is dividing the {niche} community!"
    ],
    "Funny": [
        "I tried {keyword} in {niche} and it was HILARIOUS!",
        "This {video_type} about {keyword} will make you LOL!",
        "Who knew {niche} could be this {keyword} funny?"
    ],
    "Dramatic": [
        "The {keyword} that broke my {niche} journey!",
        "This {video_type} uncovers a {keyword} you can’t ignore!",
        "How {keyword} turned my {niche} upside down!"
    ]
}

keywords_by_niche = {
    "Finance": ["trick to millions", "investment hack", "money mistake", "side hustle", "debt trap"],
    "Fitness": ["workout secret", "diet hack", "muscle myth", "cardio trick", "fitness fail"],
    "Gaming": ["pro tip", "cheat code", "game glitch", "epic fail", "hidden easter egg"],
    "Tech": ["gadget hack", "app secret", "tech myth", "AI trick", "device fail"],
    "Motivation": ["mindset shift", "success secret", "life hack", "goal trick", "inspiration boost"],
    "Self-Improvement": ["habit hack", "productivity tip", "mindset myth", "growth secret", "self-care fail"],
    "Education": ["study hack", "learning trick", "exam secret", "knowledge myth", "school fail"],
    "Vlogs": ["daily hack", "life moment", "vlog secret", "travel tip", "routine fail"],
    "Reactions": ["viral moment", "shock factor", "meme secret", "trend hack", "reaction fail"],
    "True Crime": ["case secret", "mystery hack", "crime myth", "twist reveal", "suspect fail"]
}

# Function to generate hooks
def generate_hooks(niche, tone, video_type):
    templates = hook_templates.get(tone, hook_templates["Exciting"])
    keywords = keywords_by_niche.get(niche, keywords_by_niche["Motivation"])
    hooks = []
    for _ in range(5):
        template = random.choice(templates)
        keyword = random.choice(keywords)
        hook = template.format(keyword=keyword, niche=niche.lower(), video_type=video_type.lower())
        hooks.append(hook)
    return hooks

# Generate hooks button
if st.button("Generate Hooks"):
    hooks = generate_hooks(niche, tone, video_type)
    st.subheader("Your Viral Hooks")
    for i, hook in enumerate(hooks, 1):
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"**Hook {i}:** {hook}")
        with col2:
            st.code(hook, language="text")  # Copyable text block

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by HookForge | Powered by Streamlit")
