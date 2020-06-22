import configparser
import requests
from datetime import datetime

# Busca do api key no arquivo config.ini
def get_api_key():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["openweathermap"]["api"]

# Request da 5 day forecast de Ribeirão Preto usando o city_ID
def get_forecast_list(city_id, api_key):
    url = "https://api.openweathermap.org/data/2.5/forecast?id={}&appid={}".format(city_id, api_key)
    r = requests.get(url)
    return r.json()["list"]

# Filtro do forecast_list e display do resultado final
def display_message(forecast_list):
    rainy_days_list = []
    for forecast in forecast_list:

        # Definição do dia da semana a partir da unix epoch
        week_day = datetime.fromtimestamp(forecast["dt"]).strftime("%A")

        # Check da humidade e de se o dia da semana ainda não está na lista
        if forecast["main"]["humidity"] > 70 and week_day not in rainy_days_list:
            rainy_days_list.append(week_day)

    print("You should take an umbrella in these days:", ", ".join(rainy_days_list[:-1]), "and", rainy_days_list[-1])

def main():
    api_key = get_api_key()
    ribeiraopreto_city_id = 3451328
    forecast_list = get_forecast_list(ribeiraopreto_city_id, api_key)
    display_message(forecast_list)

if __name__ == "__main__":
    main()
