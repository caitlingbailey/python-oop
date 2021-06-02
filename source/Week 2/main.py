# Imports
from room import Room
from item import Item
from character import Enemy
from rpginfo import RPGInfo

# Create game
spooky_castle = RPGInfo("The Spooky Castle")

# Create rooms
kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

dining_hall = Room("dining hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Create characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Braiiiiinnnnss!")
dave.set_weakness("cheese")

evan = Enemy("Evan", "A ghost!")
evan.set_conversation("Boo!")
evan.set_weakness("orange")

dining_hall.set_character(dave)
ballroom.set_character(evan)

# Create some items
cheese = Item("cheese")
cheese.set_description("Some smelly cheese. Wonder what this could be useful for?")
dining_hall.set_item(cheese)

orange = Item("orange")
orange.set_description("Yummy, a juicy orange!")
ballroom.set_item(orange)


# Set up game
spooky_castle.welcome()
RPGInfo.info()
print(f"There are {str(Room.number_of_rooms)} rooms to explore, and {Enemy.enemies_to_defeat} enemies to defeat.")

current_room = kitchen
alive = True
backpack = []

while alive:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()

    if inhabitant:
        inhabitant.describe()
    if item:
        item.describe()

    command = input("> ")
    
    if command in ["north", "east", "south", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant:
            inhabitant.talk()

    elif command == "fight":
        if inhabitant and isinstance(inhabitant, Enemy):
            fight_item = input("What will you fight with? ")
            if fight_item in backpack:
                outcome = inhabitant.fight(fight_item)
                if not outcome:
                    print("Sorry, you died!\n")
                    alive = outcome
                else:
                    print("You won the fight!")
                    current_room.set_character(None)
                    print(f"You have {Enemy.enemies_to_defeat} enemies to go.")

            else:
                print("You don't have that item!")

    elif command == "take":
        if item:
            print(f"You put the {item.get_name()} in your backpack.\n")
            backpack.append(item.get_name())
            current_room.set_item(None)
            print("You now have these in your backpack:\n")
            print(backpack)
    
    if Enemy.enemies_to_defeat == 0:
        print(f"Well done! You've defeated all the enemies.\n")
        print("You win!")
        alive = False


RPGInfo.author = "Caitlin"
RPGInfo.credits()