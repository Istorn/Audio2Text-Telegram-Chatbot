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
from config import chatbot_token
from file_operations import messageAlreadyAnswered, saveOGAFile, convertAudioMsg2WAV
from speech_operations import convertWAV2Text


if __name__ == "__main__":
    # istanzio il chatbot
    chatbot=telegram.Bot(token=chatbot_token)

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

            if last is not None:
                # il messaggio non è None
                # prendo il message_id 
                message_id=str(last.message.message_id)
                
                # non ho ancora risposto al messaggio, procedo
                if messageAlreadyAnswered(message_id):
                
                    print("Devo rispondere al messaggio")

                    # verifico che il contenuto sia di tipo "voice"
                    if hasattr(last.message,"voice"):

                        # recupero il file dai sever di Telegram
                        file_url=chatbot.getFile(last.message.voice.file_id).file_path
                        richiesta = requests.get(file_url)

                        # uso il file_id come file name per la nota audio
                        ogaFileName=f"NotaAudio{last.message.voice.file_id}.oga"
                        
                        # prendo i byte come contenuto della nota audio stessa
                        ogaFileContent=richiesta.content

                        # lo salvo in locale in formato "oga"
                        saveOGAFile(oga_file_content=ogaFileContent,oga_file_name=ogaFileName)
                        
                        # lo converto in formato wav
                        wav_file_name=convertAudioMsg2WAV(ogaFileName)

                        # prendo la lingua dell'utente
                        # lingua utente: nel caso si voglia modificare la lingua da impostare durante le richieste a Google
                        language_user_code=last.effective_user.language_code

                        # eseguo il processo di conversione in testo
                        text_from_audio=convertWAV2Text(wav_file_name=wav_file_name,user_language=language_user_code)

                        
                        # Invio una conferma all'utente con un messaggio
                        chatbot.sendMessage(chat_id=last.message.chat_id,text=f"Dovresti avermi detto qualcosa come {text_from_audio}")

                    if hasattr(last.message,"text"):
                        message=last.message.text
                        if message is not None:
                            if "help" in message or "start" in message:
                                chatbot.sendMessage(chat_id=last.message.chat_id,text=f"Ciao! Sono un chatbot di Lorenzo Neri in grado di convertire ciò che mi dici in una nota audio in testo.\nPosso tornarti comodo se non hai voglia di ascoltare gli audio dei tuoi amici, puoi inoltrarmeli ;)\n\nPer usare la mia magia, ti è sufficiente mandarmi un messaggio vocale!")
