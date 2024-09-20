intents = {
    "greet": ["hello", "hi", "hey", "howdy", "hola", "greetings", "good morning", "good afternoon", "good evening"],
    "goodbye": ["goodbye", "bye", "see you", "see you later", "adios", "cya"],
    "thanks": ["thanks", "thank you", "thx"],
    "search": ["search", "find", "look up", "search for"],
}

def get_intent(text):
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in text:
                return intent
    return None

question = "i go now"
intent = get_intent(question)
print(intent)  