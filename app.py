import streamlit as st
import subprocess
from PIL import Image
import tempfile
import os
import pytesseract
# ---------------------------
# CONFIG
# ---------------------------
MODEL = "tinyllama"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"

st.set_page_config(page_title="Multimodal Assistant Demo", layout="wide")

st.title("🚀 Multimodal AI Assistant (Evolution Demo)")

# ---------------------------
# HELPER: OLLAMA CALL
# ---------------------------
def run_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", MODEL],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()

# ---------------------------
# SIDEBAR - VERSION CONTROL
# ---------------------------
version = st.sidebar.selectbox(
    "Select Version",
    [
        "V0 - Text Only",
        "V1 - Image Understanding",
        "V2 - Structured Output",
        "V3 - Voice Input (Simulated)",
        "V4 - Voice Output (Simulated)",
        "V5 - Full Assistant"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("Model:", MODEL)

# ---------------------------
# INPUT SECTION
# ---------------------------
st.header("🧾 Input")

user_text = st.text_input("Ask a question")

uploaded_file = st.file_uploader("Upload an image (invoice, doc)", type=["png", "jpg", "jpeg"])

audio_note = st.text_area("🎤 (Simulated Voice Input - type what user says)")

# ---------------------------
# IMAGE → TEXT (SIMPLIFIED OCR)
# ---------------------------
import pytesseract

def real_ocr(image):
    text = pytesseract.image_to_string(image)
    return text.strip()

# ---------------------------
# PROMPT BUILDER
# ---------------------------
def build_prompt(version, user_text, context):

    base = f"""
You are a helpful AI assistant.
"""

    if version == "V0 - Text Only":
        return f"{base}\nUser: {user_text}"

    elif version == "V1 - Image Understanding":
        return f"""
{base}

Context:
{context}

User: {user_text}
"""

    elif version == "V2 - Structured Output":
        return f"""
{base}

Extract:
- Total Amount
- Due Date

Context:
{context}

User: {user_text}
"""

    elif version == "V3 - Voice Input (Simulated)":
        return f"""
{base}

User said:
{user_text}
"""

    elif version == "V4 - Voice Output (Simulated)":
        return f"""
{base}

Answer clearly so it can be spoken.

User:
{user_text}
"""

    elif version == "V5 - Full Assistant":
        return f"""
You are a helpful AI assistant.

Rules:
- Answer based on context if available
- Be concise
- Extract structured info if relevant

Context:
{context}

User:
{user_text}
"""

# ---------------------------
# PROCESS INPUT
# ---------------------------
context = ""

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    context =  real_ocr(image)
    st.info(f"📄 Extracted Text:\n{context}")

# Voice simulation
if audio_note:
    user_text = audio_note

# ---------------------------
# RUN BUTTON
# ---------------------------
if st.button("Run Assistant"):

    if not user_text:
        st.warning("Please enter a question")
    else:
        prompt = build_prompt(version, user_text, context)

        st.subheader("🧠 Prompt Sent to Model")
        st.code(prompt)

        response = run_ollama(prompt)

        st.subheader("🤖 Response")
        st.write(response)

        # Simulated voice output
        if version in ["V4 - Voice Output (Simulated)", "V5 - Full Assistant"]:
            st.audio(None)
            st.info("🔊 (This is where TTS would play)")