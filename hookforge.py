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
click_sound_base64 = "data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YSQUAAAAAA=="
ding_sound_base64 = "data:audio/wav;base64,UklGRiYAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YSYUAAAAAA=="

# Custom CSS for themes
def get_theme_css():
    themes = {
        "light": """
            .main { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); color: #333; }
            .sidebar .sidebar-content { background: #ffffff; }
            .hook-card, .idea-card {
                background: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 10px;
                transition: transform 0.3s ease, box-shadow 0.3s ease; opacity: 0; animation: fadeIn 0.5s forwards;
            }
            .hook-card:hover, .idea-card:hover { transform: translateY(-3px); box-shadow: 0 6px 15px rgba(0,0,0,0.2); }
            .stButton>button { background: #ff4b4b; color: white; border-radius: 8px; padding: 10px 20px; font-weight: bold; }
            .stButton>button:hover { background: #e04343; transform: scale(1.05); }
            .hook-title, .idea-title { color: #333; font-size: 18px; font-weight: bold; }
            @keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }
        """,
        "dark": """
            .main { background: linear-gradient(135deg, #1e1e1e 0%, #434343 100%); color: #fff; }
            .sidebar .sidebar-content { background: #2a2a2a; }
            .hook-card, .idea-card {
                background: #2a2a2a; padding: 15px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.3); margin-bottom: 10px;
                transition: transform 0.3s ease, box-shadow 0.3s ease; opacity: 0; animation: fadeIn 0.5s forwards;
            }
            .hook-card:hover, .idea-card:hover { transform: translateY(-3px); box-shadow: 0 6px 15px rgba(0,0,0,0.4); }
            .stButton>button { background: #ff4b4b; color: white; border-radius: 8px; padding: 10px 20px; font-weight: bold; }
            .stButton>button:hover { background: #e04343; transform: scale(1.05); }
            .hook-title, .idea-title { color: #fff; font-size: 18px; font-weight: bold; }
            @keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }
        """,
        "neon": """
            .main { background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%); color: #fff; }
            .sidebar .sidebar-content { background: #1a2a44; }
            .hook-card, .idea-card {
                background: #1a2a44; padding: 15px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,255,255,0.5); margin-bottom: 10px;
                transition: transform 0.3s ease, box-shadow 0.3s ease; opacity: 0; animation: fadeIn 0.5s forwards;
            }
            .hook-card:hover, .idea-card:hover { transform: translateY(-3px); box-shadow: 0 6px 15px rgba(0,255,255,0.7); }
            .stButton>button { background: #00ffcc; color: #000; border-radius: 8px; padding: 10px 20px; font-weight: bold; }
            .stButton>button:hover { background: #00ccaa; transform: scale(1.05); }
            .hook-title, .idea-title { color: #00ffcc; font-size: 18px; font-weight: bold; }
            @keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }
        """,
        "creator": """
            .main { background: linear-gradient(135deg, #ff0000 0%, #ff4b4b 50%, #000000 100%); color: #fff; box-shadow: inset 0 0 40px rgba(255,0,0,0.5); }
            .sidebar .sidebar-content { background: #1a1a1a; }
            .hook-card, .idea-card {
                background: #2a2a2a; padding: 15px; border-radius: 10px; box-shadow: 0 0 15px rgba(255,0,0,0.7); margin-bottom: 10px;
                transition: transform 0.3s ease, box-shadow 0.3s ease; opacity: 0; animation: fadeIn 0.5s forwards;
            }
            .hook-card:hover, .idea-card:hover { transform: translateY(-3px); box-shadow: 0 6px 15px rgba(255,0,0,0.9); }
            .stButton>button { background: #ff0000; color: white; border-radius: 8px; padding: 10px 20px; font-weight: bold; }
            .stButton>button:hover { background: #cc0000; transform: scale(1.05); }
            .hook-title, .idea-title { color: #ff4b4b; font-size: 18px; font-weight: bold; }
            @keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }
        """
    }
    return f"<style>{themes.get(st.session_state.theme, themes['light'])}</style>"

# Add sound effects (simplified, no particles.js to reduce size)
st.markdown(f"""
    <audio id="click-sound" src="{click_sound_base64}"></audio>
    <audio id="ding-sound" src="{ding_sound_base64}"></audio>
""", unsafe_allow_html=True)

st.markdown(get_theme_css(), unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.header("🎬 HookForge Settings")
    st.image("https://via.placeholder.com/150.png?text=HookForge", caption="HookForge Logo")
    language = st.selectbox("🌐 Language", ["English", "Spanish", "French", "German", "Italian", "Portuguese"])
    niche = st.selectbox("🎯 Niche", ["Finance", "Fitness", "Gaming", "Tech", "Motivation", "Self-Improvement", "Education", "Vlogs", "Reactions", "True Crime", "Cooking", "Travel", "Beauty", "DIY", "Parenting"])
    tone = st.selectbox("😎 Tone", ["Exciting", "Suspenseful", "Relatable", "Controversial", "Funny", "Dramatic"])
    video_type = st.selectbox("🎥 Video Type", ["Tutorial", "Listicle", "Storytelling", "Commentary", "Day in the Life", "Challenge", "Podcast Clip", "Review", "Interview", "Q&A", "Unboxing"])
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
st.markdown("Generate **10 viral hooks** and **3 video ideas** for your videos! Add a video brief for smarter hooks.")

# Simplified templates (only English for brevity; expand as needed)
hook_templates = {
    "English": {
        "Exciting": ["You won't believe {keyword} that will change your {niche} game!", "This {video_type} reveals the {keyword} everyone’s talking about!"],
        "Suspenseful": ["What if {keyword} could ruin your {niche} forever?", "The {keyword} behind this {video_type} will shock you!"],
        "Relatable": ["Struggling with {niche}? This {keyword} is for YOU!", "Every {niche} fan will relate to this {keyword}!"],
        "Controversial": ["Is {keyword} the biggest lie in {niche}?", "Why {keyword} is dividing the {niche} community!"],
        "Funny": ["I tried {keyword} in {niche} and it was HILARIOUS!", "The {keyword} fail that broke the internet!"],
        "Dramatic": ["The {keyword} that broke my {niche} journey!", "How {keyword} turned my {niche} upside down!"]
    }
}

tiktok_hook_templates = {
    "English": {
        "Exciting": ["{keyword} will blow your {niche} mind!", "This {keyword} changes {niche}!"],
        "Suspenseful": ["{keyword} could ruin {niche}!", "Shocking {keyword} in {niche}!"],
        "Relatable": ["{keyword} hits every {niche} fan!", "I get {keyword} in {niche}!"],
        "Controversial": ["{keyword}: {niche}’s big lie?", "{keyword} shocks {niche}!"],
        "Funny": ["{keyword} in {niche}? LOL!", "This {keyword} is hilarious!"],
        "Dramatic": ["{keyword} broke my {niche}!", "{keyword} changes {niche}!"]
    }
}

keywords_by_niche = {
    "English": {
        "Finance": ["trick to millions", "investment hack"], "Fitness": ["workout secret", "diet hack"], "Gaming": ["pro tip", "cheat code"],
        "Tech": ["gadget hack", "app secret"], "Motivation": ["mindset shift", "success secret"], "Self-Improvement": ["habit hack", "productivity tip"],
        "Education": ["study hack", "learning trick"], "Vlogs": ["daily hack", "life moment"], "Reactions": ["viral moment", "shock factor"],
        "True Crime": ["case secret", "mystery hack"], "Cooking": ["recipe hack", "cooking tip"], "Travel": ["destination hack", "travel tip"],
        "Beauty": ["makeup hack", "skincare secret"], "DIY": ["craft hack", "project tip"], "Parenting": ["parenting hack", "kid tip"]
    }
}

video_idea_templates = {
    "Tutorial": ["Teach viewers how to master {keyword} in {niche} with a step-by-step guide."],
    "Listicle": ["Rank the top 5 {keyword} tips for {niche} in a {tone} list."],
    "Storytelling": ["Tell a {tone} story about how {keyword} transformed your {niche} journey."],
    "Commentary": ["Give a {tone} take on the latest {keyword} trends in {niche}."],
    "Day in the Life": ["Show a {tone} day incorporating {keyword} into your {niche} routine."],
    "Challenge": ["Take on a {tone} {keyword} challenge in {niche} and share the results."],
    "Podcast Clip": ["Share a {tone} podcast clip discussing {keyword} in {niche}."],
    "Review": ["Review a {keyword} product or tool for {niche} with a {tone} perspective."],
    "Interview": ["Interview a {niche} expert on {keyword} with a {tone} approach."],
    "Q&A": ["Answer viewer questions about {keyword} in {niche} with a {tone} vibe."],
    "Unboxing": ["Unbox a {keyword} product for {niche} with a {tone} reaction."]
}

ab_test_variations = {
    "Exciting": ["More Urgent: {hook} NOW!", "Softer: Curious about {keyword}? Check this {niche} {video_type}!"],
    "Suspenseful": ["More Intense: {hook} You CAN’T ignore this!", "Milder: Wondering about {keyword} in {niche}? Find out!"],
    "Relatable": ["More Personal: {hook} It’s my {niche} story!", "Broader: {keyword} speaks to all {niche} fans!"],
    "Controversial": ["Stronger: {hook} The TRUTH revealed!", "Toned Down: {keyword} in {niche}—what’s the real story?"],
    "Funny": ["Exaggerated: {hook} You’ll DIE laughing!", "Subtle: {keyword} in {niche}—pretty funny stuff!"],
    "Dramatic": ["More Epic: {hook} A {niche} game-changer!", "Calmer: {hook} It shook up my {niche}."]
}

# Functions
def extract_brief_keywords(brief):
    if not brief:
        return []
    words = brief.lower().split()
    return [word for word in words if len(word) > 3 and word not in ["this", "that", "with", "from", "about", "your", "video"]][:2]

def generate_hooks(language, niche, tone, video_type, brief, mode):
    templates = tiktok_hook_templates if mode == "TikTok/Shorts" else hook_templates
    templates = templates.get(language, {}).get(tone, hook_templates["English"]["Exciting"])
    keywords = keywords_by_niche.get(language, {}).get(niche, keywords_by_niche["English"]["Motivation"])
    brief_keywords = extract_brief_keywords(brief)
    if brief_keywords:
        keywords = brief_keywords + keywords[:1]
    hooks = []
    for _ in range(10):
        template = random.choice(templates)
        keyword = random.choice(keywords)
        hook = template.format(keyword=keyword, niche=niche.lower(), video_type=video_type.lower())
        if mode == "TikTok/Shorts" and len(hook.split()) > 10:
            hook = " ".join(hook.split()[:8]) + "..."
        ab_variations = [var.format(hook=hook, keyword=keyword, niche=niche.lower(), video_type=video_type.lower()) for var in ab_test_variations.get(tone, [])]
        hooks.append((hook, ab_variations))
    return hooks

def generate_video_ideas(niche, tone, video_type, brief):
    templates = video_idea_templates.get(video_type, video_idea_templates["Tutorial"])
    keywords = keywords_by_niche.get("English", {}).get(niche, keywords_by_niche["English"]["Motivation"])
    brief_keywords = extract_brief_keywords(brief)
    if brief_keywords:
        keywords = brief_keywords + keywords[:1]
    ideas = []
    for _ in range(3):
        template = random.choice(templates)
        keyword = random.choice(keywords)
        idea = template.format(keyword=keyword, niche=niche.lower(), tone=tone.lower())
        ideas.append(idea)
    return ideas

def calculate_virality_score(hook, tone):
    score = 50
    words = hook.lower().split()
    length = len(words)
    emotional_words = ["shock", "secret", "hack", "fail", "reveal", "truth", "believe", "hilarious", "change", "forever"]
    if st.session_state.mode == "TikTok/Shorts":
        if length <= 8: score += 20
        elif length <= 10: score += 10
    else:
        if 8 <= length <= 15: score += 15
        elif length < 8: score += 5
    for word in emotional_words:
        if word in hook.lower(): score += 10
    if tone in ["Exciting", "Suspenseful", "Controversial"]: score += 10
    elif tone == "Funny": score += 5
    score = min(score, 100)
    if score >= 80: return score, "🔥 High potential!"
    elif score >= 60: return score, "👍 Solid hook!"
    elif score >= 40: return score, "🤖 Tweak the tone?"
    else: return score, "😕 Needs more punch."

# Generate hooks and ideas
if st.button("🚀 Generate Hooks & Ideas", key="generate"):
    st.markdown("<script>document.getElementById('ding-sound').play();</script>", unsafe_allow_html=True)
    hooks = generate_hooks(language, niche, tone, video_type, video_brief, st.session_state.mode)
    ideas = generate_video_ideas(niche, tone, video_type, video_brief)
    query_params = {"language": language, "niche": niche, "tone": tone, "video_type": video_type, "mode": st.session_state.mode, "hooks": "|".join([hook[0] for hook in hooks]), "ideas": "|".join(ideas)}
    shareable_link = f"https://hookforge.streamlit.app/?{urllib.parse.urlencode(query_params)}"

    # Display hooks
    st.subheader("🎣 Your Viral Hooks")
    hook_text = ""
    for i, (hook, ab_variations) in enumerate(hooks, 1):
        hook_text += f"Hook {i}: {hook}\n"
        score, feedback = calculate_virality_score(hook, tone)
        with st.container():
            st.markdown(f"<div class='hook-card'><p class='hook-title'>Hook {i} (Score: {score}/100)</p>{hook}<br>{feedback}</div>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.code(hook, language="text")
            with col2:
                if st.button("Copy Hook", key=f"copy_hook_{i}"):
                    st.session_state[f"copied_hook_{i}"] = True
                    st.markdown("<script>document.getElementById('click-sound').play();</script>", unsafe_allow_html=True)
                if st.session_state.get(f"copied_hook_{i}", False):
                    st.success("Copied!")
            with col3:
                st.markdown("**A/B Variations**")
                for var in ab_variations:
                    st.write(f"- {var}")

    # Download hooks
    st.download_button(label="📥 Download Hooks", data=hook_text, file_name="hookforge_hooks.txt", mime="text/plain")

    # Shareable link
    st.markdown(f"🔗 **Shareable Link**: {shareable_link}")
    if st.button("Copy Link"):
        st.session_state["copied_link"] = True
        st.markdown("<script>document.getElementById('click-sound').play();</script>", unsafe_allow_html=True)
    if st.session_state.get("copied_link", False):
        st.success("Link Copied!")

    # Display video ideas
    st.subheader("💡 Video Ideas")
    idea_text = ""
    for i, idea in enumerate(ideas, 1):
        idea_text += f"Idea {i}: {idea}\n"
        with st.container():
            st.markdown(f"<div class='idea-card'><p class='idea-title'>Idea {i}</p>{idea}</div>", unsafe_allow_html=True)
            col1, col2 = st.columns([3, 1])
            with col1:
                st.code(idea, language="text")
            with col2:
                if st.button("Copy Idea", key=f"copy_idea_{i}"):
                    st.session_state[f"copied_idea_{i}"] = True
                    st.markdown("<script>document.getElementById('click-sound').play();</script>", unsafe_allow_html=True)
                if st.session_state.get(f"copied_idea_{i}", False):
                    st.success("Copied!")

    # Download video ideas
    st.download_button(label="📥 Download Ideas", data=idea_text, file_name="hookforge_ideas.txt", mime="text/plain")

# Footer
st.markdown("---")
st.markdown("🎥 **HookForge** - Built with 💖 by [Your Name] | Powered by [xAI](https://x.ai) | © 2025", unsafe_allow_html=True)
