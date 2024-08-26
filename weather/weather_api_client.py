from datetime import datetime
import locale
import pyttsx3 as pyt


# weather info (max and min degree, current degree, feels degree, description)
# say to good bye
def get_infos():
    engine = init_text_to_speech_engine()
    get_date_and_time_info(engine)


def init_text_to_speech_engine():
    engine = pyt.init('nsss')
    engine.setProperty('rate', 150)
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.yelda.premium')
    return engine


def get_date_and_time_info(engine):
    locale.setlocale(locale.LC_TIME, 'tr_TR.UTF-8')
    now = datetime.now()
    part_of_day = get_part_of_day(now.hour)
    engine.say(part_of_day)
    formatted_date = now.strftime('Bugün %d %B %Y %A')
    engine.say(formatted_date)
    formatted_time = now.strftime('Saat %H %M')
    engine.say(formatted_time)
    engine.runAndWait()


def get_part_of_day(hour):
    if 6 <= hour <= 12:
        return 'Günaydın'
    elif 12 < hour <= 18:
        return 'İyi Günler'
    elif 18 < hour <= 21:
        return 'İyi Akşamlar'
    else:
        return 'İyi Geceler'
