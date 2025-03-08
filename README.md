# AI_chatbot
# Healthcare Assistant Chatbot

This is a **Streamlit-based Healthcare Chatbot** that provides assistance by responding to medical-related queries using a combination of **predefined responses** and AI-generated answers from **BlenderBot (facebook/blenderbot_small-90M)**. The chatbot is designed to help users with general healthcare-related questions but is not a replacement for professional medical advice.

## 🚀 Features
- Provides **predefined responses** for common healthcare-related queries (e.g., symptoms, medication, appointments).
- Uses **BlenderBot**, an AI-based conversational model, for more dynamic responses.
- **Streamlit UI** for easy interaction.
- **Loading indicator** to show processing time.

## 🛠️ Tech Stack
- **Python** (Primary Language)
- **Transformers Library** (for BlenderBot AI model)
- **Streamlit** (for UI)
- **NLTK** (for text processing)

## 📦 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/healthcare-chatbot.git
cd healthcare-chatbot
```

### 2️⃣ Install Dependencies
Make sure you have Python 3.8+ installed, then run:
```sh
pip install -r requirements.txt
```
If you don't have PyTorch installed, install it with:
```sh
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### 3️⃣ Run the Chatbot
```sh
streamlit run app.py
```

## 📝 How It Works
1. The user enters a query in the input field.
2. The chatbot first checks for predefined responses based on keywords.
3. If no predefined response is found, it generates a response using BlenderBot.
4. The chatbot displays the response in the Streamlit UI.

## 🏥 Example Queries
- "I'm experiencing a fever and cough."
- "Can I schedule a doctor's appointment?"
- "What are the side effects of this medication?"
- "Tell me something about mental health."

## ⚠️ Disclaimer
This chatbot is **not a replacement for professional medical advice**. If you have a medical emergency, please consult a healthcare professional.

## 📌 Future Improvements
- Integrate a **speech-to-text** feature for voice interaction.
- Add **appointment booking functionality**.
- Improve **natural language understanding** with better models.

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📜 License
This project is licensed under the MIT License.

---

Feel free to modify as needed! 🚀


