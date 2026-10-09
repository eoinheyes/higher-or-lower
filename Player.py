class Player:
    def __init__(self, username, score):
        self.username = username
        self.score = score
    
    def __str__(self):
        return self.username, self.score