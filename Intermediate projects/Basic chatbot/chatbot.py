import re


patterns = {
    r"\bhi\b|\bhello\b|\bhey\b":"Hello",
    r"\bhow are you?\b|\bhow about you?\b": "I'm good. How about you?",
    r"\bwho are you?\b": "I'm a mini chatbot developed by Anil Reddy",
    r"\bgood\b|\bwelcome\b": "Thanks. How can I help you?",
    r"\bwhat's your name?\b": "My name is Abhesshan. Thanks for asking."
}


def chatbot():
    print("Chatbot🤖: Hi, I'm a mini chatbot. How can I help you?")
    while True:
        user_input = input("You: ")
        if user_input == "exit":
            print("Bye!")
            break
        
        for pattern, response in patterns.items():
            matched = False
            if re.search(pattern, user_input):
                print("Chatbot🤖: ", response)
                matched = True
                break
        if not matched:
            print("Chatbot🤖: I didn't quite get you.")


chatbot()