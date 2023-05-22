from pyperclip import copy as Copiar
from gtts import gTTS
import openai
import vlc

"""
librerias:
pip install pyperclip
pip install python-vlc
pip install openai
pip install gTTS
"""

def hablar(texto):
    dialogo = gTTS(text = texto, lang = "es-us", slow = False)
    dialogo.save("dialogo.mp3")
    repr = vlc.MediaPlayer("dialogo.mp3")
    repr.play()
    #repr.stop() #sirve para pausar la reproducción xd

openai.api_key = "sk-5AskfZc7v1xkgL6hKelnOBC1z0OojT3BlbkFJd3w08toY72C"

def pensar(pregunta): #esto genera el texto
    completion = openai.Completion.create(engine="text-davinci-003", prompt=pregunta, max_tokens=4000)
    return completion.choices[0].text
try:
    hablar("Hola! Bienvenido!!!")
except: None

print("""Bienvenido!!!

Soy una interfaz de preguntas creada por @Brick_Briceno ¿en que puedo ayudarte? :D

Trucos:

para Salir solo escriba "salir"
para Repetir la respuesta solo escriba "repite"
para Copiar la respuesta al portapepeles solo escriba "copiar"
para Activar o Decativar la Voz solo escriba "voz"


""")

voz = True

while True:
    pregunta = input("Tu: ")

    if pregunta == "salir":
        print("Chaooo :D")
        break

    elif pregunta == "repite":
        repr = vlc.MediaPlayer("dialogo.mp3")
        repr.play()
    
    elif pregunta == "copiar":
        Copiar(respuesta)
        print("Texto Copiado!")

    elif pregunta == "voz":
        voz = not(voz)
        if voz:
            print("Voz activada")
        else:
            print("Voz desactivada")
        try:
            repr.stop()
        except: None

    else:
        try:
            respuesta = pensar(pregunta)
            if voz:
                try:
                    hablar(respuesta)
                except None:
                    print("Olvidé como hablar, lo siento")
                    voz = not(voz)
                    print("Voz desactivada")
            print("\nIA:" + respuesta + "\n")
        except:
            print("\nOh hubo un error :(\nIntente una vez más! :D")#esto por si hay un error en el servidor
