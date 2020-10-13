import os
import subprocess
from uuid import uuid4
try:
    from gtts import gTTS
except:
    pass

from ttsdemo.settings import MEDIA_ROOT, MEDIA_URL, TTS_ENGINE


def tts(text :str) -> str:
    try:
        engine = _ENGINES[TTS_ENGINE]
    except KeyError:
        raise ValueError('No such engine: {}'.format(TTS_ENGINE))

    name = uuid4().hex
    path = os.path.join(MEDIA_ROOT, name)    
    engine(text, path)
    return MEDIA_URL + name


def _system_tts(text, path, params):
    txt_path = path + '.txt'
    params[params.index(None)] = txt_path
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)
    proc = subprocess.Popen(params, stdin=subprocess.PIPE)
    proc.wait()


def _rhvoice(text, path):
    params = ['RHVoice-test', '-i', None, '-o', path, '-p', 'aleksandr+alan']
    _system_tts(text, path, params)


def _festival(text, path):
    params = ['text2wave', None, '-o', path]
    _system_tts(text, path, params)


def _google(text, path):
    result = gTTS(text)
    result.save(path)


_ENGINES = {
    'Google': _google,
    'RHVoice': _rhvoice,
    'Festival': _festival
}