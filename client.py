import requests

def get_weathers(url):
    try:
        response = requests.get(f"{url}/weather")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return f"Error fetching: {e}"

def get_weather_by_id(url, id):
    try:
        response = requests.get(f"{url}/weather/{id}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return f"Error fetching: {e}"

def get_weather_by_name(url, name):
    try:
        response = requests.get(f"{url}/weatherbyName?name={name}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return f"Error fetching: {e}"
print("Enter your option:\n")
choice = input("1: GET WEATHER \n2: GET WEATHER BY ID \n3: GET WEATHER BY NAME \n")

if choice == "1":
    print(get_weathers("http://127.0.0.1:5000"))
elif choice == "2":
    id = input("Enter your ID: ")
    print(get_weather_by_id("http://127.0.0.1:5000",id))
else:
    name = input("Enter the name of the city: ")
    print(get_weather_by_name("http://127.0.0.1:5000",name))
