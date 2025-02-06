# This generator creates an Account Number for a Traveller Character
# or business based on the input - the output format is AAAAnnnn.

import random
import hashlib

print("Welcome to the Imperial Interstellar Bank Account Number Generator!")
accountType = input("Choose the type of account (Business or Personal)[b/p]: ")


def generate_personal_code(name, dob, id_number):
    input_string = f"{name.lower()}|{dob}|{id_number}"
    hash_obj = hashlib.md5(input_string.encode())  # Generate hash
    hex_digest = hash_obj.hexdigest()

    letters = "".join(
        [chr(65 + (int(hex_digest[i : i + 2], 16) % 26)) for i in range(0, 8, 2)]
    )
    numbers = "".join(
        [str(int(hex_digest[i : i + 2], 16) % 10) for i in range(8, 16, 2)]
    )

    return letters + numbers


def generate_business_code(name, account):
    input_string = f"{name.lower()}|{account}"
    hash_obj = hashlib.md5(input_string.encode())  # Generate hash
    hex_digest = hash_obj.hexdigest()

    letters = "".join(
        [chr(65 + (int(hex_digest[i : i + 2], 16) % 26)) for i in range(0, 8, 2)]
    )
    numbers = "".join(
        [str(int(hex_digest[i : i + 2], 16) % 10) for i in range(8, 16, 2)]
    )

    return letters + numbers


if accountType == "Personal" or accountType == "P" or accountType == "p":
    name = input("Enter your Full Name in the format First Name Last Name: ")
    dob = input("Enter your date of birth (YYYY-DDD): ")
    id_number = input("Enter your ID number: ")
    code = generate_personal_code(name, dob, id_number)
    print("Generated Code:", code)
elif accountType == "Business" or accountType == "B" or accountType == "b":
    name = input("Enter your Business Full Trading Name: ")
    account = input("Enter your account identifier: ")
    code = generate_business_code(name, account)
    print("Generated Code:", code)
else:
    print("Invalid Account Type Specified")
