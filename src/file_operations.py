from pydub import AudioSegment

# funzione che verifica se il chatbot ha già risposto al message con il 'message_id' indicato
def messageAlreadyAnswered(message_id:str):

        file_ultimo= open("lastanswered.txt","r")
        righe=file_ultimo.readlines()
        

        if len(righe)>0:
            if message_id!=righe[0].strip("\n"):
                file_ultimo.close()
                file_ultimo= open("lastanswered.txt","w")
                file_ultimo.write(f"{message_id}\n")
                file_ultimo.close()
                return True
        else:
            file_ultimo= open("lastanswered.txt","w")
            file_ultimo.write(f"{message_id}\n")
            file_ultimo.close()
            return True

# funzione usata per salvare la nota vocale dell'utente

def saveOGAFile(oga_file_content:bytes, oga_file_name:str):
    with open(f"./{oga_file_name}", 'wb') as nota_ogg:
        nota_ogg.write(oga_file_content)

# funzione usata per convertire la nota vocale in formato wav
def convertAudioMsg2WAV(oga_file_name:str):
    filename_without_extension=oga_file_name.split(".")[0]
    wav_file_name=f'./{filename_without_extension}.wav'
    AudioSegment.from_ogg(oga_file_name).export(wav_file_name, format='wav')
    return wav_file_name