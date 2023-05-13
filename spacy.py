# import speech_recognition as sr
# import pyttsx3
# import spacy

# # Initialize speech recognition engine and text-to-speech engine
# r = sr.Recognizer()
# engine = pyttsx3.init()

# # Load spaCy model
# nlp = spacy.load('en_core_web_sm')

# def speak(text):
#     """
#     Use text-to-speech engine to speak the given text.
#     """
#     engine.say(text)
#     engine.runAndWait()

# # def get_input():
# #     """
# #     Use speech recognition to get user input.
# #     """
# #     with sr.Microphone() as source:
# #         r.adjust_for_ambient_noise(source)
# #         print("Listening...")
# #         audio = r.listen(source)

# #     try:
# #         # Use Google speech recognition API to convert speech to text
# #         text = r.recognize_google(audio)
# #         print("You said: " + text)
# #         return text
# #     except sr.UnknownValueError:
# #         print("Sorry, I didn't understand that.")
# #         return ""
# #     except sr.RequestError as e:
# #         print("Could not request results from Google Speech Recognition service; {0}".format(e))
# #         return ""

# # def process_input(text):
# #     """
# #     Process user input and perform actions or provide responses as appropriate.
# #     """
# #     doc = nlp(text)
# #     entities = [(ent.text, ent.label_) for ent in doc.ents]
    
# #     # Check for keywords in user input
# #     if "hello" in text.lower() or "hi" in text.lower():
# #         speak("Hello, how can I help you?")
# #     elif "thank you" in text.lower():
# #         speak("You're welcome!")
# #     elif "set a reminder" in text.lower() and "for" in text.lower() and entities:
# #         for entity in entities:
# #             if entity[1] == "DATE":
# #                 speak(f"Okay, I will remind you on {entity[0]}")
# #                 # Add code to set a reminder for the specified date
# #                 break
# #     elif "search" in text.lower():
# #         # Extract search query from user input
# #         query = text.lower().replace("search", "").strip()
# #         speak(f"Searching the internet for {query}...")
# #         # Add code to search the internet for the specified query
# #     else:
# #         speak("Sorry, I didn't understand that.")

# # # Main loop
# # while True:
# #     user_input = get_input()
# #     process_input(user_input)
