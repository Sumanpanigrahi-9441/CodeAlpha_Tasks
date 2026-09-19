def basic_chatbot():
    print("=== Basic Chatbot (Type 'bye' to exit) ===")
    
    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hi!")
        elif user_input in ["how are you", "how are you?"]:
            print("Bot: I'm fine, thanks!")
        elif user_input in ["bye", "goodbye"]:
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I'm sorry, I don't understand that. Try saying 'hello' or 'how are you'.")

if __name__ == "__main__":
    basic_chatbot()