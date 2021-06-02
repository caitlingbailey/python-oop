from room import Room
from item import Item

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

current_room = kitchen

sword = Item("sword")
print(sword.get_name())
# while True:
#     print("\n")
#     current_room.get_details()
#     command = input("Which way? ")
#     current_room = current_room.move(command)