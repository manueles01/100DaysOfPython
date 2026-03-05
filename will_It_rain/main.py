import requests 
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "8565fe4f5e8f0826dd7af4f313a9735c"
MY_LAT = "41.026241"
MY_LON = "-73.628548"


weather_params ={
    "lat": MY_LAT,
    "lon":MY_LON,
    "appid":api_key,
}


response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
print(response.json())
