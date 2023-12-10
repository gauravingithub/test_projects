import requests
import smtplib

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "open_weather_map_api_key"
my_email = "gmail_account"
password = "gmail_app_password"

weather_params = {
    "lon": 78.0333,
    "lat": 30.3167,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

def check_data(id: int)->bool:
    id//=100
    if id != 8:
        return False
    return True

res = requests.get(endpoint,params=weather_params)
res.raise_for_status()
data = res.json()
data_id = data['hourly'][0]['weather'][0]['id']

if (check_data(data_id)):
    data_main = data['hourly'][0]['weather'][0]['main']
    data_desc = data['hourly'][0]['weather'][0]['description']
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:{data_main} Alert\n\nThere may be a {data_desc} in the next hour")