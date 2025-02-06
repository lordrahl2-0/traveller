import random
import os


def load_words(filename):
    """Load words from a text file in the script's directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get script's directory
    filepath = os.path.join(script_dir, filename)  # Construct full path

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Warning: {filepath} not found. Using default words.")
        return []


def generate_company_name(category):
    """Generate a company name, sometimes using only a prefix for one-word names."""
    prefixes = load_words(f"{category}_prefixes.txt")
    suffixes = load_words(f"{category}_suffixes.txt")

    prefix = random.choice(prefixes) if prefixes else "Generic"

    # Random chance of omitting the suffix (e.g., 50% one-word names)
    if suffixes and random.random() > 0.5:
        suffix = random.choice(suffixes)
        return f"{prefix} {suffix}"

    return prefix  # Return only the prefix for one-word names


def main():
    categories = ["retail", "weapons", "vehicles", "luxury"]
    category = input(f"Enter company type ({', '.join(categories)}): ").strip().lower()

    if category not in categories:
        print("Invalid category. Defaulting to 'retail'.")
        category = "retail"

    try:
        count = int(input("How many company names do you want to generate? ").strip())
    except ValueError:
        print("Invalid number. Defaulting to 1.")
        count = 1

    for _ in range(count):
        company_name = generate_company_name(category)
        print(f"Generated Company Name: {company_name}")


if __name__ == "__main__":
    main()
