# Idea for Sydney's business
    # >> View inventory of scensty items
    # >> Add new items to inventory
    # >> Update counts
        # >> Will require a remove keyword
    # >> Save to excel spreadsheet
    #     >> Formatted, possibly graph?
    # >> Load excel spreadsheet to program

from test import load, save, add_new

active = True

print("\nWelcome to your inventory program, Sydney!")

# Main program loop
while active:
    prompt = input(f"\nWhat would you like to do first?"
                    "\nView inventory 'view'"
                    "\nAdd new items 'add'"
                    "\nUpdate counts 'update'"
                    "\nDelete an item 'delete'"
                    "\nSave 'save'"
                    "\n>> ")
    
    scentsyItems = load()
    
    # View the current inventory
    if prompt == 'view':
        # Category
            # Item: Count
        
        # Loop through main dictionary
        for category, item in scentsyItems.items():
            print(f"\nCategory: {category.title()}")

            for key, value in item.items():
                print(f"\tScent: {key.title()} | Amount: {value}")
    # Add to the current inventory
    elif prompt == 'add':
        # Gather what category
            # input the item and the amount after
            # Check if the item already exists, and just add the amount to current
        add_new()
    elif prompt == 'update':
        # Loop through all items and ask for a new value
        
        for category, info in scentsyItems.items():
             print(f"\nCategory: {category.title()}")

             for item in info.keys():
                try:
                    newValue = int(input(f"How many {item.title()} do you have? >> "))
                except ValueError:
                    newValue = 0

                print(f"Update: {item.title()}: {newValue}\n")
                scentsyItems[category][item] = newValue
                save(scentsyItems)
                continue
    
    elif prompt == 'save':
        # Save into .json file
        save(scentsyItems)
    elif prompt == 'delete':
        # Delete an item from a category
        category = input("What category are you looking for? >> ")

        for key, value in scentsyItems.items():
            if category == key:
                print(f"You have accessed the '{category.title()}' category.\n")
                for nested_key, nested_value in value.items():
                    print(f"Scent: {nested_key.title()} | Amount: {nested_value}")
                
                item = input("\nWhat item would you like to delete? >> ")

                # Loop through the nested dict and check if the item exists,
                # if so, prompt confirmation, then delete key and value.
                for nest_key, nest_value in value.items():
                    if item == nest_key:
                        print(f"Would you like delete all {item.title()}? (y/n)")
                        check_delete_all = input(">> ")

                        if check_delete_all.lower() == 'y':
                            # delete the item
                            scentsyItems[category].pop(item)
                            save(scentsyItems)
                            print(f"{item.title()} has been successfully deleted.")
                            break
                        elif check_delete_all.lower() == 'n':
                            # ask how many they want to delete
                            delete_quantity = int(input("How many do you want to delete? >> "))
                            if delete_quantity > nest_value:
                                delete_quantity = int(input("Sorry, that amount is too much, try again. >> "))
                            elif delete_quantity == nest_value:
                                scentsyItems[category].pop(item)
                                print(f"{item.title()} has been successfully deleted.")
                            elif delete_quantity < nest_value:
                                new_value = nest_value - delete_quantity
                                scentsyItems[category][item] = new_value
                                print(f"You have removed {delete_quantity} from the {item.title()}.")
                            save(scentsyItems)
                            break

                        else:
                            print("error.")
    elif prompt == 'quit' or prompt == 'q':
        print("Goodbye.")
        active = False