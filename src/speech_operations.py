import speech_recognition as speechrec

# funzione che traduce il file wav in testo puro usando le API di Google Cloud Speech
def convertWAV2Text(wav_file_name:str,user_language:str="it-IT"):
    audio_recognizer = speechrec.Recognizer()

    with speechrec.AudioFile(f"./{wav_file_name}") as nota_wav:
        
        # prendo il contenuto della nota audio
        audio_data = audio_recognizer.record(nota_wav)
        
        # prendo la conversione in testo da Google
        testo_ottenuto = audio_recognizer.recognize_google(audio_data,language=user_language)

        # ritorno il testo ottenuto

        return testo_ottenuto