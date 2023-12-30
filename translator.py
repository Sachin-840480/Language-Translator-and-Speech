import gtts
from playsound import playsound
from translate import Translator
import sys

lang_code = 'hi'    #Default Lang-code

if len(sys.argv) < 2 or len(sys.argv) >= 3:           #Helps the user to Change the lang_code correctly.
        print("Running Default 'hindi'")
        print("Usage: translator.py <lang-code>  | Ex: 'ja', 'hi, 'mr'..etc\n")

else:
    lang_code = sys.argv[1]
    print(f"Running Language: \"{lang_code}\"\n")

translator = Translator(to_lang = lang_code)

try:
    with open('./translate.txt', mode ='r') as file:
        text = file.read()
        translation = translator.translate(text)
        print('Translation Successful')

        with open('./translated.txt', mode ='w', encoding = 'utf-8') as file2:
            file2.write(translation)
            print("Please check the newly Generated 'Translated.txt' file.")

    with open('./translated.txt', mode ='r', encoding = 'utf-8') as file:
        text = file.read()
        t1 = gtts.gTTS(text = text, lang = lang_code)
        t1.save('speak.mp3')
         
        # Use a relative path to play the 'welcome.mp3' file
        playsound('speak.mp3')

        print('Audio Playback Successful')

except FileNotFoundError:
    print('Please check the file path.')