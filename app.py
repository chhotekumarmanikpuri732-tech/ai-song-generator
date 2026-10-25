import streamlit as st

# Page Configuration
st.set_page_config(page_title="Manikpuri AI Lyrics Hub", page_icon="🎵", layout="centered")

# App Header
st.title("🎵 Manikpuri AI Lyrics & Song Hub")
st.subheader("Manikpuri Digital Service & Academy")
st.caption("यहाँ पाएँ भक्ति भजन, सुपरहिट गीत और स्टेटस शायरियाँ - एक क्लिक में कॉपी करें!")

st.markdown("---")

# Categories Selection
category = st.selectbox(
    "अपनी पसंद की कैटेगरी चुनें:",
    ["🚩 भक्ति भजन (Bhakti Songs)", "❤️ रोमैंटिक / लव सॉन्ग", "🔥 मोटिवेशनल / स्टेटस शायरी", "✨ खुद का लिरिक्स बनाएँ (Custom AI)"]
)

# Song Database
if category == "🚩 भक्ति भजन (Bhakti Songs)":
    st.markdown("### 🚩 ओ मेरी माँ जगदम्बे")
    lyrics_1 = """ओ मेरी माँ जगदम्बे, चरणों में तेरे नमन करूँ,
तू ही मेरी शक्ति है, तुझसे ही जीवन वरण करूँ।
ममता की मूरत है तू, सारे जग की दाती,
तेरे दर पे आके हर विपदा टल जाती!

सुबह की पहली किरण में तेरा ही नाम लूँ,
हर सांस में तेरी पूजा का पैगाम लूँ।
अँधेरी इस दुनिया में तूने राह दिखाई,
मुझको हर मुश्किल से मेरी मैय्या ने बचाई।
तेरी चुनरी की छांव में सुख सारा पाऊँ,
हर जनम मैं तेरी ही चरणों में आऊँ!"""
    
    st.text_area("लिरिक्स:", value=lyrics_1, height=220)

elif category == "❤️ रोमैंटिक / लव सॉन्ग":
    st.markdown("### ❤️ दिल की धड़कन तू")
    lyrics_2 = """तेरे बिना मेरी रातें अधूरी,
तू पास आए तो हो ख्वाहिशें पूरी।
चाँदनी रात में तेरा ही चेहरा दिखे,
मेरी हर दुआ में सिर्फ तेरा ही नाम लिखा दिखे!

तू ही मेरी सुबह, तू ही मेरी शाम है,
इस दिल पे लिखा सिर्फ तेरा ही नाम है।"""
    
    st.text_area("लिरिक्स:", value=lyrics_2, height=180)

elif category == "🔥 मोटिवेशनल / स्टेटस शायरी":
    st.markdown("### 🔥 मंज़िल की तलाश")
    lyrics_3 = """जो हो गया उसे सोचा नहीं करते,
जब मिल गया उसे खोया नहीं करते।
हासिल उन्हें होती है मंज़िल अक्सर,
जो वक़्त और हालात पर रोया नहीं करते!

लहरों से डर कर नौका पार नहीं होती,
कोशिश करने वालों की कभी हार नहीं होती!"""
    
    st.text_area("लिरिक्स:", value=lyrics_3, height=180)

elif category == "✨ खुद का लिरिक्स बनाएँ (Custom AI)":
    topic = st.text_input("किस टॉपिक पर गाना/शायरी चाहिए?")
    if st.button("✨ लिरिक्स तैयार करें"):
        if topic:
            st.success(f"'{topic}' पर आपका लिरिक्स नीचे तैयार है:")
            custom_text = f"""[शीर्षक: {topic}]\n\nहर मोड़ पर तेरा नाम रहेगा,\nदिल में हमेशा तेरा ही पैगाम रहेगा।\nकोशिश हमारी रंग लाएगी ज़रूर,\nअब सफलता का ही नया आगाज़ रहेगा!"""
            st.text_area("लिरिक्स (कॉपी करें):", value=custom_text, height=180)
        else:
            st.warning("कृपया कोई टॉपिक लिखें!")

st.markdown("---")
st.caption("© 2026 Manikpuri Digital Service & Academy | All Rights Reserved")
