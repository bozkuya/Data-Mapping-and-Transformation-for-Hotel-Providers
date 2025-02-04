import json
from classes import Category, Chain, Hotel

def parse_data(json_data):
    # Initialize dictionaries to store categories, chains, and a list for hotels
    categories = {}
    chains = {}
    hotels = []

    # Iterate through each item in the JSON data
    for key, value in json_data.items():
        # Extract category, chain, and location data from the JSON item
        category_data = value.get("category")
        chain_data = value.get("chain")
        location_data = value.get("location")
        
        # If any of the necessary data is missing, skip this item
        if not category_data or not chain_data or not location_data:
            continue
        
        # Get the category object or create a new one if it doesn't exist
        category = categories.get(category_data["id"], Category(category_data["id"], category_data["name"]))
        categories[category_data["id"]] = category
        
        # Get the chain object or create a new one if it doesn't exist
        chain = chains.get(chain_data["id"], Chain(chain_data["id"], chain_data["name"]))
        chains[chain_data["id"]] = chain
        
        # Create a hotel object and add it to the hotels list
        hotel = Hotel(value["property_id"], value["name"], category, chain, location_data["coordinates"])
        hotels.append(hotel)

    # Return the dictionaries of categories, chains, and the list of hotels
    return categories, chains, hotels