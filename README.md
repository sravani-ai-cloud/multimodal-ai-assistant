# multimodal-ai-assistant
Multimodal AI Assistant using Streamlit, Ollama (TinyLlama), and Tesseract OCR
#  Multimodal AI Assistant

This project is a multimodal AI assistant that processes text and image inputs using a local LLM.

##  Tech Stack
- Python
- Streamlit
- Ollama (TinyLlama)
- Tesseract OCR

##  Features
- Text-based Q&A
- Image to text extraction (OCR)
- Structured data extraction
- Multiple assistant modes (V0–V5)

##  How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the app:
streamlit run app.py

3. Make sure Ollama is installed:
ollama pull tinyllama

##  Future Improvements
- Add RAG (Retrieval-Augmented Generation)
- Add vector database (FAISS)
- Improve model performance
