import locale
from datetime import datetime


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
