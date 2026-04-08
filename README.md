#  Multimodal AI Assistant 
## Demo
[Multimodal AI Assistant](screenshots/demo.png)
Streamlit-based Multimodal AI Assistant supporting text, image (OCR), and prompt-based interactions.
## Architecture
This application follows a modular pipeline for processing multimodal inputs:
- User Input Layer: Accepts text, image, and simulated voice input  
- Frontend (Streamlit): Handles UI interactions and user input collection  
- OCR Layer (Tesseract): Extracts text from uploaded images  
- Prompt Engineering Layer: Formats structured prompts based on selected assistant version  
- LLM Layer (Ollama - TinyLlama): Generates responses using local inference  
- Output Layer: Displays results in the UI  
##  Tech Stack
- Python
- Streamlit (UI)
- Ollama (TinyLlama - Local LLM)
- Tesseract OCR (Image to Text)
## Features
- Text-based Q&A using local LLM  
- Image understanding via OCR  
- Structured data extraction (invoice details, etc.)  
- Multiple assistant modes (V0–V5 evolution)  
- Simulated voice input/output  
##  How to Run
1. Clone the repository
git clone https://github.com/sravani-ai-cloud/multimodal-ai-assistant.git
cd multimodal-ai-assistant
2. Install dependencies
pip install -r requirements.txt
3. Install and run Ollama
Download from: https://ollama.com
ollama pull tinyllama
4. Run the app
streamlit run app.py
##  Why this project?
This project demonstrates how to build a real-world multimodal AI system by integrating:
- Local LLM inference
- Image processing (OCR)
- Interactive UI
- Prompt engineering
It showcases practical GenAI application development beyond basic chatbot implementations.
##  Future Enhancements
- Add Retrieval-Augmented Generation (RAG)
- Integrate vector database (FAISS / Chroma)
- Add real voice input/output (Speech-to-Text & TTS)
- Upgrade to advanced models (Llama3, Mistral)

# Author
Sravani Koriginja
- LinkedIn: https://www.linkedin.com/in/sravani-koriginja
- GitHub: https://github.com/sravani-ai-cloud
