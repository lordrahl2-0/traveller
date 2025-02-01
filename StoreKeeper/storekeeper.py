import random
import os

def load_items(file_name):
    """Loads item details from an external text file."""
    if not os.path.exists(file_name):
        print(f"Error: {file_name} does not exist.")
        return []
    
    items = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            parts = line.strip().split('|')
            if len(parts) == 7:  # Now we expect 7 parts per line
                item_name, item_type, description, traits, law_level, tech_level, base_price = parts
                items.append({
                    'name': item_name,
                    'type': item_type,
                    'description': description,
                    'traits': traits,
                    'law_level': int(law_level),
                    'tech_level': int(tech_level),
                    'base_price': int(base_price)  # Store the base price as an integer
                })
    
    return items

def generate_price(base_price, fluctuation_percentage=0.2):
    """Generate a random price around a nominal value with a fluctuation range."""
    fluctuation = base_price * random.uniform(-fluctuation_percentage, fluctuation_percentage)
    return round(base_price + fluctuation, 2)

def generate_stock(min_stock=1, max_stock=10):
    """Generate a random stock level."""
    return random.randint(min_stock, max_stock)

def get_store_size_multiplier(store_size):
    """Returns the multiplier for number of items and stock based on the store size."""
    store_sizes = {
        'tiny': (2, 2),       # Few items, low stock
        'small': (3, 4),      # Small number of items, medium stock
        'medium': (5, 6),     # Moderate number of items, decent stock
        'large': (8, 10),     # Large number of items, higher stock
        'superstore': (12, 15),# Very large number of items, very high stock
        'megastore': (20, 25) # Huge number of items, massive stock
    }
    
    return store_sizes.get(store_size.lower(), (5, 6))  # Default to medium if invalid size

def filter_items_by_tech_level(items, selected_tech_level, num_items_required):
    """Filters and weights items based on proximity to selected tech level, expanding search if needed."""
    weighted_items = []
    tech_level_range = 0
    items_found = 0
    
    while items_found < num_items_required and tech_level_range <= 3:
        # Look at tech levels from (selected_tech_level - tech_level_range) to (selected_tech_level + tech_level_range)
        for item in items:
            if abs(item['tech_level'] - selected_tech_level) <= tech_level_range:
                weighted_items.append(item)
                items_found += 1
            if items_found >= num_items_required:
                break
        
        # If still not enough items, increase the tech_level_range to expand the search.
        tech_level_range += 1

    # Ensure we return only the required number of items, even if we found more than needed
    return weighted_items[:num_items_required]

def generate_inventory(store_type, max_law_level, max_tech_level, store_size):
    """Generates a random inventory for a given store type, filtered by law level and tech level."""
    # Define store type to file mapping
    store_files = {
        'general': 'StoreKeeper/Stores/generalgoods.txt',
        'weapons': 'StoreKeeper/Stores/weapons.txt',
        'potions': 'items_potions.txt'
    }
    
    # Load appropriate items based on store type
    file_name = store_files.get(store_type.lower())
    
    if not file_name:
        print("Invalid store type.")
        return []
    
    items = load_items(file_name)
    
    if not items:
        print(f"No items found for {store_type} store.")
        return []
    
    # Filter items based on law level
    filtered_items = [
        item for item in items if item['law_level'] >= max_law_level
    ]
    
    # Get store size multiplier for the number of items and stock levels
    num_items_multiplier, stock_multiplier = get_store_size_multiplier(store_size)
    
    # Determine the number of items required based on store size multiplier
    num_items_required = num_items_multiplier * 3  # Ensure enough items for larger stores
    
    # Filter and weight items based on tech level, expanding the search if necessary
    weighted_items = filter_items_by_tech_level(filtered_items, max_tech_level, num_items_required)
    
    # If no items match the criteria, notify the user and return an empty inventory
    if not weighted_items:
        print("No items meet the criteria based on the law level and tech level.")
        return []
    
    # Remove duplicates if any by converting the list to a set and back to a list
    weighted_items = list({item['name']: item for item in weighted_items}.values())
    
    # Adjust number of items to select based on the filtered list
    num_items_to_stock = min(len(weighted_items), num_items_required)
    
    # Randomly select a subset of items from the filtered list to stock
    selected_items = random.sample(weighted_items, num_items_to_stock)
    
    # Generate random inventory for selected items
    inventory = []
    for item in selected_items:
        price = generate_price(item['base_price'])  # Use the base price from the item
        stock = generate_stock(1, 10 * stock_multiplier)  # Stock will vary based on store size multiplier
        inventory.append({
            'name': item['name'],
            'type': item['type'],
            'description': item['description'],
            'traits': item['traits'],
            'price': price,
            'stock': stock,
            'law_level': item['law_level'],
            'tech_level': item['tech_level']
        })
    
    return inventory



def display_inventory(inventory):
    """Displays the generated inventory."""
    if not inventory:
        print("No inventory to display.")
        return
    
    for item in inventory:
        print(f"Item: {item['name']}")
        print(f"Type: {item['type']}")
        print(f"Description: {item['description']}")
        print(f"Traits: {item['traits']}")
        print(f"Price: {item['price']} gold")
        print(f"Stock: {item['stock']}")
        print(f"Law Level: {item['law_level']}")
        print(f"Tech Level: {item['tech_level']}")
        print("-" * 40)

def main():
    print("Welcome to the RPG Store Inventory Generator!")
    
    # Prompt user for law level
    try:
        max_law_level = int(input("Enter your law level (0-9): ").strip())
    except ValueError:
        print("Invalid input for law level.")
        return
    
    if not (0 <= max_law_level <= 9):
        print("Law level must be between 0 and 9.")
        return
    
    # Prompt user for tech level
    try:
        max_tech_level = int(input("Enter your tech level (0-15): ").strip())
    except ValueError:
        print("Invalid input for tech level.")
        return
    
    if not (0 <= max_tech_level <= 15):
        print("Tech level must be between 0 and 15.")
        return
    
    # Prompt user for store size
    store_size = input("Enter the store size (tiny, small, medium, large, superstore, megastore): ").strip().lower()
    
    # Choose store type
    store_type = input("Choose store type (general, weapons, potions): ").strip().lower()
    
    # Generate inventory for selected store type and size
    inventory = generate_inventory(store_type, max_law_level, max_tech_level, store_size)
    
    # Display generated inventory
    display_inventory(inventory)

if __name__ == "__main__":
    main()
