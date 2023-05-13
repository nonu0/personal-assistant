import speech_recognition as sr
from datetime import datetime
import pyttsx3
import spacy
import wikipedia
import wolframalpha
import webbrowser

# Initialize speech recognition engine and text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
activation_word = 'computer'
appId = 'VRR945-924YJ3UVA9'
wolframaClient = wolframalpha.Client(appId)

def listorDict(var):
    if isinstance(var,list):
        return var[0]['plaintext']
    else:
        return var['plaintext']
    
# chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
def speak(text,rate = 120):
    """
    Use text-to-speech engine to speak the given text.
    """
    engine.setProperty('rate',rate)
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
        # listener.adjust_for_ambient_noise(source)
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

    elif "search" in text or 'go' in text or 'find' in text:
        query_str = ' '.join(text[2:])
        print("Searching the web")
        print(query_str)
        speak("Searching the web")
        # query = text.pop(0)
        webbrowser.open_new_tab(query_str)
        
    elif 'wikipedia' in text:
        query = ' '.join(text[2:])
        speak('Querying the universal database')
        result = wikipedia_search(query)    
        speak(result)
    elif 'compute' in text:
        query = ' '.join(text[1:])
        print('computing...')
        result = wolframalpha_result(query)
    elif 'log' in text or 'record' in text:
        speak('Ready to record  your note')
        newNote = get_input().lower()
        now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        with open('Note_%s.txt' % now ,'w') as newFile:
            newFile.write(newNote)
            speak('New note written')
    else:
        speak("Sorry, I didn't understand that.")
    # if 'exit' in text:
    #     speak("Goodbye")
    #     break
def wikipedia_search(query= ''):
    wikiresult = wikipedia.search(query)
    if not wikiresult:
        print("I didn't quite catch that")
        return 'No results found'
    try:
        wikipage = wikipedia.page(wikiresult[0])
    except wikipedia.DisambiguationError as e:
        wikipage = wikipedia.page(e.options[0])
    print(wikipage.title)
    wikisummary = str(wikipage.summary)
    return wikisummary

def wolframalpha_result(query=''):
    response = wolframaClient.query(query)
    speak(response)
    if response['@success'] == 'false':
        return "couldn't compute"
    else:
        result = ''
        pod0 = response['pod'][0]
        pod1 = response['pod'][1]
        if (('result') in pod1['@title'].lower() or (pod1.get('@primary','false') == 'true' or ('definition' in pod1['@title'].lower()))):
            result = listorDict(pod1['subpod'])
            return result.split('(')[0]
        else:
            question = listorDict(pod0['subpod'])
            return question.split('(')[0]
            speak('Computation failed,querying the question in the universal database')
            return wikipedia_search(question)
# Main loop
if __name__ == '__main__':
    print("All systems are a go")
    speak("All systems are a go",120)
    while True:
        user_input = get_input().lower().split()
        if user_input[0] == activation_word:
            user_input.pop(0)
            process_input(user_input)
        
