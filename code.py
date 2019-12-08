pip install PyAudio
pip install SpeechRecognition

import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
  print('At your service')
  audio=r.listen(source)

  try:
    text = r.recognize_google(audio)
    print('you said : {}'.format(text))
  except:
    print("Sorry coudn't recognize your voice")
