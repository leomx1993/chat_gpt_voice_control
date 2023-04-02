import openai 
import requests
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga algo...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language='pt-BR')
    print("Você disse: {}".format(text))
except sr.UnknownValueError:
    print("Não foi possível reconhecer o áudio.")
except sr.RequestError as e:
    print("Erro ao solicitar o serviço de reconhecimento de fala; {0}".format(e))

def txt_chatgpt (text):
  openai.api_key = "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"

  url = "https://api.openai.com/v1/engines/text-davinci-002/completions"
  prompt= text

  params = {
      "prompt": prompt,
      "max_tokens": 500,
      "n": 1,
      "stop": None,
      "temperature": 0.7
    }

  response = requests.post(url, headers={"Authorization": f"Bearer {openai.api_key}"}, json=params)

  if response.status_code != 200:
      print(f"Erro ao gerar resposta: {response.text}")
  else:
      data = response.json()
      text = data["choices"][0]["text"]
      print(text)

txt_chatgpt(text)
