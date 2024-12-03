import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon_name):
    url = f"{base_url}/pokemon/{pokemon_name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon_name = "charizard"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"NAME: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"BASE EXP: {pokemon_info["base_experience"]}")
    print(f"HEIGHT: {pokemon_info["height"]}")
    print(f"WEIGHT: {pokemon_info["weight"]}")


