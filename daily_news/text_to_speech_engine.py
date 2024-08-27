import platform

import pyttsx3 as pyt


def init_text_to_speech_engine():
    engine = pyt.init(get_engine_driver_by_os())
    engine.setProperty('rate', 150)
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.yelda.premium')
    return engine


def get_engine_driver_by_os():
    sys_platform = platform.system()
    if sys_platform == 'Linux':
        return 'espeak'
    elif sys_platform == 'Darwin':
        return 'nsss'
    elif sys_platform == 'Windows':
        return 'sapi5'
