import json

filename = "scentsy_counts.json"

"""
scentsyItems = {
    "warmers": {
        "iron man": "1",
        "jack skellington": "1",
        "pink salt rock": "1",
        "test": "1",
        "newtest": 5,
        "letterboard": "1"
    },
    "bars": {
        "mystery man": "15",
        "very bery twist": "3",
        "orange mint": "4",
        "flava": "2"
    },
    "scent circles": {
        "flava": "1",
        "jayden smelly goody": "1"
    },
    "carbar": {
        "mystery man": "1",
        "my new test": "3",
        "another new item": "99"
    },
} 
"""


def load():
    try:
        with open(filename) as f_obj:
            items = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return items


def save(items):

    with open(filename, "w") as f_obj:
        json.dump(items, f_obj, indent=4)


def add_new():

    category = input("What category would you like to add to? >> ")
    scentsyItems = load()
    is_new = True
    is_a_category = False

    for key in scentsyItems.keys():
        if category == key:
            is_a_category = True
            break
    
    if is_a_category: # If category exists, check item
        new_entry = input("What is the name of the item? >> ")
        for key, items in scentsyItems.items():
            for nest_key in items.keys():
                if nest_key == new_entry:
                    is_new = False
                    break
        
        if is_new:
            print(f"Is {new_entry} a new item you would like to add? (y/n)")
            check_new_item = input(">> ")

            if check_new_item.lower() == 'y':
                new_item_count = int(input(f"How many of {new_entry} do you have? >> "))
                scentsyItems[category][new_entry] = new_item_count
                save(scentsyItems)
            elif check_new_item.lower() == 'n':
                print("Okay, goodbye.")
            else:
                print("error")
        else:
            print("That item exists already, are you adjusting the count? (y/n)")
            check_new_count = input(">> ")
            if check_new_count.lower() == 'y':
                new_count = int(input("What is the new amount? >> "))
                scentsyItems[category][new_entry] = new_count
                save(scentsyItems)
            elif check_new_count.lower() == 'n':
                print("Okay, goodbye.")
            else:
                print("error.")
    else:
        print("That category doesn't exist, would you like to create it? (y/n)")
        check_new_category = input(">> ")
        if check_new_category.lower() == 'y':
            print(f"New category '{category}' has been added, what item would you like to add?")

            new_entry = input(">> ")
            new_entry_amount = int(input("How many do you have? >> "))
            
            scentsyItems[category] = {new_entry: new_entry_amount}

            save(scentsyItems)
            print(f"{new_entry.title()} has been added with the amount of {new_entry_amount}.")
        elif check_new_category.lower() == 'n':
            print("Okay, goodbye.")
        else:
            print("error.")