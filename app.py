from transformers import BlenderbotTokenizer, TFBlenderbotForConditionalGeneration
import streamlit as st
import nltk
import tensorflow as tf  # Ensure TensorFlow is available

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load BlenderBot model & tokenizer (TensorFlow version)
model_name = "facebook/blenderbot_small-90M"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = TFBlenderbotForConditionalGeneration.from_pretrained(model_name)

def healthcare_chatbot(user_input):
    # Predefined responses for medical-related queries
    if "symptom" in user_input.lower():
        return "It seems like you are experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input.lower():
        return "Would you like to schedule an appointment with your doctor?"
    elif "medication" in user_input.lower():
        return "It's important to take prescribed medication regularly. If you have concerns, please consult your doctor."

    # Generate response from BlenderBot model (TensorFlow)
    inputs = tokenizer(user_input, return_tensors="tf")
    reply_ids = model.generate(**inputs)
    response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    return response  # Extract chatbot’s reply

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?")

    if st.button("Submit"):
        if user_input:
            st.write("User:", user_input)
            with st.spinner("Processing... please wait..."):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant:", response)
        else:
            st.write("No input provided, please enter a message.")

if __name__ == "__main__":
    main()
