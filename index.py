from gtts import gTTS
import os

try:
    with open("demo.txt", "r") as file:
        for line in file:
            tts = gTTS(text=line.strip(), lang='en')
            tts.save("temp.mp3")
            os.system("afplay temp.mp3")  # macOS specific command to play audio
            os.remove("temp.mp3")  # Remove the temporary audio file
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print("An error occurred:", e)
#https://github.com/hariharan1476