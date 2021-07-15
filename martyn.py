import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki

speaker = pyttsx3.init()

rate = speaker.getProperty('rate')
speaker.setProperty('rate', 150)

"""VOICE"""
voices = speaker.getProperty('voices')       #getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female


listener = sr.Recognizer()


def speak(text):
    speaker.say(text)
    speaker.runAndWait()


def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()


def first_know(text):
    speaker.say(text)
    speaker.runAndWait()


va_name = 'martin'
speak_ex('I am ' + va_name + ', ' + 'your assistant, tell me boss')
# first_know('Please tell me your gender boss')


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print("I am listing......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if va_name in command:
                command = command.replace(va_name + ' ', '')
                # print(command)
                # speak(command)

    except:
        print("Can't recognize your voice!")
    return command


while True:
    user_command = take_command()
    if 'close' in user_command:
        print('see you boss.' + 'I will be back when ever you call.')
        speak('see you boss.' + ', ' + 'I will be back when ever you call.')
        break

    elif 'do you here me' in user_command or 'martin do you here me' in user_command or 'martin am i audible' in user_command:
        user_command = user_command.replace('do you here me', '')
        user_command = user_command.replace('martin do you here me', '')
        user_command = user_command.replace('martin am i audible', '')
        print('yes boss i am hearing you' + user_command)
        speak('yes boss i am hearing you' + user_command)

    elif 'time' in user_command:
        cur_time = dt.datetime.now().strftime("%I:%M %p")
        print(cur_time)
        speak(cur_time)

    elif 'how i am looking' in user_command:
        user_command = user_command.replace('how i am looking ', '')
        print('You are looking so handsome boss')
        speak('You are looking so handsome boss')

    elif 'good morning' in user_command:
        print('hello sir, good morning and have a nice day')
        speak('hello sir, good morning and have a nice day')

    elif 'whom do you like more' in user_command:
        print('I like my boss purnesh')
        speak('I like my boss purnesh')

    elif 'play' in user_command:
        user_command = user_command.replace('play ', '')
        print('playing ' + user_command + ' ' + 'enjoy boss')
        speak('playing ' + user_command + ' ' + 'enjoy boss')
        pk.playonyt(user_command)
        break

    elif 'where i am' in user_command:
        user_command = user_command.replace('where i am ', '')
        print('boss you are in India  andhra pradesh  state,  anathapur district,  dharmavaram mandel, near '
              'anapurneshwari temple')
        speak('boss you are in India  andhra pradesh state,  anathapur district,  dharmavaram mandel,  near '
              'anapurneshwari temple')

    elif 'print' in user_command:
        user_command = user_command.replace('print ', '')
        print(user_command)
        speak(user_command)

    elif 'who are you' in user_command:
        user_command = user_command.replace('who are you', user_command)
        print('I am your martin boss ')
        speak('I am your martin boss ')

    elif 'who developed you' in user_command:
        user_command = user_command.replace('who developed you', '')
        print('I am developed by poornesh ')
        speak('I am developed by poornesh ')

    elif 'who is your boss' in user_command:
        user_command = user_command.replace('who is your boss ', '')
        print('my boss is poornesh ')
        speak('my boss is poornesh ')

    elif 'how are you' in user_command:
        user_command = user_command.replace('how are you ', '')
        print('i am fine boss ')
        speak('i am doing fine boss, how are you doing ')

    elif 'i am doing fine' in user_command or 'i am fine' in user_command:
        user_command = user_command.replace('i am doing fine ', '')
        user_command = user_command.replace('i am doing fine ', '')
        print("that's grate boss")
        speak("that's grate boss")

    elif 'thank you' in user_command:
        user_command = user_command.replace('thank you ', '')
        print('your pleasure boss ')
        speak('your pleasure boss ')

    elif 'who is' in user_command or 'tell me about':
        user_command = user_command.replace('who is ', '')
        user_command = user_command.replace('tell me about ', '')
        info = wiki.summary(user_command, 1)
        print(info)
        speak(info)

    elif 'search for' in user_command or 'google' in user_command:
        user_command = user_command.replace('search for ', '')
        user_command = user_command.replace('google ', '')
        print('searching for' + user_command)
        speak('searching for' + user_command)
        pk.search(user_command)

    else:
        speak_ex('sorry boss , please say  it again.')

