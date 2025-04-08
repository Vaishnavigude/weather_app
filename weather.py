import requests

city = input("Enter city: ")
api_key = "YOUR_API_KEY"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url).json()
temp = response["main"]["temp"]
desc = response["weather"][0]["description"]

print(f"Temperature in {city}: {temp}°C, {desc}")
