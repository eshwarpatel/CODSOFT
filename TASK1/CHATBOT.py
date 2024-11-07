import re
import random

# Define a list of responses for each intent
responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What do you need assistance with?", "Greetings! How can I assist you?"],
    "farewell": ["Goodbye! Have a great day!", "See you later! Feel free to return if you have more questions.", "Take care!"],
    "how_are_you": ["I'm just a program, but thanks for asking! How can I assist you?", "Doing well, thank you! What can I do for you?"],
    "help": ["Sure! What do you need help with?", "I'm here to assist you! What can I do for you?"],
    "name": ["I am a simple rule-based chatbot created for assistance.", "You can call me Chatbot!"],
}

# Define patterns for intent recognition
patterns = {
    "greeting": r'\b(hello|hi|hey)\b',
    "farewell": r'\b(bye|exit|see you)\b',
    "how_are_you": r'\b(how are you|how do you do)\b',
    "help": r'\b(help|assist|support)\b',
    "name": r'\b(name|who are you)\b',
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    for intent, pattern in patterns.items():
        if re.search(pattern, user_input):
            return random.choice(responses[intent])
    
    return "I'm sorry, I didn't understand that. Can you please rephrase?"

def chat():
    print("Welcome to the advanced chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        if "bye" in user_input or "exit" in user_input:
            break

# Start the chatbot
chat()