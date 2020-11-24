import string
import random
import requests

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

        # Check if the word is correct
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        #print(str(json_response))
        if json_response['found'] == False:
            result = False
            #print("not a correct word: "+word)

        return result



"""
https://wagon-dictionary.herokuapp.com/
{"message":"welcome","endpoints":["https://wagon-dictionary.herokuapp.com/:word","https://wagon-dictionary.herokuapp.com/autocomplete/:stem"],"total_api_hits":3671216,"words_found":2044038,"autocomplete_hits":863815}
"""
