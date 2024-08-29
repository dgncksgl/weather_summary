import platform

import pyttsx3 as pyt

DRIVER = {
    'Linux': 'espeak',
    'Darwin': 'nsss',
    'Windows': 'sapi5'
}


def init_text_to_speech_engine():
    engine = pyt.init(get_engine_driver_by_os())
    engine.setProperty('rate', 150)
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.yelda.premium')
    return engine


def get_engine_driver_by_os() -> str:
    sys_platform = platform.system()
    return DRIVER[sys_platform]
