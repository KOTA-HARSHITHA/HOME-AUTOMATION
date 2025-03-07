import speech_recognition as sr
import pyttsx3
import datetime
import cv2
import pywhatkit



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def talk(text):
    for voice in voices:
    #print(voice, voice.id)
        engine.setProperty('voice', voice.id)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        
        
def take_command():
    global command
    try:       
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice,language='en-in')
            command = command.lower()
            if 'alexa' not in command:
                command = command.replace('alexa', '')
                #print(command)
    except:
        pass
    return command
    

def run_alexa():
    global counter
    global Name
    command = take_command()
    print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'register my face' in command:
        camera=cv2.VideoCapture(0)
        Name=input("enter your name: ")
        for i in range(10):
            return_value, image = camera.read()
            cv2.imwrite(Name+str(i)+'.png', image)
        del(camera)
        file=open("F:/actors.csv","a")
        file.write("\n"+str(counter)+","+Name+",C:/Users/DELL/OneDrive/Desktop/Project/"+Name+"5.png")
        file.close()  
     
    
counter = 0        
while True:
    run_alexa()
    counter +=1      