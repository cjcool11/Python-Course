class flashcards:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word + ' ('+self.meaning+')'
    

flash = []

while(True):
    word = input("put the word you want to to add to flashcard: ")
    meaning = input("put the meaning of the word: ")

    flash.append(flashcards(word, meaning))
    option = int(input("enter 0 if you want to add another flashcard otherwise enter 1: "))

    if(option):
        break

print("here are your flashcards: ")
for i in flash:
    print(">",i)