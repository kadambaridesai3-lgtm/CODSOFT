def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day 😊")
            break

        elif user_input in ["hi", "hello", "hey"]:
            print("🤖 Chatbot: Hello! How can I help you?")

        elif "your name" in user_input:
            print("🤖 Chatbot: I am a simple rule-based chatbot.")

        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm doing great!")

        elif "college" in user_input:
            print("🤖 Chatbot: I can help you with AI projects and coding!")

        elif "ai" in user_input:
            print("🤖 Chatbot: AI stands for Artificial Intelligence.")

        elif "thank you" in user_input:
            print("🤖 Chatbot: You're welcome 😊")

        elif "help" in user_input:
            print("🤖 Chatbot: You can ask me about AI, college, greetings, etc.")

        else:
            print("🤖 Chatbot: Sorry, I don't understand. Can you rephrase?")


# IMPORTANT: Run the chatbot
chatbot()