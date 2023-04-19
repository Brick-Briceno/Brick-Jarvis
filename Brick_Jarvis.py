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


openai.api_key = "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"

def pensar(pregunta): #esto genera el texto
    completion = openai.Completion.create(engine="text-davinci-003", prompt=pregunta, max_tokens=4000)
    return completion.choices[0].text

hablar("Hola! Bienvenido!!!")
 
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
        print("Copiado!")

    elif pregunta == "voz":
        voz = not(voz)

    else:
        try:
            respuesta = pensar(pregunta)
            if voz:
                hablar(respuesta)
            print("IA:" + respuesta + "\n")
        except:
            print("\nOh hubo un error :(\nIntente una vez más! :D")#esto por si hay un error en el servidor
