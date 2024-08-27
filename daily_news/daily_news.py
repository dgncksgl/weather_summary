from .date_time_info import get_date_and_time_info
from .text_to_speech_engine import init_text_to_speech_engine


def get_infos():
    engine = init_text_to_speech_engine()
    get_date_and_time_info(engine)
