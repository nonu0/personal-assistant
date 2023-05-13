import speech_recognition as sr
import pyttsx3
import spacy
import wikipedia
import wolframalpha
import webbrowser

# Initialize speech recognition engine and text-to-speech engine
engine = pyttsx3.init()
voices = engine.getproperty('voices')
engine.setproperty('voice',voices[0].id)
activation_word = 'computer'

def speak(text,rate = 120):
    """
    Use text-to-speech engine to speak the given text.
    """
    engine.setproperty('rate',rate)
    engine.say(text)
    engine.runAndWait()

def get_input():

    listener = sr.Recognizer()
    print('Listening...')
    """
    Use speech recognition to get user input.
    """
    with sr.Microphone() as source:
        listener.pause_threshold = 2
        # r.adjust_for_ambient_noise(source)
        # print("Listening...")
        input_speech = listener.listen(source)

    try:
        print('Recognizing speech')
        # Use Google speech recognition API to convert speech to text
        query = listener.recognize_google(input_speech,language='eng_gb')
        print("You said: " + query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def process_input(text):
    """
    Process user input and perform actions or provide responses as appropriate.
    """
    # nlp = spacy.load('en_core_web_sm')
    # doc = nlp(text)
    # entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Check for keywords in user input
    if "hello" in text or "hi" in text:
        speak("Hello, how can I help you?")
    elif "thank you" in text:
        speak("You're welcome!")
    elif "set a reminder" in text and "for" in text and entities:
        for entity in entities:
            if entity[1] == "DATE":
                speak(f"Okay, I will remind you on {entity[0]}")
                # Add code to set a reminder for the specified date
                break
    elif "search" in text:
        # Extract search query from user input
        query = text.replace("search", "").strip()
        speak(f"Searching the internet for {query}...")
        # Add code to search the internet for the specified query
    else:
        speak("Sorry, I didn't understand that.")

# Main loop
if __name__ == '__main__':
    print("All systems are a go")
    speak("All systems are a go",120)
    while True:
        user_input = get_input().lower().split()
        if user_input[0] == activation_word:
            user_input.pop(0)
            process_input(user_input)
