import requests
from twilio.rest import Client

url = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "NA"

account_sid = "NA"
auth_token = "NA"

weather_params = {
    "lat": 34.149551,
    "lon": -118.141449,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url, params=weather_params)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data['list'][:12]

will_rain = False

for hour_data in weather_slice:
    id_code = hour_data['weather'][0]['id']
    if int(id_code) < 700:
        will_rain = True

if will_rain:
    rain = "It's gonna rain bitch"
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=rain,
        from_='+18446360575',
        to='+18054230365'
    )
    print(message.status)
