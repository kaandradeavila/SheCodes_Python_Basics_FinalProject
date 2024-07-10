import requests
from rich import print
from datetime import datetime


def ask_city():
  city = input("Enter a city: ")
  if city:
    return city
  else:
    "Please try again."
    ask_city()


def greet_user():
  print("[bold purple]Welcome to my weather app![/bold purple]")


def handle_api_request():
  api_key = "424369doa037d0347bft3cfcc8cef956"
  city = ask_city()

  api_url_current_weather = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}&units=metric"
  api_url_forecast = f"https://api.shecodes.io/weather/v1/forecast?query={city}&key={api_key}&units=metric"

  response_current_weather = requests.get(api_url_current_weather)
  response_forecast = requests.get(api_url_forecast)

  display_current_weather(response_current_weather.json())
  display_forecast_weather(response_forecast.json())


def display_current_weather(response):
  current_temperature = round(response["temperature"]["current"])
  print(f"[bold blue]Today[/bold blue]: {current_temperature}ºC")


def display_forecast_weather(response):
  print("\n[bold green]Forecast[bold green]:")

  for day in response["daily"]:
    timestamp = day["time"]
    date = datetime.fromtimestamp(timestamp)
    formatted_day = date.strftime("%A")
    temperature = round(day["temperature"]["day"])

    if date.date() != datetime.now().date():
      print(f"[bold blue]{formatted_day}[/bold blue]: {temperature}ºC")


greet_user()
handle_api_request()

print(
    "\n[bold yellow]This app was built by Kyrenia Ailen Andrade Avila[/bold yellow]"
)
