import os
from datetime import datetime
import xml.etree.ElementTree as ET

# Global variables for vessel name and ID
vessel_name = None
vessel_id = None
log_filename = None
user_name = None
user_rank = None

# Log categories with descriptions
log_categories = {
    "1": "Ship's Activities: General activities (e.g., departure, arrival, course changes, docking, maintenance)",
    "2": "System Status Updates: Information about ship’s critical systems (Drive, Life Support, Communications)",
    "3": "Crew Log: Notes on crew activities, sickbay visits, shifts, notable crew actions",
    "4": "Cargo Log: Details about cargo, changes in cargo status, inventory notes, inspections",
    "5": "Shipboard Incidents: Any incidents, accidents, conflicts, or unusual events on the ship",
    "6": "Scientific/Exploratory Notes: Exploration of planets, anomalies encountered, sensor logs",
    "7": "Notes from the Captain: Personal notes or comments from the Captain about the mission",
    "8": "Repairs/Maintenance Log: Details of repairs, system failures, or parts replaced",
    "9": "Manual Entry: Free-form log entry",
}


def prompt_for_vessel_details():
    """Prompt the user for the vessel's name and ID code."""
    global vessel_name, vessel_id, log_filename
    if vessel_name is None or vessel_id is None:
        print("\n--- Vessel Setup ---")
        vessel_name = input("Enter the vessel's name: ")
        vessel_id = input("Enter the vessel's ID code (e.g., VESSEL-1234): ")
        log_filename = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            f"{vessel_name}_{vessel_id}_log.xml",
        )
        print(f"Vessel: {vessel_name} ({vessel_id})\n")
        save_initial_vessel_details()


def save_initial_vessel_details():
    """Save the vessel name and ID code to the XML file if they don't already exist."""
    if not os.path.exists(log_filename):
        root = ET.Element("log")
        tree = ET.ElementTree(root)
        tree.write(log_filename)


def prompt_for_user_details():
    """Prompt the user for their name and rank on first login."""
    global user_name, user_rank
    if user_name is None or user_rank is None:
        print("\n--- Welcome to the Ship Log System ---")
        user_name = input("Enter your name (Captain's Name): ")
        user_rank = input("Enter your rank (e.g., Captain, First Officer): ")
        print(f"Welcome, Captain {user_name} ({user_rank})!\n")
        save_initial_log_details()


def save_initial_log_details():
    """Save the name and rank to the XML file if they don't already exist."""
    if not os.path.exists(log_filename):
        tree = ET.parse(log_filename)
        root = tree.getroot()
        initial_entry = ET.SubElement(root, "entry")
        initial_entry.set("captain", user_name)
        initial_entry.set("rank", user_rank)
        initial_entry.set("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        tree.write(log_filename)


def prompt_for_ship_status():
    """Prompt for the ship's current status."""
    print("\n--- Ship Status ---")
    destination = input("Current destination: ")
    captain_status = input("Captain's Status (Active, On Leave, Incapacitated): ")
    crew_status = input("Crew Status (Full Complement, Missing Personnel, etc.): ")
    cargo_status = input(
        "Cargo Status (Cargo Held, Unloaded, Manifest Attached, etc.): "
    )

    return destination, captain_status, crew_status, cargo_status


def prompt_for_entry_details():
    """Prompt the user for more structured log details."""
    print("\n--- New Log Entry ---")

    # Display the categories
    print("\nSelect a category for the log entry:")
    for key, value in log_categories.items():
        print(f"{key}. {value}")

    entry_type = input("\nEnter the number of the category: ")
    while entry_type not in log_categories:
        print("Invalid choice. Please select a valid category.")
        entry_type = input("\nEnter the number of the category: ")

    entry_type_description = log_categories[entry_type]
    print(f"\nYou selected: {entry_type_description}")

    # Record the entry specifics
    location = input("Location (e.g., Planet Name, Star System, Coordinates): ")
    description = input("Brief Description of the event or situation: ")

    return entry_type, entry_type_description, location, description


def prompt_for_manual_date():
    """Prompt for the log entry date in Imperial Calendar format (ddd yyyy)."""
    date_input = input("Enter the log date (Imperial Calendar: ddd yyyy): ")
    try:
        imperial_date = datetime.strptime(date_input, "%j %Y")
        return imperial_date.strftime("%Y-%m-%d")  # Convert to standard date format
    except ValueError:
        print("Invalid date format. Please use ddd yyyy format.")
        return (
            prompt_for_manual_date()
        )  # Recursively ask for the date until correct format


def write_log():
    """Function to write a new log entry."""
    prompt_for_user_details()  # Ensure we have the captain's details
    destination, captain_status, crew_status, cargo_status = prompt_for_ship_status()
    entry_type, entry_type_description, location, description = (
        prompt_for_entry_details()
    )
    log_date = prompt_for_manual_date()  # Prompt for manual date entry

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create the new log entry
    entry = ET.Element("entry")
    entry.set("date", log_date)
    entry.set("captain", user_name)
    entry.set("rank", user_rank)
    entry.set("timestamp", timestamp)

    entry_type_elem = ET.SubElement(entry, "log_type")
    entry_type_elem.text = entry_type_description

    location_elem = ET.SubElement(entry, "location")
    location_elem.text = location

    description_elem = ET.SubElement(entry, "description")
    description_elem.text = description

    destination_elem = ET.SubElement(entry, "destination")
    destination_elem.text = destination

    captain_status_elem = ET.SubElement(entry, "captain_status")
    captain_status_elem.text = captain_status

    crew_status_elem = ET.SubElement(entry, "crew_status")
    crew_status_elem.text = crew_status

    cargo_status_elem = ET.SubElement(entry, "cargo_status")
    cargo_status_elem.text = cargo_status

    # Save to XML file
    tree = ET.parse(log_filename)
    root = tree.getroot()
    root.append(entry)
    tree.write(log_filename)

    print("Log entry saved.\n")


def write_emergency_log():
    """Function for creating an emergency log entry with minimal details."""
    print("\n--- Emergency Log Entry ---")
    emergency_name = input("Enter your name (Captain's Name): ")
    emergency_rank = input("Enter your rank (e.g., Captain, First Officer): ")
    emergency_date = prompt_for_manual_date()  # Ask for a manual date entry
    emergency_entry = input("Enter the emergency log entry text: ")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create the emergency log entry
    emergency_entry_elem = ET.Element("entry")
    emergency_entry_elem.set("date", emergency_date)
    emergency_entry_elem.set("captain", emergency_name)
    emergency_entry_elem.set("rank", emergency_rank)
    emergency_entry_elem.set("timestamp", timestamp)

    emergency_log_elem = ET.SubElement(emergency_entry_elem, "emergency_log")
    emergency_log_elem.text = emergency_entry

    # Save to XML file
    tree = ET.parse(log_filename)
    root = tree.getroot()
    root.append(emergency_entry_elem)
    tree.write(log_filename)

    print("Emergency log entry saved.\n")


def view_logs():
    """Function to view the saved logs, grouped by Imperial date."""
    if os.path.exists(log_filename):
        tree = ET.parse(log_filename)
        root = tree.getroot()

        if root:
            logs_by_date = {}

            for entry in root.findall("entry"):
                date = entry.get("date")
                if date not in logs_by_date:
                    logs_by_date[date] = []
                logs_by_date[date].append(entry)

            sorted_dates = sorted(
                logs_by_date.keys(), reverse=True
            )  # Sort dates in reverse order (most recent first)

            print(f"\n--- {vessel_name} ({vessel_id}) Ship Logs ---")
            for date in sorted_dates:
                print(f"\nDate: {date}")
                for entry in logs_by_date[date]:
                    print(f"Captain: {entry.get('captain')} ({entry.get('rank')})")

                    # Check if the entry is a regular log or an emergency log
                    log_type_elem = entry.find("log_type")
                    if log_type_elem is not None:
                        print(f"Log Type: {log_type_elem.text}")
                    else:
                        emergency_log_elem = entry.find("emergency_log")
                        if emergency_log_elem is not None:
                            print(f"Emergency Log Entry: {emergency_log_elem.text}")

                    location_elem = entry.find("location")
                    if location_elem is not None:
                        print(f"Location: {location_elem.text}")

                    description_elem = entry.find("description")
                    if description_elem is not None:
                        print(f"Description: {description_elem.text}")

                    destination_elem = entry.find("destination")
                    if destination_elem is not None:
                        print(f"Destination: {destination_elem.text}")

                    captain_status_elem = entry.find("captain_status")
                    if captain_status_elem is not None:
                        print(f"Captain's Status: {captain_status_elem.text}")

                    crew_status_elem = entry.find("crew_status")
                    if crew_status_elem is not None:
                        print(f"Crew Status: {crew_status_elem.text}")

                    cargo_status_elem = entry.find("cargo_status")
                    if cargo_status_elem is not None:
                        print(f"Cargo Status: {cargo_status_elem.text}")

                    print("-" * 50)
        else:
            print("No logs found.")
    else:
        print("No logs file found.")


def clear_logs():
    """Function to clear all saved logs."""
    if os.path.exists(log_filename):
        confirm = input("Are you sure you want to delete all logs? (y/n): ")
        if confirm.lower() == "y":
            os.remove(log_filename)
            print("All logs have been deleted.")
        else:
            print("Log deletion cancelled.")
    else:
        print("No logs to delete.")


def main():
    """Main function to interact with the user."""
    global vessel_name, vessel_id  # Ensure these are declared global in the main function

    prompt_for_vessel_details()  # Ensure we have the vessel details

    while True:
        print(f"\n--- {vessel_name} ({vessel_id}) Ship Log ---")
        print("1. Record a new log entry")
        print("2. Write an emergency log entry")
        print("3. View logs")
        print("4. Clear all logs")
        print("5. Switch to a different ship")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            write_log()
        elif choice == "2":
            write_emergency_log()
        elif choice == "3":
            view_logs()
        elif choice == "4":
            clear_logs()
        elif choice == "5":
            print("Switching to a different ship...\n")
            # Reset global variables for a new ship
            vessel_name = None
            vessel_id = None
            user_name = None
            user_rank = None
            main()  # Restart the program to set up a new vessel
            break
        elif choice == "6":
            print("Exiting ship log system. Safe travels!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
