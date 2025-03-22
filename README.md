ERPal - AI Avatar Assistant for ERP Support
🚀 AI-powered Avatar Assistant for seamless ERP support, featuring voice & text interaction, real-time knowledge retrieval, and AI-driven responses.

🔹 Overview
ERP systems can be complex, making it difficult for users to find the information they need quickly. AI Avatar Assistant for ERP Support is an intelligent, interactive assistant designed to simplify ERP navigation using AI-driven text and voice support. With a lip-synced avatar, knowledge base integration, and LLM-powered fallback, it provides instant, engaging, and efficient responses to ERP-related queries.

✨ Features
✅ Dual Input Modes – Supports text & voice queries.
✅ Knowledge Base Integration – Retrieves ERP-specific information.
✅ AI Fallback Mechanism – Uses LLMs (Large Language Models) when answers aren’t found.
✅ Text-to-Speech (TTS) – Converts AI responses into natural speech.
✅ Animated Avatar – Lip-synced assistant for interactive user experience.
✅ Intuitive UI – Built with React, offering a seamless chat interface.
✅ Scalable & Adaptive – Can be extended to multiple ERP platforms & languages.

🛠️ Technology Stack
Frontend:
React.js – UI development

Backend:
Python – Core processing

Hugging Face Transformers, Sentence Transformers – AI text generation

PyTorch – Machine learning models

APIs & Integrations:
Eleven Labs API – Text-to-Speech (TTS)

D-ID API – Avatar lip-syncing & animation

OpenAI API – AI-driven responses

SpeechRecognition, Pydub, Imageio_ffmpeg – Speech-to-text conversion

📌 Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/AI-Avatar-ERP.git
cd AI-Avatar-ERP
2️⃣ Install Dependencies
Frontend
bash
Copy
Edit
cd frontend
npm install
Backend
bash
Copy
Edit
cd backend
pip install -r requirements.txt
3️⃣ Set Up API Keys
Obtain API keys for OpenAI, Eleven Labs, and D-ID.

Create a .env file in both frontend and backend directories.

Add API keys:

bash
Copy
Edit
OPENAI_API_KEY=your_openai_api_key
ELEVEN_LABS_API_KEY=your_eleven_labs_api_key
D_ID_API_KEY=your_did_api_key
4️⃣ Run the Application
Start Backend Server
bash
Copy
Edit
cd backend
python app.py
Start Frontend
bash
Copy
Edit
cd frontend
npm start
🚀 Usage
1️⃣ Open the web application.
2️⃣ Type or speak an ERP-related query.
3️⃣ The assistant searches the knowledge base.
4️⃣ If no match is found, it queries OpenAI.
5️⃣ AI response is converted into natural speech & lip-synced avatar animation.
6️⃣ View responses in chat history.
