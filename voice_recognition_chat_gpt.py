import openai 
import requests
import speech_recognition as sr

### Voice to text transformation 

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language='your_langauge')
    print("You said: {}".format(text))
except sr.UnknownValueError:
    print("Voice not detected. Try again please...")
except sr.RequestError as e:
    print("Error requesting speech recognition service; {0}".format(e))

### Connecting and interacting to Chatgpt 

def txt_chatgpt (text):
  openai.api_key = "your_chatgpt_api_key"

  url = "url"
  prompt= text

  params = {
      "prompt": prompt,
      "max_tokens": 500,
      "n": 1,
      "stop": None,
      "temperature": 0.7
    }

### Chatgpt response 

  response = requests.post(url, headers={"Authorization": f"Bearer {openai.api_key}"}, json=params)

  if response.status_code != 200:
      print(f"Error generating response: {response.text}")
  else:
      data = response.json()
      text = data["choices"][0]["text"]
      print(text)

txt_chatgpt(text)