"""Project Two starter for the student's text-based adventure game."""

# Lauren Surles
# IT 140 - Project Two
# Y2K Mall After Dark



def show_instructions():
    """Display the game objective and available commands."""
    print("====================================")
    print("       Y2K MALL AFTER DARK")
    print("====================================")
    print("The mall is closed, but you're still inside!")
    print("Collect all 6 items before encountering")
    print("the Night Manager to escape the mall.")
    print()
    print("Move commands: go north, go south, go east, go west")
    print("Collect items: get <item name>")
    print("====================================")


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("\n------------------------------------")
    print(f"You are in the {current_room}.")
    print(f"Inventory: {inventory}")

    # Display an item only if the room contains one.
    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}.")

    print("------------------------------------")



def main():
    """Run the main gameplay loop."""

    # Define the mall rooms, connecting directions, and items.
    rooms = {
        'Food Court': {
            'north': 'Replay Records',
            'south': 'Flashback Photo Booth',
            'east': 'Pixel Palace Arcade',
            'west': 'Glow Beauty'
        },
        'Replay Records': {
            'south': 'Food Court',
            'item': 'Burned CD'
        },
        'Glow Beauty': {
            'east': 'Food Court',
            'item': 'Lip Gloss'
        },
        'Pixel Palace Arcade': {
            'west': 'Food Court',
            'item': 'Arcade Token'
        },
        'Flashback Photo Booth': {
            'north': 'Food Court',
            'south': 'Starstruck Department Store',
            'item': 'Photo Strip'
        },
        'Starstruck Department Store': {
            'north': 'Flashback Photo Booth',
            'west': 'Electronics Store',
            'east': 'Security Office',
            'item': 'Employee Keycard'
        },
        'Electronics Store': {
            'east': 'Starstruck Department Store',
            'item': 'Flip Phone'
        },
        'Security Office': {
            'west': 'Starstruck Department Store',
            'villain': 'The Night Manager'
        }
    }

    # Start the player in the Food Court.
    current_room = 'Food Court'

    # Store items collected during gameplay.
    inventory = []

    # Display the game instructions.
    show_instructions()


    # Continue gameplay until the player wins or loses.
    while True:
        show_status(current_room, inventory, rooms)

        # Ask the player what they want to do next.
        command = input("Enter your move: ").strip().lower()

        # Handle movement commands.
        if command.startswith("go "):
            direction = command[3:]

            if direction in ("north", "south", "east", "west") and direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print(f"\nYou moved to the {current_room}.")
            else:
                print("\nYou can't go that way!")

        # Handle item collection commands.
        elif command.startswith("get "):
            item_name = command[4:]
            room_item = rooms[current_room].get("item")

            if room_item and item_name == room_item.lower():
                inventory.append(room_item)
                del rooms[current_room]["item"]
                print(f"\nYou collected the {room_item}!")
            else:
                print("\nThat item isn't available here!")

        # Handle unrecognized commands.
        else:
            print("\nInvalid command. Try 'go north' or 'get Lip Gloss'.")

        # Check whether the player encountered the villain.
        if "villain" in rooms[current_room]:
            if len(inventory) == 6:
                print("\nYou collected all 6 items and escaped the mall!")
                print("Congratulations! You win!")
            else:
                print("\nThe Night Manager caught you!")
                print("GAME OVER!")
            print("Thanks for playing Y2K Mall After Dark!")
            break



if __name__ == "__main__":
    main()
