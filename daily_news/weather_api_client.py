import requests
from pyttsx3 import engine

api_key = '822ccea99e830f652ac3eec191bf60ef'
city = 'Ankara'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=tr&units=metric'


def get_weather_infos(speech_engine: engine.Engine):
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        speech_engine.say(f"{city} ili için hava bilgileri şu şekildedir")
        speech_engine.say(f"mevcut sıcaklık {data['main']['temp']}°C")
        speech_engine.say(f"hissedilen sıcaklık {data['main']['feels_like']}°C")
        speech_engine.say(f"maksimum sıcaklık {data['main']['temp_max']}°C")
        speech_engine.say(f"minimum sıcaklık {data['main']['temp_min']}°C")
        speech_engine.say(f"Hava {data['weather'][0]['description']}")
    else:
        print(f"Error {data['cod']}: {data['message']}")

    speech_engine.say("Sağlıcakla kalın")
    speech_engine.runAndWait()
