import streamlit as st
from gtts import gTTS
import base64
from io import BytesIO

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Text to Voice AI",
    page_icon="🔊",
    layout="centered"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #141e30, #243b55);
}

.title {
    text-align: center;
    color: white;
    font-size: 45px;
    font-weight: bold;
    margin-top: 30px;
}

.subtitle {
    text-align: center;
    color: #d9d9d9;
    font-size: 18px;
    margin-bottom: 30px;
}

.box {
    background: rgba(255,255,255,0.10);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.15);
}

.result {
    background: white;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}

.footer {
    text-align: center;
    color: #cccccc;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown(
    '<div class="title">🔊 Text to Voice AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Convert your written text into natural-sounding speech</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# TEXT INPUT
# --------------------------------------------------

st.markdown('<div class="box">', unsafe_allow_html=True)

text = st.text_area(
    "✍️ Enter your text",
    placeholder="Type something here and convert it into speech...",
    height=200
)

# --------------------------------------------------
# LANGUAGE
# --------------------------------------------------

language = st.selectbox(
    "🌍 Select Language",
    [
        "English",
        "Hindi",
        "Telugu",
        "Tamil",
        "Kannada",
        "Malayalam",
        "Bengali",
        "Marathi"
    ]
)

language_codes = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Bengali": "bn",
    "Marathi": "mr"
}

# --------------------------------------------------
# CONVERT BUTTON
# --------------------------------------------------

convert = st.button(
    "🎙️ Convert Text to Voice",
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# TEXT TO SPEECH
# --------------------------------------------------

if convert:

    if not text.strip():

        st.warning("⚠️ Please enter some text first.")

    else:

        with st.spinner("🔄 Generating voice..."):

            try:

                lang_code = language_codes[language]

                # Create audio
                tts = gTTS(
                    text=text,
                    lang=lang_code,
                    slow=False
                )

                # Store audio in memory
                audio_buffer = BytesIO()
                tts.write_to_fp(audio_buffer)

                audio_buffer.seek(0)

                # --------------------------------------------------
                # RESULT
                # --------------------------------------------------

                st.markdown(
                    '<div class="result">',
                    unsafe_allow_html=True
                )

                st.subheader("🎧 Generated Voice")

                st.audio(
                    audio_buffer,
                    format="audio/mp3"
                )

                # --------------------------------------------------
                # DOWNLOAD
                # --------------------------------------------------

                st.download_button(
                    label="⬇️ Download Voice",
                    data=audio_buffer.getvalue(),
                    file_name="text_to_voice.mp3",
                    mime="audio/mpeg",
                    use_container_width=True
                )

                st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:

                st.error(
                    f"❌ Unable to generate voice.\n\nError: {e}"
                )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    '<div class="footer">✨ Text to Voice AI • Built with Python & Streamlit</div>',
    unsafe_allow_html=True
)