import random

# Define some basic components and rules for ship creation

# Define hull types and their associated costs
hull_types = {
    "Light Freighter": {"tonnage": 200, "cost": 100},
    "Mercenary Cruiser": {"tonnage": 500, "cost": 250},
    "Battleship": {"tonnage": 1000, "cost": 500},
}

# Define power plants
power_plants = {
    "Fusion Reactor": {"cost": 50, "power_output": 100},
    "Antimatter Reactor": {"cost": 150, "power_output": 200},
}

# Define weapons and their costs
weapons = {
    "Laser": {"cost": 20, "damage": 50},
    "Missile Launcher": {"cost": 40, "damage": 100},
    "Plasma Gun": {"cost": 60, "damage": 200},
}

# Define ship system components
ship_systems = {
    "Life Support": {"cost": 10},
    "Artificial Gravity": {"cost": 20},
    "Jump Drive": {"cost": 150},
}

def create_ship():
    print("Welcome to Traveller RPG Ship Designer!")
    
    # Choose hull type
    print("Choose your hull type:")
    for index, hull in enumerate(hull_types.keys(), 1):
        print(f"{index}. {hull}")
    
    hull_choice = int(input("Enter the number corresponding to your choice: ")) - 1
    hull_name = list(hull_types.keys())[hull_choice]
    hull = hull_types[hull_name]
    
    # Choose power plant
    print("Choose your power plant:")
    for index, power in enumerate(power_plants.keys(), 1):
        print(f"{index}. {power}")
    
    power_choice = int(input("Enter the number corresponding to your choice: ")) - 1
    power_name = list(power_plants.keys())[power_choice]
    power_plant = power_plants[power_name]
    
    # Choose weapons
    print("Choose your weapons (separate choices by commas, e.g. 1,3):")
    for index, weapon in enumerate(weapons.keys(), 1):
        print(f"{index}. {weapon}")
    
    weapon_choices = input("Enter weapon numbers: ")
    weapon_choices = [int(choice) - 1 for choice in weapon_choices.split(",")]
    selected_weapons = [list(weapons.keys())[choice] for choice in weapon_choices]
    total_weapon_cost = sum(weapons[weapon]["cost"] for weapon in selected_weapons)
    
    # Choose ship systems
    print("Choose your ship systems (separate choices by commas, e.g. 1,2):")
    for index, system in enumerate(ship_systems.keys(), 1):
        print(f"{index}. {system}")
    
    system_choices = input("Enter system numbers: ")
    system_choices = [int(choice) - 1 for choice in system_choices.split(",")]
    selected_systems = [list(ship_systems.keys())[choice] for choice in system_choices]
    total_system_cost = sum(ship_systems[system]["cost"] for system in selected_systems)
    
    # Calculate total cost
    total_cost = hull["cost"] + power_plant["cost"] + total_weapon_cost + total_system_cost
    total_tonnage = hull["tonnage"]  # Start with hull tonnage (for simplicity)

    print("\n--- Ship Design Summary ---")
    print(f"Hull: {hull_name} (Tonnage: {hull['tonnage']}, Cost: {hull['cost']})")
    print(f"Power Plant: {power_name} (Cost: {power_plant['cost']}, Power Output: {power_plant['power_output']})")
    print("Weapons: " + ", ".join(selected_weapons) + f" (Total Weapon Cost: {total_weapon_cost})")
    print("Systems: " + ", ".join(selected_systems) + f" (Total System Cost: {total_system_cost})")
    print(f"Total Cost: {total_cost}")
    print(f"Total Tonnage: {total_tonnage} tons")

# Call the create_ship function to run the program
if __name__ == "__main__":
    create_ship()