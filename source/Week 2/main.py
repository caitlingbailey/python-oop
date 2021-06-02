# Imports
from room import Room
from item import Item
from character import Enemy
from character import Character

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
evan.set_weakness("sunlight")

dining_hall.set_character(dave)
ballroom.set_character(evan)


# Set up game

current_room = kitchen
alive = True

while alive:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()

    if inhabitant:
        inhabitant.describe()
    

    command = input("> ")
    
    if command in ["north", "east", "south", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant:
            inhabitant.talk()

    elif command == "fight":
        if inhabitant and isinstance(inhabitant, Enemy):
            outcome = inhabitant.fight(input("What will you fight with? "))
            if not outcome:
                print("Sorry, you died!\n")
                alive = outcome
            else:
                print("You won the fight!")
                current_room.set_character(None)
