import requests

api_key = '822ccea99e830f652ac3eec191bf60ef'
city = 'Ankara'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=tr&units=metric'


def get_weather_infos(engine):
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        engine.say(f"{city} ili için hava bilgileri şu şekildedir")
        engine.say(f"mevcut sıcaklık {data['main']['temp']}°C")
        engine.say(f"hissedilen sıcaklık {data['main']['feels_like']}°C")
        engine.say(f"maksimum sıcaklık {data['main']['temp_max']}°C")
        engine.say(f"minimum sıcaklık {data['main']['temp_min']}°C")
        engine.say(f"Hava {data['weather'][0]['description']}")
    else:
        print(f"Error {data['cod']}: {data['message']}")

    engine.say("Sağlıcakla kalın")
    engine.runAndWait()
