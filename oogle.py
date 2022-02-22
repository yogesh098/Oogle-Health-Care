from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import roman
import pywhatkit
#from Class1 import Student
#import pytesseract
from PIL import Image
import requests
import pyjokes



numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
a = {'name':'your email'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
    # Method for the speaking of the the assistant
    engine.say(audio)
    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('prag890@gmail.com', '123@#yogesh') # email id - use any email id whose security/privacy is off
    server.sendmail('prag890@gmail.com', to, content)
    server.close()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning Maya, Myself Oogle!\n म तापईलाई के सहयोग गर्न  सक्छु. नलजाई  भन्नुष है.") 
        window.update()
        speak("Good Morning Maya!, Myself Oogle!\n Ma tapai lai k sahayog garna sakchu. Nalajai vannush hai.")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon Maya!, Myself Oogle!\n म तापईलाई के सहयोग गर्न  सक्छु. नलजाई  भन्नुष है.")
        window.update()
        speak("Good Afternoon Maya!,Myself Oogle!\n Ma tapai lai k sahayog garna sakchu. Nalajai vannush hai. ")
    else:
        var.set("Good Evening Maya, Myself Oogle!\n म तापईलाई के सहयोग गर्न  सक्छु. नलजाई  भन्नुष है.")
        window.update()
        speak("Good Evening Maya!, Myself Oogle!\n Ma tapai lai k sahayog garna sakchu. Nalajai vannush hai. ")

# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing

def takeCommand():
    r = sr.Recognizer()

    # from the speech_Recognition module 
    # we will use the Microphone module
    # for listening the command

    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        
        # seconds of non-speaking audio before 
        # a phrase is considered complete

        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized 
        # it is good else we will have exception 
        # handling 

    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        # for Listening the command in indian
        # english we can also use 'hi-In' 
        # for hindi recognizing
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query

def covid():
    btn2['state'] = 'normal'
    btn0['state'] = 'disabled'
    btn1['state'] = 'disabled'
    btn3['state'] = 'disabled'
    btn4['state'] = 'disabled'
    while True:
        var.set('Data from Nepal \nTotal case : 648,085\n Total death : 9263\n Total Recovered : 614,327\n New Cases : 1,718\n Not safe, Be Careful.')
        btn2['state'] = 'normal'
        btn0['state'] = 'normal'
        btn3['state'] = 'normal'
        btn4['state'] = 'normal'
        btn1['state'] = 'normal'
        window.update()
        speak('Data from Nepal Total case : 648,085  Total death : 9263 Total Recovered : 614,327 New cases : 1,718 Not safe, Be Careful.')

       # btn3.configure(bg = 'orange')
       #url = "https://api.covid19api.com/countries"
        #response = requests.get(url)
        #var.set(response.content)
        #window.update()
        #speak(response.content)
        #print(response.content)
        
        break
        


    

def register():
    return

def login():
    return

def jokes():
    btn2['state'] = 'normal'
    btn0['state'] = 'disabled'
    btn1['state'] = 'disabled'
    btn3['state'] = 'disabled'
    btn4['state'] = 'disabled'
    while True:
        
        var.set('Welcome to Programmer Jokes')
        btn2['state'] = 'normal'
        btn0['state'] = 'normal'
        btn3['state'] = 'normal'
        btn4['state'] = 'normal'
        btn1['state'] = 'normal'
        window.update()
        speak(pyjokes.get_joke())
        return

    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate 
    # the program
def play():
    btn3['state'] = 'disabled'
    btn4['state'] = 'disabled'
    btn2['state'] = 'normal'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    wishme()
    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir, आउदै गर्नुष है !! मलाई नाबिर्शी |")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            btn3['state'] = 'normal'
            btn4['state'] = 'normal'
            window.update()
            speak("Bye sir, Aaudai garnush hai. Malai nabirsi.")
            break

        elif 'search' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=1)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                    print(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')
        
        
        elif 'symptoms of corona' in query:
            var.set('Most Common Symptoms:\n   fever,\n dry cough,\n tiredness')
            window.update()
            speak('Most Common Symptoms:   fever, dry cough, tiredness')
        
        elif 'medicines used fever' in query:
            var.set('opening website')
            window.update()
            speak('Opening best website')
            




#Medicine info

        elif'paracetamol' in query:
            if 'paracetomal' in query:
                speak('Paracetamol, also known as acetaminophen, is a medication used to treat fever and mild to moderate pain.')
            else:
                var.set('Paracetamol, also known as acetaminophen, is a medication used to treat fever and mild to moderate pain.')
                window.update()
                speak('Paracetamol, also known as acetaminophen, is a medication used to treat fever and mild to moderate pain.')
                speak('Opening best website')
                webbrowser.open('en.wikipedia.org/wiki/Paracetamol')

        elif 'anaesthetic' in query:
            var.set('opening website')
            window.update()
            speak('Opening best website')
            webbrowser.open('en.wikipedia.org/wiki/Anesthetic')
        
        elif 'ketamine' in query:
            var.set('opening website')
            window.update()
            speak('Ketamine is a medication that is used to induce loss of consciousness, or anesthesia.')
            speak('Opening best website')
            webbrowser.open('www.medicalnewstoday.com/articles/302663')
        
        elif 'bupivacaine' in query:
            var.set('opening website')
            window.update()
            speak('upivacaine is a prescription medication used as a local anesthetic')
            speak('Opening best website')
            webbrowser.open('www.rxlist.com/consumer_bupivacaine_marcaine_sensorcaine/drugs-condition.htm')
        
        elif 'atropine' in query:
            var.set('opening website')
            window.update()
            speak('Opening best website')
            webbrowser.open('www.rxlist.com/atropine-drug.htm')
        
        elif 'morphine' in query:
            var.set('opening website')
            window.update()
            speak('Opening best website')
            webbrowser.open('medlineplus.gov/druginfo/meds/a682133.html')
        
        elif 'promethazine' in query:
            var.set('opening website')
            window.update()
            speak('Opening best website')
            webbrowser.open('www.drugs.com/promethazine.html')
        
        elif 'acetylsalicylic acid' in query:
            var.set('opening website')
            window.update()
            speak('opeaning best website')
            webbrowser.open('go.drugbank.com/drugs/DB00945')

        elif 'morphine' in query:
            var.set('opening website')
            window.update()
            speak('opeaning best website')
            webbrowser.open('medlineplus.gov/druginfo/meds/a682133.html')

        elif 'gout' in query:
            if 'gout' in query:
                print("Meidcine is alopurinol")
            else:
                var.set('opening website')
            window.update()
            speak('opeaning best website')
            webbrowser.open('medlineplus.gov/druginfo/meds/a682673.html')

        elif 'chlorpheniramine' in query:
            var.set('opening website')
            window.update()
            speak('opeaning best website')
            webbrowser.open('https://www.drugs.com/mtm/chlorpheniramine.html')
        
        elif 'dexamethasone' in query:
            var.set('opening website')
            window.update()
            speak('opeaning best website')
            webbrowser.open('www.medicalnewstoday.com/articles/322409#warnings')
        
        elif 'adrenaline' in query:
            var.set('opening website')
            window.update()
            speak('opeaning best website')
            webbrowser.open('www.rxlist.com/adrenalin-drug.htm')
        
        elif 'hospital' in query:
            var.set('opening website')
            window.update()
            speak('opeaning website')
            webbrowser.open('https://www.google.com/search?q=hospitals+near+me&sxsrf=ALeKk02UASrxsCiNv0YmPXXcUyf340TKow%3A1625627491418&ei=YxvlYJSCGY7Wz7sPsKWOgAc&oq=hospitals+near+me&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEMyAggAMgIIADICCAAyAggAMgIIADICCAAyBAgAEEMyAggAMgIIADoHCAAQRxCwA0oECEEYAFDcB1jcB2CwDWgAcAN4AIABlgKIAYAEkgEDMi0ymAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=gws-wiz&ved=0ahUKEwjUv6ap_s_xAhUO63MBHbCSA3AQ4dUDCA4&uact=5')

        elif 'medical' in query:
            var.set('opening website')
            window.update()
            speak('opening website')
            webbrowser.open("https://www.google.com/search?q=medicals+near+me&sxsrf=ALeKk024iVW71Y_ThzIoU9IP81O2ispLiQ%3A1625627494669&ei=ZhvlYJ6tKLfbz7sP6Kq-uAM&oq=medicals+near+me&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEMQCMgYIABAHEB4yCAgAEAcQChAeMggIABAHEAoQHjIICAAQBxAKEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeOgsIABCSAxDhAxCwAzoHCAAQRxCwAzoQCC4QxwEQrwEQsAMQyAMQQ0oFCDgSATFKBAhBGABQ5t8FWI7oBWD26QVoAXACeAGAAdgCiAHdDZIBBzAuNy4xLjGYAQCgAQGqAQdnd3Mtd2l6yAEMwAEB&sclient=gws-wiz&ved=0ahUKEwie-Oyq_s_xAhW37XMBHWiVDzcQ4dUDCA4&uact=5")

        

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")
        
        elif "play" in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'open course error' in query:
            var.set('opening course era')
            window.update()
            speak('opening course era')
            webbrowser.open("coursera.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'hello' in query:
            var.set('Hello, तपाई लाइ मेरो दुनिया मा स्वागत छ !!')
            window.update()
            speak("Hello, Tapai lai mero duniya ma swagat cha.")
        
        elif 'love you' in query:
            var.set('तेस्तो  नभन्नुस है . I am in love with Oogle.')
            window.update()
            speak("Testo Navannush hai. I am in love with Oogle.")
			
        elif 'open stackoverflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif (' music' in query) or ('change music' in query):
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = 'D:\My Music\Favourites' # Enter the Path of Music Library
            songs = os.listdir(music_dir)
            n = random.randint(0,27)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" %strtime)

        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate) 

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        elif 'can you do for me' in query:
            var.set('I can do multiple tasks for you sir. tell me whatever you want to perform sir')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

        elif 'old are you' in query:
            var.set("I am a little baby sir")
            window.update()
            speak("I am a little baby sir")

        elif 'open media player' in query:
            var.set("opening VLC media Player")
            window.update()
            speak("opening V L C media player")
            path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe" #Enter the correct Path according to your system
            os.startfile(path)

        elif 'your name' in query:
            var.set("Myself Oogle Sir")
            window.update()
            speak('myself Oogle sir')
        
        elif 'ok' in query:
            var.set('Yes, sir.')
            window.update()
            speak('Yes sir')

        elif 'who creates you' in query:
            var.set('My Creator is Mr. Yogesh Singh')
            window.update()
            speak('My Creator is Mr. Yogesh Singh')

        elif 'say hello' in query:
            var.set('Hello Everyone! My self Oogle')
            window.update()
            speak('Hello Everyone! My self Oogle')

        elif 'open pycharm' in query:
            var.set("Openong Pycharm")
            window.update()
            speak("Opening Pycharm")
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2018.3.2\\bin\\pycharm64.exe" #Enter the correct Path according to your system
            os.startfile(path)

        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" #Enter the correct Path according to your system
            os.startfile(path)

        elif 'email to me' in query:
            try:
                var.set("What should I say")
                window.update()
                speak('what should I say')
                content = takeCommand()
                to = a['name']
                sendemail(to, content)
                var.set('Email has been sent!')
                window.update()
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                var.set("Sorry Sir! I was not able to send this email")
                window.update()
                speak('Sorry Sir! I was not able to send this email')
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
		
        elif "open python" in query:
            var.set("Opening Python Ide")
            window.update()
            speak('opening python Ide')
            os.startfile('C:\\Users\\mridu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.7\\IDLE (Python 3.7 64-bit)')

        elif 'calculation' in query:
            sum = 0
            var.set('Yes Sir, please tell the numbers')
            window.update()
            speak('Yes Sir, please tell the numbers')
            while True:
                query = takeCommand()
                if 'answer' in query:
                    var.set('here is result'+str(sum))
                    window.update()
                    speak('here is result'+str(sum))
                    break
                elif query:
                    if query == 'x**':
                        digit = 30
                    elif query in numbers:
                        digit = numbers[query]
                    elif 'x' in query:
                        query = query.upper()
                        digit = roman.fromRoman(query)
                    elif query.isdigit():
                        digit = int(query)
                    else:
                        digit = 0
                    sum += digit
        

        elif 'click photo' in query:
            stream = cv2.VideoCapture(0)
            grabbed, frame = stream.read()
            if grabbed:
                cv2.imshow('pic', frame)
                cv2.imwrite('pic.jpg',frame)
            stream.release()

        elif 'record video' in query:
            cap = cv2.VideoCapture(0)
            out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret:
                    
                    out.write(frame)

                    cv2.imshow('frame',frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            out.release()
            cv2.destroyAllWindows()
        '''
        elif 'read the photo' in query: #If you have Pytesseract installed for Optical Character Recognition
            try:
                im = Image.open('pic.jpg')
                text = pytesseract.image_to_string(im)
                speak(text)
            except Exception as e:
                print("Unable to read the data")
                print(e)
            '''
               

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)
    


label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable=var, bg = '#ADD8E6')
label1.config(font=("Arial", 14))
var.set('Welcome to my world')
label1.pack()

Output = Label(window, height = 5, width = 95, )
Output.pack()

frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('Health Assistant OOGLE')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)


btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()

btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()

btn3 = Button(text = 'COVID UPDATE',width = 20,command = covid, bg = '#5C85FB')
btn3.config(font=("Courier", 12))
btn3.pack()

btn4 = Button(text = 'JOKES',width = 20,command = jokes, bg = '#5C85FB')
btn4.config(font=("Courier", 12))
btn4.pack()

btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()

window.mainloop()