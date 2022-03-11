from pynput.keyboard import Key, Controller
import speech_recognition as sr
keyboard = Controller()

# new window / tab
# with keyboard.pressed(Key.cmd):
#     #WINDOW
#     # keyboard.press('l')
#     # keyboard.release('l')
#     #TAB
#     keyboard.press('t')
#     keyboard.release('t')



#URL ENTRY
# with keyboard.pressed(Key.cmd):
#     keyboard.press('l')
#     keyboard.release('l')

# keyboard.type("twitter.com")
# keyboard.press(Key.enter)


# incognito window
# with keyboard.pressed(Key.cmd):
#     with keyboard.pressed(Key.shift):
#         keyboard.press('n')
#         keyboard.release('n')

'''

SAFARI/CHROME COMMANDS

CMD + L --> go to search bar
CMD + N --> new window
CMD + O --> open
    # needs to be integrated with leap motion for file selection
CMD + SHIFT + N --> incognito window

'''



r = sr.Recognizer()
mic = sr.Microphone()

def recognize_audio(r, mic):
    transcript = None
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            transcript = r.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            # response["success"] = False
            # response["error"] = "API unavailable"
            print("API unavailable")
        except sr.UnknownValueError:
            # speech was unintelligible
            # response["error"] = "Unable to recognize speech"
            print("unable to recognize speech")
    return transcript


def contains_url(transcript):
    words = transcript.split(' ')
    for w in words:
        if ".com" in w:
            return w
    return ""

def scrape_transcript_for_commands(transcript):
    print("tab" in transcript)
    if "tab" in transcript:
        print("tab in transcript")
        with keyboard.pressed(Key.cmd):
            keyboard.press('t')
            keyboard.release('t') 
        print('pressed keyboard')
    if "window" in transcript:
        with keyboard.pressed(Key.cmd):
            keyboard.press('n')
            keyboard.release('n')
    else:
        url = contains_url(transcript)
        if url != "":
            with keyboard.pressed(Key.cmd):
                keyboard.press('l')
                keyboard.release('l')

            keyboard.type(url)
            keyboard.press(Key.enter)


if __name__ == "__main__":
    r = sr.Recognizer()
    mic = sr.Microphone() 
    try:
        while True:
            transcript = recognize_audio(r, mic)
            if transcript is not None:
                print("recognized speech:", transcript)
                scrape_transcript_for_commands(transcript)
            else:
                print("could not recognize speech. Try again!")
    except KeyboardInterrupt:
        print("Quitting Application") 
    pass