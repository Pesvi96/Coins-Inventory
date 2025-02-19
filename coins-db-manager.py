import json
import os


def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {"coins": []}  # Default if JSON is empty or invalid
    return {"coins": []}  # Default if file doesn't exist


def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def get_next_id(coins):
    return max((coin["id"] for coin in coins), default=0) + 1


def get_valid_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        elif value == "":
            return 1
        print("Invalid input. Please enter a valid number.")


def main():
    file_path = "coins.json"
    data = load_json(file_path)

    while True:
        choice = input("Do you want to add a coin in your database? (y/n): ").strip().lower()
        if choice == "n":
            print("Goodbye!")
            break
        elif choice != "y":
            print("Invalid input. Please enter 'y' or 'n'.")
            continue

        # Get user input for the new coin
        new_id = get_next_id(data["coins"])
        print(f"Current ID is {new_id}")
        country = input("Please indicate country: ").strip()
        currency = input("Please indicate currency: ").strip()
        year = get_valid_int("Please indicate year: ")
        original_price = input("Please indicate original price: ").strip()
        text = input("Please indicate text on the coin: ").strip()
        selling_price = get_valid_int("Please indicate selling price: ")
        comment = input("Please add a comment: ").strip()
        amount = get_valid_int("Please indicate amount: ")

        # Construct new coin entry
        new_coin = {
            "id": new_id,
            "country": country,
            "year": year,
            "currency": currency,
            "original_price": original_price,
            "text": text,
            "photo_front": f"./images/{new_id}-front.jpg",
            "photo_back": f"./images/{new_id}-back.jpg",
            "selling_price": selling_price,
            "comment": comment,
            "amount": amount
        }

        # Add to the database and save
        data["coins"].append(new_coin)
        save_json(file_path, data)
        print(f"Coin ID {new_id} added successfully!\n\n")


if __name__ == "__main__":
    main()
