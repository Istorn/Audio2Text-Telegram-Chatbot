"""
    Lorenzo Neri - hello@lorenzoneri.com 

    http://lorenzoneri.com

    Chatbot Telegram in grado di convertire le note audio in messaggi testuali

    Questo codice è regolato dalla licenza Creative Commons CC BY-NC 4.0
    https://creativecommons.org/licenses/by-nc/4.0/


    Cosa puoi farci:


    - Condividi: copia e ridistribuisci il materiale in qualsiasi mezzo o formato
    - Adatta: remixa, trasforma e costruisci sul materiale 

    A che condizioni: citandomi!

    Cosa NON puoi farci:

    Usare la codebase a scopi commerciali
"""

import telegram
import requests
import speech_recognition as sr
from pydub import AudioSegment

# chatbot token
token="il_tuo_chatbot_token"

# istanzio il chatbot
chatbot=telegram.Bot(token=token)

# ciclo never ending
while True:
    latests=[]
    try:
        latests=chatbot.getUpdates()
    except Exception as e:
        print(f"Errore di time out: {str(e)}")
        pass

    last=None

    # significa che ho messaggi in memoria
    if len(latests)>0:

        # prendo l'ultimo messaggio il più recente
        last=latests[-1]

        # verifico se non ho già risposto al messaggio
        file_ultimo= open("./lastanswered.txt","r")
        righe=file_ultimo.readlines()
        to_answer=False

        if len(righe)>0:
            if str(last.message.message_id)!=righe[0].strip("\n"):
                file_ultimo.close()
                file_ultimo= open("./lastanswered.txt","w")
                file_ultimo.write(f"{last.message.message_id}\n")
                file_ultimo.close()
                to_answer=True
        else:
            file_ultimo= open("./lastanswered.txt","w")
            file_ultimo.write(f"{last.message.message_id}\n")
            file_ultimo.close()
            to_answer=True

        # non ho ancora risposto al messaggio, procedo
        if to_answer:
            if last is not None:
                print("Devo rispondere al messaggio")

                # verifico che il contenuto sia di tipo "voice"
                if hasattr(last.message,"voice"):

                    # recupero il file dai sever di Telegram
                    file_url=chatbot.getFile(last.message.voice.file_id).file_path
                    richiesta = requests.get(file_url)

                    
                    # lo salvo il locale in formato "oga"
                    with open(f"./notaaudio.oga", 'wb') as nota_ogg:
                        nota_ogg.write(richiesta.content)
                    
                    # lo converto in formato wav
                    AudioSegment.from_ogg('notaaudio.oga').export('notaaudio.wav', format='wav')

                    audio_recognizer = sr.Recognizer()

                    with sr.AudioFile("./notaaudio.wav") as nota_wav:
                        
                         
                        audio_data = audio_recognizer.record(nota_wav)
                        # lingua utente: nel caso si voglia modificare la lingua da impostare durante le richieste a Google
                        language_user_code=last.effective_user.language_code

                        # prendo la conversione in testo da Google
                        testo_ottenuto = audio_recognizer.recognize_google(audio_data,language="it-IT")

                        # Invio una conferma all'utente con un messaggio
                        chatbot.sendMessage(chat_id=last.message.chat_id,text=f"Dovresti avermi detto qualcosa come {testo_ottenuto}")
                if hasattr(last.message,"text"):
                    message=last.message.text
                    if "help" in message or "start" in message:
                        chatbot.sendMessage(chat_id=last.message.chat_id,text=f"Ciao! Sono un chatbot di Lorenzo Neri in grado di convertire ciò che mi dici in una nota audio in testo.\nPosso tornarti comodo se non hai voglia di ascoltare gli audio dei tuoi amici, puoi inoltrarmeli ;)\n\nPer usare la mia magia, ti è sufficiente mandarmi un messaggio vocale!")
