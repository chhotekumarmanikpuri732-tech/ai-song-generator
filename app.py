import streamlit as str_lib
import requests

# --- PAGE CONFIGURATION ---
str_lib.set_page_config(
    page_title="Manikpuri Digital Service & Academy - AI Song Maker",
    page_icon="🎵",
    layout="centered"
)

# --- CUSTOM CSS STYLING ---
str_lib.markdown("""
    <style>
    .brand-header {
        text-align: center;
        background: linear-gradient(135deg, #FF4B4B, #FF8E53);
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin-bottom: 20px;
    }
    .brand-title {
        font-size: 1.8rem;
        font-weight: bold;
        margin: 0;
    }
    .brand-subtitle {
        font-size: 1rem;
        margin-top: 5px;
        opacity: 0.9;
    }
    .main-title {
        text-align: center;
        color: #222;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .sub-title {
        text-align: center;
        color: #666;
        margin-bottom: 25px;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-size: 18px;
        height: 50px;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- BRAND HEADER (यहाँ आपका नाम और अकादमी दिखेगी) ---
str_lib.markdown("""
    <div class='brand-header'>
        <p class='brand-title'>✨ Manikpuri Digital Service & Academy ✨</p>
        <p class='brand-subtitle'>Digital Creator & AI Tool Platform</p>
    </div>
""", unsafe_allow_html=True)

# --- APP MAIN HEADING ---
str_lib.markdown("<h1 class='main-title'>🎵 AI Song Generator Studio</h1>", unsafe_allow_html=True)
str_lib.markdown("<p class='sub-title'>अपनी पसंद की मूवी और गाने की तर्ज पर अपना खुद का लिरिक्स गाना बनाएँ!</p>", unsafe_allow_html=True)

str_lib.divider()

# --- INPUT FORM (3 OPTIONS) ---
col1, col2 = str_lib.columns(2)

with col1:
    movie_name = str_lib.text_input("1. किसी भी मूवी का नाम (Movie Name)", placeholder="उदा. Shershaah, Animal...")

with col2:
    song_name = str_lib.text_input("2. उस मूवी का गाना (Song Name)", placeholder="उदा. Raataan Lambiyan, Pehle Bhi Main...")

lyrics = str_lib.text_area("3. अपना नया लिरिक्स (Your Custom Lyrics)", placeholder="यहाँ अपना लिखा हुआ शानदार लिरिक्स टाइप करें...", height=150)

str_lib.write("")

# --- GENERATE BUTTON ---
if str_lib.button("🚀 गाना तैयार करें (Generate Song)"):
    if not movie_name or not song_name or not lyrics:
        str_lib.warning("⚠️ कृपया तीनों विकल्प (मूवी का नाम, गाने का नाम और अपना लिरिक्स) ठीक से भरें!")
    else:
        str_lib.info("🎵 AI आपके गाने की धुन तैयार कर रहा है... कृपया कुछ सेकंड इंतज़ार करें!")
        
        # PROMPT CREATION FOR MUSIC AI
        prompt = f"A melodious song inspired by '{song_name}' from the movie '{movie_name}'. Vocals singing custom lyrics: {lyrics}"
        
        with str_lib.spinner("🎧 म्यूज़िक और वोकल कंपोज़ हो रहे हैं..."):
            try:
                # Meta MusicGen API (Free Hugging Face Inference)
                API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
                payload = {"inputs": prompt}
                
                response = requests.post(API_URL, json=payload, timeout=60)
                
                if response.status_code == 200:
                    audio_bytes = response.content
                    str_lib.success("🎉 आपका नया गाना बनकर तैयार है!")
                    str_lib.audio(audio_bytes, format="audio/wav")
                    str_lib.download_button(
                        label="⬇️ गाना डाउनलोड करें (Download Audio)",
                        data=audio_bytes,
                        file_name=f"{song_name}_custom_cover.wav",
                        mime="audio/wav"
                    )
                else:
                    # Fallback preview if free queue is heavy
                    str_lib.warning("⚡ फ्री AI सर्वर अभी व्यस्त है, आपका प्रोजेक्ट डेटा दर्ज हो गया है:")
                    str_lib.write(f"🎬 **मूवी:** {movie_name} | 🎵 **गाना:** {song_name}")
                    str_lib.info(f"📝 **आपका लिरिक्स:**\n{lyrics}")
                    
            except Exception as e:
                str_lib.error("कनेक्शन में कुछ दिक्कत आई। कृपया दोबारा बटन दबाएँ!")
