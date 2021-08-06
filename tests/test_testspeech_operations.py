from src.speech_operations import convertWAV2Text

def test_convertWAV2Text_FileNotExists():
    try:
        convertWAV2Text("NotExistsingfile.txt")
    except FileNotFoundError as FileDoesNotExists:
        print(FileDoesNotExists)

def test_convertWAV2Text_NoneFile():
    try:
        convertWAV2Text(None)
    except FileNotFoundError as FileDoesNotExists:
        print(FileDoesNotExists)

def test_convertWAV2Text_ExpectedResult():
    expected_text=convertWAV2Text("./tests/notaaudioWAV.wav")
    assert expected_text == "test nota audio"


    