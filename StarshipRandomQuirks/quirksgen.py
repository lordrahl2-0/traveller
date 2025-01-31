import random

# Define the lists of options (you can add more options to each list as needed)
systems = ["computer", "power plant", "jump drive", "maneuver drive", "fuel tank", "weapon"]
systems_2 = ["ship's computer", "power plant", "jump drive", "maneuver drive", "autodoc", "weapon", "pilot controls", "nav computer", "gunnery computer", "crew toilets", "autochef"]
powered_systems = ["life support", "shields", "maneuver drive", "computer"]
drives = ["jump drive", "maneuver drive", "power plant"]
locations = ["bridge", "fresher", "cargo bay", "galley", "stateroom", "engineering", "medical"]
fluids = ["oil", "fuel", "fresh water", "sewage"]
posmodifiers = ["+1", "+2"]
negmodifiers = ["-1", "-2"]
allmodifiers = ["+1", "+2", "-1", "-2"]
d4 = ["1", "2", "3", "4"]
loot = ["drugs", "weapons", "contraband", "valuables"]
temp = ["10", "16", "21", "27", "32", "38"]

# Generate quirky or perk-like phrases for each random choice
def generate_quirk_perk():
    system_choice = random.choice(systems)
    system_2_choice = random.choice(systems_2)
    powered_system_choice = random.choice(powered_systems)
    drive_choice = random.choice(drives)
    location_choice = random.choice(locations)
    fluid_choice = random.choice(fluids)
    posmodifier_choice = random.choice(posmodifiers)
    negmodifier_choice = random.choice(negmodifiers)
    allmodifier_choice = random.choice(allmodifiers)
    loot_choice = random.choice(loot)
    d4_roll = random.choice(d4)

    # Randomly pick one quirk/perk from the list
    return random.choice(quirksandperks_list)

def get_random_choices():
    # Ask how many options the user wants
    n = int(input("How many random quirks/perks would you like to generate? "))

    if n < 1:
        print("You must pick at least 1 option.")
        return

    # Prepare the list and shuffle to avoid repeated results
    quirksandperks_list = [
        f"{random.choice(systems)} {random.choice(allmodifiers)} to repairs",
        f"{random.choice(systems)} needs repairs",
        f"{random.choice(systems_2)} needs percussive maintenance to work",
        "access to coded military channels",
        "adjustable gravity deck plating",
        f"advanced ECM: {random.choice(posmodifiers)} against missiles",
        f"advanced shields {random.choice(posmodifiers)}",
        f"advanced vehicle: {random.choice(posmodifiers)} tech levels higher than the ship",
        f"alien alloy hull: {random.choice(posmodifiers)} against lasers",
        "alien graffiti on hull",
        "alien porn in the ship's computer",
        "all doors are airtight",
        "animal droppings found in galley",
        "annoying, mild gravity fluctuations",
        "atmosphere modifiers in cargo bay",
        "autochef only makes flavorless gruel",
        f"autodoc gives {random.choice(posmodifiers)} to MED rolls",
        "awesome color scheme",
        "awesome sound system",
        "awkward control interface (-1 to bridge activities)",
        "battle scars draw unwanted attention",
        "bridge consoles rattle in flight",
        "bridge controls are in an alien language",
        "bunks are really comfortable",
        "bunks are very uncomfortable",
        "can bypass interdiction satellites",
        "can make .5 past lightspeed",
        "cargo door sticks 50% of the time",
        "cargo space can be refrigerated",
        "clean engines - difficult to track",
        "comm system is plagued with static",
        "comm system on the fritz",
        f"computer data: {random.choice(allmodifiers)} to COMP rolls",
        f"computer glitch: {random.choice(allmodifiers)} to ENG rolls",
        f"computer glitch: {random.choice(allmodifiers)} to GUNNERY rolls",
        f"computer glitch: {random.choice(allmodifiers)} to NAV rolls",
        f"computer glitch: {random.choice(allmodifiers)} to PILOT rolls",
        "computer has strange accent",
        "computer is becoming self-aware",
        "computer talks fast",
        "computer talks slow",
        "concussive backfire on takeoff",
        "constant new car smell",
        "contraband found in hidden space",
        "cooking activates fire alarm",
        "cosmetic damage to the exterior",
        "cramped crew staterooms",
        "cramped Engineering: -1 to rolls",
        "cramped passenger staterooms",
        "custom consoles (+1 to bridge rolls)",
        f"database adds {random.choice(posmodifiers)} to COMP rolls",
        "dead vermin found on occasion",
        "dilapidated interiors",
        "designed for a different species",
        "designed for water landings",
        "difficult to maintain (-1 to ENG)",
        "difficult to pilot (-1 to PILOT)",
        "difficult to start",
        "distinctive nose art",
        "easy to maintain (+1 to ENG)",
        "easy to pilot (+1 to PILOT)",
        "emergency escape bubbles",
        "emissions make it easy to track",
        "energy weapons do double damage",
        "energy weapons do half damage",
        "engineer robot (can't leave ship)",
        "engine room is very hot. Costly to fix.",
        "engines have a distinctive whine",
        "engines hum pleasantly",
        "engines run hot (+40°C at drives)",
        "engines smoke in atmosphere",
        "entirely robotic crew",
        "exhaust gas fills Engineering",
        "experienced crew (crew has min. skill level 3)",
        "exposed live electrical wiring",
        "false registry papers found onboard",
        "faulty acceleration compensators",
        "faulty grav deck plating",
        "firefight damage to interior",
        "flickering internal ship lights",
        "flushing toilets activates hull breach alarm",
        "free Netflix",
        "fuel efficient (-10% on fuel costs)",
        "fuel inefficient (+10% on fuel costs)",
        "fuel skimmers smell of fish",
        "has smuggling compartments",
        f"hidden space contains {random.choice(loot)}",
        "high performance fuel scoops",
        "high tech weapons locker",
        "highly automated (+1 to all crew rolls)",
        "highly custom (-1 to repairs)",
        "hull spotted with small arms fire",
        "illegal drugs are found on board",
        "illegal weapons system is found",
        f"inertial dampener lag {random.choice(negmodifiers)} to DEX",
        "inescapable brig",
        "infested with insects",
        "infested with vermin",
        "interior doors hum pleasantly",
        "interior doors work poorly",
        "interior lights blink on startup",
        "interior lights flicker during jump",
        "intermittent black globe cloak",
        "internal comm system on the fritz",
        f"jerky turret: {random.choice(negmodifiers)} to GUNNERY rolls",
        "jump drive causes mild jump sickness",
        "landing gear won't retract on 9+",
        f"leaks {random.choice(fluids)} when docked",
        "lights flicker occasionally",
        "liquid crystal hull with many patterns",
        "looks like a piece of junk",
        "loose deck plating prohibits running",
        "lots of battle scars",
        "luxurious interiors",
        "luxury crew staterooms",
        "luxury passenger staterooms",
        "luxury ship's vehicle",
        "main airlock sticks on 9+",
        f"main turret: {random.choice(posmodifiers)} to GUNNERY rolls",
        f"main turret: {random.choice(negmodifiers)} to GUNNERY rolls",
        "mass produced (+1 to repairs)",
        "medical robot (can't leave ship)",
        "military grade sensor suite",
        "misjumps on 12+ (each jump)",
        "nav computer locks up on 12+",
        "needs frequent repair",
        "needs new part",
        "needs repair (-1 to all crew rolls)",
        "noisy air system",
        "non-standard airlock connectors",
        "novice crew (crew has max. skill level 1)",
        "on the run from creditors",
        "poor environmental controls",
        "poor galley (-1 to STEWARD)",
        "poorly maintained (-1 to ENG)",
        "potable water tastes bad",
        "previous owner wants ship back",
        "pristine - not a scratch on her",
        "random audible warnings (1/day)",
        "random fire suppression system",
        "random warning lights (1/day)",
        "recently replaced jump drive",
        "refit time is fast (-20% time)",
        "refit time is slow (+20% time)",
        "refuel time is fast (-20% time)",
        "refuel time is slow (+20% time)",
        "reliable (+1 to crew rolls)",
        "requires proprietary parts",
        "rich Corinthian leather",
        f"robotic brain gunnery: {random.choice(posmodifiers)} to GUNNERY",
        f"robotic brain navigator:{random.choice(posmodifiers)} to NAV",
        f"robotic brain pilot: {random.choice(posmodifiers)} to PILOT",
        "robotic cargo handling system",
        "runs illegal Watchdog software",
        "secondary airlock inoperable",
        "sensors work at double their range",
        "sensors work at half their range",
        "several hull patches of questionable integrity",
        "ship is an obvious lemon",
        "ship kept clean by schloobies",
        "ship's computer is very slow",
        "ship's transponder is +1 to modify",
        "sketchy history/repeatedly renamed",
        "sleeper (looks bad, runs great)",
        "smelly air handling system",
        "sonic showers cause comm static",
        "spacious crew staterooms",
        "spacious passenger staterooms",
        "steward robot (can't leave ship)",
        "strange noises in crew quarters",
        "sub-standard crew staterooms",
        "sub-standard passenger staterooms",
        "suffers from Sick Ship Syndrome",
        "superior control interface (+1 to bridge activities)",
        "surface rust on various ship parts",
        "suspicious: -1 to law encounters",
        f"temp stays a constant {random.choice(temp)} deg. C",
        "terrible smell in (location)",
        f"transponder has {random.choice(d4)} switchable I.D.s",
        "transponder is twitchy",
        "trusted: +1 to law encounters",
        "turrets are hidden (pop-out)",
        "ugly color scheme",
        "uncomfortable bridge seats",
        "undetected gas causes sickness",
        "unpressurized cargo area",
        "unreliable (-1 to crew rolls)",
        "unsightly stains in fresher",
        "untested alien autodoc",
        "untraceable smell of burnt electronics",
        "untraceable ship's history",
        "used to be a military ship",
        "used to be a smuggling ship",
        "used to belong to a nearby noble",
        f"{random.choice(loot)} found in hidden space",
        "variable environment cargo space",
        "vents smelly steam on landing",
        "vibrates violently when going into/out of jump",
        "viewports fog up during flight",
        "water landing very difficult",
        "water supply tastes funny",
        "weak shields (-1)",
        f"weapons drain power from {random.choice(powered_systems)}",
        "well loved (+1 to ENG)"
    ]
    
    # If the user asks for more quirks than the list has, warn them
    if n > len(quirksandperks_list):
        print(f"Warning: There are only {len(quirksandperks_list)} unique quirks/perks available. I will give you all of them.")
        n = len(quirksandperks_list)

    print(f"\nGenerating {n} random quirks/perks...\n")
    
    # Shuffle the list so we can pick items without repetition
    random.shuffle(quirksandperks_list)

    for i in range(n):
        # Pick the first item in the shuffled list (without duplication)
        print(quirksandperks_list[i])

# Run the function
get_random_choices()
