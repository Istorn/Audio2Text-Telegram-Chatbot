from src.file_operations import convertAudioMsg2WAV,saveOGAFile, messageAlreadyAnswered
import pathlib
import pytest
from tests.fixtures import notaAudioOGG,notaAudioWAV

@pytest.mark.skip
def test_convertAudioMsg2Wav_Expected():
    
    wav_file_name=convertAudioMsg2WAV("./tests/notaaudioOGG.oga")

    assert pathlib.Path("./tests/notaaudioWAV.wav").exists() == True

    
    assert wav_file_name.split(".")[0] == "notaaudioOGG.oga".split(".")[0]
    
    assert wav_file_name.split(".")[1] == "wav"


def test_convertAudioMsg2Wav_NotExists():
    try:
        convertAudioMsg2WAV("FileNotExists.oga")
    except FileNotFoundError as filenotfound:
        assert filenotfound is not None

@pytest.mark.parametrize('oggcontent',[notaAudioOGG])
def test_saveOGAFile_Expected(oggcontent):
    
    fileName=saveOGAFile(oggcontent.read(),"testNotaAudio.oga")

    assert fileName == "testNotaAudio.oga"


