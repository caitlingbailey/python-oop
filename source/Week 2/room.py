class Room():
    '''
    This is a docstring
    '''
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_description(self, room_description):
        self.description = room_description
    
    def get_description(self):
        return self.description
    
    def describe(self):
        print( self.description )

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def get_details(self):
        print(f"The {self.name}")
        print("---------------")
        print(f"{self.description}")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")
        print("\n")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self