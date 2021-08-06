import pytest 

@pytest.fixture
def chatbot_token():
    token_file=open("./personal_token.txt","r")
    token=token_file.read()
    token_file.close()
    return token

@pytest.fixture
def notaAudioOGG():
    ogg_file=open("./tests/notaaudioOGG.oga","rb")
    ogg_content=ogg_file.read()
    ogg_file.close()
    return ogg_content

@pytest.fixture
def notaAudioWAV():
    wav_file=open("./tests/notaaudioWAV.wav","rb")
    wav_content=wav_file.read()
    wav_file.close()
    return wav_content