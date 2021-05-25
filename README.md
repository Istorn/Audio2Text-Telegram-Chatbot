# Audio2Text-Telegram-Chatbot

![Immagine del chatbot](https://lorenzoneri.com/wp-content/uploads/2021/05/anteprimachatbot.jpg)

Questo chatbot è in grado di convertire le note vocali dei tuoi utenti **in messaggi di testo** *attraverso l'uso delle Google Cloud Speech API*.

### Architettura del chatbot stesso

Il chatbot si basa sulla seguente archiettura:

![Immagine dell'architettura](https://lorenzoneri.com/wp-content/uploads/2021/05/algoritmo-1024x650.jpg)

Per maggior informazioni a riguardo, è possibile consultare l'articolo presente sul mio blog: [Scopri di più](https://lorenzoneri.com/chatbot-telegram-conversione-note-vocali-in-messaggi/)

### Installazione, dipendenze ed uso

È necessario Python3: https://www.python.org/downloads/

Una volta installato, eseguire i seguenti step per installare i pacchetti Python necessari.
**È necessario installare anche [pip](https://pypi.org/project/pip/)**

1. Aprire una finistra terminale
2. Eseguire il seguente comando *se non si ha installato **pip***:
```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```
3. Una volta scaricato, **installare pip oppure procedere direttamente allo step 4**:
```python3 get-pip.py```
4. Per installare tutti i pacchetti, localizzarsi nella cartella del chatbot, *ad esempio*:
```cd ~/Audio2Text-Telegram-Chatbot```

    Dopodichè lanciare il seguente comando:

    ```pip install -r requirements.txt```

    Termianta l'installazione dei pacchetti necessari, **è possibile usare il chatbot**

### Come avere un Chatbot Telegram

Il chatbot in sé *non funziona se non si ha a disposizione un chatbot registrato su Telegram*.

Per fare ciò, seguire i seguenti step:

1. **Come creare un chatbot Telegram**: [guida alla creazione](https://lorenzoneri.com/come-creare-un-chatbot-telegram/)
2. **Imparare i meccanismi basilari di un chatbot Telegram**: [guida al funzionamento](https://lorenzoneri.com/il-tuo-primo-chatbot-telegram/)

### Come usarlo

Una volta terminato il processo di installazione e *inserimento del token nel file `main.py`*, **aprire una finestra terminale e lanciare il seguente comando**:

```python3 main.py```

Al ricevimento di nuovi messaggi, il chatbot si premurerà *di interrogare le API di Google e infine* **restituire un messaggio di testo vero e proprio**:

![Immagine chat Telegram](https://lorenzoneri.com/wp-content/uploads/2021/05/Screenshot_20210525_113255.jpg)


### Licenza

Questo codice è regolato dalla licenza Creative Commons CC BY-NC 4.0: https://creativecommons.org/licenses/by-nc/4.0/


**Cosa puoi farci:**


- Condividi: copia e ridistribuisci il materiale in qualsiasi mezzo o formato;
- Adatta: remixa, trasforma e costruisci sul materiale;

A che condizioni: citandomi!

**Cosa *NON* puoi farci**:

Usare la codebase a scopi commerciali

