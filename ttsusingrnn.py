import pyttsx3

text_speech = pyttsx3.init()

answer = input("What you want to convert to speech? ")
rate = text_speech.getProperty('rate')
text_speech.setProperty('rate',rate-100)
# voices = text_speech.getProperty('voices')
# for voice in voices :
#     text_speech.setProperty('voice',voice.id)


text_speech.say(answer)
text_speech.runAndWait() 