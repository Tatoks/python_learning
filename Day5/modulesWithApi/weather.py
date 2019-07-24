import requests

def current_weather():
    url = "https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=f2e9b3d28adf99c7d56b98d9044e6173"
    r = requests.get(url)
    print(r)
    weather_json = r.json()
    print(weather_json)

    min = weather_json['main']['temp_min']
    max = weather_json['main']['temp_max']

    print("The circus' forecast is", min , "as the low and", max, "as the high")