import requests
import json

class players:
    def __init__(player,name,level,rank): # Create a player object
        player.name = name 
        player.level = level
        player.rank = rank

    def __str__(player):
        return f'name: {player.name}, level: {player.level}, rank: {player.rank}'

player_data = [] # List to append player data objects to later
print("Number of players") # Ask for the number of players
num = input()
i = 0
while i < int(num): # Loop for each entered player
    print("Enter the name#tag of the player") # Ask for player id
    player_name = input()
    formatted_player_name = player_name.replace("#","/") # Replace # in the entered name with / for the link processing
    response_API = requests.get(f"https://api.henrikdev.xyz/valorant/v1/account/{formatted_player_name}") # Get the API request 
    if response_API.status_code == 200:
        data = response_API.text # Convert response to text
        parse_json = json.loads(data) # Parse the JSON response
        response_API_mmr = requests.get(f"https://api.henrikdev.xyz/valorant/v1/mmr/eu/{formatted_player_name}") # Get MMR data
        mmrdata = response_API_mmr.text # Convert MMR response to text
        mmr_parse_json =json.loads(mmrdata) # Parse the MMR JSON response
        player = players(parse_json["data"]["name"], parse_json["data"]["account_level"], mmr_parse_json["data"]["currenttierpatched"]) # Create a player object
        player_data.append(player) # Append player object to the list
        i += 1  
    else:
        print(response_API.status_code) # Print the API status code if it's not 200
        i += 1

for player in player_data:
    print(player) # Print each player's details
