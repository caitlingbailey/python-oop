class Room():
    '''
    This is a docstring
    '''
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
    
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