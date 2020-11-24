import string
import random

class Game:

    def __init__(self):
        self.letter_choices = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.grid = []
        for i in range(9):
            index_letter = random.randint(1, len(self.letter_choices))
            #print(index_letter)
            self.grid.append(self.letter_choices[index_letter-1])
        #print(self.grid)

    def is_valid(self, word):
        result = True
        #print("word: "+word)
        #print("grid :"+str(self.grid))

        if word != None:
            copygrid = self.grid.copy()
            for letter in word:
                if letter in copygrid:
                    copygrid.remove(letter)
                    #print(copygrid)
                else:
                    result = False
        else:
            result = False

        return result
