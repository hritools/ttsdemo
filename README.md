# TTS Demo
Simple Text-To-Speech web app.

## Configure
### 1. Instal requirements
`pip install -Ur requirements.txt`

### 2. Choose TTS Engine
Change `TTS_ENGINE` in `ttsdemo/settings.py`.  
Supported engines:
* `Google`  
  `pip install -U "gtts==2.0.3"`
* `RHVoice`  
  [Read wiki](https://cordelianew.university.innopolis.ru/wiki/doku.php?id=rhvoice) for installing instructions.

* `Festival`  
  [Read wiki](https://cordelianew.university.innopolis.ru/wiki/doku.php?id=festival_tts) for installing instructions.

### 3. File storage directory (optional)
In this directory generated audio and text files are stored.  
Change `MEDIA_ROOT` in `ttsdemo/settings.py`.  
Default is `/path/to/ttsdemo/media`. 

### 4. Reverse Proxy (optional)
To work with reverse prxoy set `BASE_URL` environment variable

## Run
1. Run server `python manage.py runserver`
2. In browser open [http://localhost:8000](http://localhost:8000)

## Cleaner
Removes generated files.  
Run once: `python cleaner.py 1`  
Run forever: `python cleaner.py`
