# Demander la météo à un service sur internet
# et la renvoyer
# s'inscrire gratuitement sur openweathermap.org
# aller dans l'onglet de son compte et générer une API key (devSV)

# créer un fichier .env
# API_KEY=numDeLApiKey
# ajouter .env dans le fichier .gitignore

# aller dans https://openweathermap.org/current
# pour récupérer l'API call
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# et voir les paramètres qu'on peut passer
# et le format de la réponse JSON
# dans onglet units of mesurement (à droite)
# chercher call back Celsius (&units=metric après {API key})

import requests
from dotenv import load_dotenv
import os
from pprint import pprint

# charger la clé API
load_dotenv()

def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name:\n")
    # modifier url pour choix d'une ville et non de coordonnées
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)
    # + Run du fichier renvoie l'url avec API et ville choisie (ici Rennes)

    weathert_data = requests.get(request_url).json()
    print(weathert_data)
    # {'coord': {'lon': -1.6667, 'lat': 48.1667}, 'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09n'}], 'base': 'stations', 'main': {'temp': 13.8, 'feels_like': 13.69, 'temp_min': 11.99, 'temp_max': 14.02, 'pressure': 997, 'humidity': 94}, 'visibility': 6000, 'wind': {'speed': 2.06, 'deg': 170}, 'clouds': {'all': 100}, 'dt': 1698263978, 'sys': {'type': 1, 'id': 6565, 'country': 'FR', 'sunrise': 1698216019, 'sunset': 1698253259}, 'timezone': 7200, 'id': 2983989, 'name': 'Arrondissement de Rennes', 'cod': 200}
    
    # Formater le print la réponse
    # pprint(weathert_data)
    # {'base': 'stations',
    # 'clouds': {'all': 100},
    # 'cod': 200,
    # 'coord': {'lat': 48.1667, 'lon': -1.6667},
    # 'dt': 1698263978,
    # 'id': 2983989,
    # 'main': {'feels_like': 13.69,
    #         'humidity': 94,
    # ...}
    print(f"Current weather for {weathert_data['name']}")
    print(f"The temp is {weathert_data['main']['temp']}")
    print(f"Feels like {weathert_data['main']['feels_like']}\nand {weathert_data['weather'][0]['description'].capitalize()} ")
    # Current weather for Arrondissement de Rennes
    # The temp is 13.8
    # Feels like 13.69 
    # and Light intensity drizzle


if __name__ == "__main__":
    get_current_weather()







