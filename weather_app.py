import requests
import json
import os


def weather_app(city_name,api_key):
    """ get the weather from weather app and return the json into python dictionary"""

    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        "q" : city_name ,
        "appid" :api_key,
        "&units": "metric"
    }
        
    try:

        r = requests.get(base_url,params=params)  
        r.raise_for_status()
        weather_data = r.json()
        return weather_data

    except requests.exceptions.HTTPError as e:
        if r.status_code == 401:
            print("APi key is invalid")
        elif r.status_code == 404:
            print("query not occur")
        else:
            print(f"unexpected error:{e}")   
    except requests.exceptions.ConnectionError as r:
        print(f"connection not established :{r}")
    except requests.exceptions.RequestException as e:
        print(f"other errror occured:{e}")                 



def display_weather(data):
    if not data:
        print("there is not data")

    try:
        city_name = data["name"]
        country = data["sys"]["country"]
        main_weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n--- Weather in {city_name}, {country} ---")
        print(f"Condition: {main_weather} ({description})")
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print("------------------------------")
        
    except KeyError as e:
        print(f"Error: Could not parse weather data. Missing key: {e}")
        print("The API response structure may have changed.")
    except IndexError:
        print("Error: Could not parse weather 'description'.")

def main():
    api_key = '2d015ebe5142b551f5384dac8e14397c'

    if not api_key:
        print("invalid key!! please try again")

    city_name = input("enter city name:- ").strip()

    if not city_name:
        print("enter valid city")
    else:
        weather_data = weather_app(city_name,api_key)

        if weather_data:
            display_weather(weather_data) 


main()               




    


    





  