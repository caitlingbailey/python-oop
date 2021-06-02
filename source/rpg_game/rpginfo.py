class RPGInfo():
    '''
    Information about the game and author
    '''
    author = "Anonymous"

    def __init__(self, game_title):
        self.title = game_title
   
    def welcome(self):
        print("Welcome to " + self.title)
        print('''
                                     -|             |-
         -|                  [-_-_-_-_-_-_-_-]                  |-
         [-_-_-_-_-]          |             |          [-_-_-_-_-]
          | o   o |           [  0   0   0  ]           | o   o |
           |     |    -|       |           |       |-    |     |
           |     |_-___-___-___-|         |-___-___-___-_|     |
           |  o  ]              [    0    ]              [  o  |
           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
_____----- |     ]              [ ||||||| ]              [     |
           |     ]              [ ||||||| ]              [     |
       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
      ( (__________------------_____________-------------_________) )
      ''')

    @staticmethod
    def info():
        print("Made using the OOP RPG game creator")
    
    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print(f"Created by {cls.author}")