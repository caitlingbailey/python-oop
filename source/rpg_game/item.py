class Item():
    '''
    Creates an item in game.
    '''
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
    
    def set_name(self, item_name):
        self.name = item_name
    
    def get_name(self):
        return self.name
    
    def describe(self):
        print(f"A {self.name} is here.")
        print( self.description )
    
    def set_description(self, item_description) -> None:
        self.description = item_description
    
