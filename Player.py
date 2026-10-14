import csv
class Player:
    def __init__(self, username, score):
        self.username = username
        self.score = score
    
    def __str__(self):
        return self.username, self.score

    def highScore(self, score):
        self.score = score
        self.save()

    def save(self):
        scores = []
        foundUser = False
        with open("scores.csv","r",newline="") as file:
            reader = csv.reader(file)
            scores = list(reader)
            for row in scores:
                if row[0] == self.username:
                    row[1] = str(self.score)
                    foundUser = True
                    break
        if not foundUser:
            scores.append([self.username, str(self.score)])
        with open("scores.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(scores)
