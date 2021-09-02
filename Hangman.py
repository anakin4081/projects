#Hangman
import random



def playhangman():
    keyboard = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
        "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    lives, x, letters = 10, [], " ".join(keyboard)
    word = random.choice(Defs.liwo)
    for y in range(len(word)):
            x.append("*")
    while lives != 0:    
        print(len(word),"letters")
        wrd = "".join(x)
        print(wrd)    
        print((lives),"guesses remaining")
        print("---letters---")
        letters = " ".join(keyboard)
        print(letters)
        if word == wrd:
            print("you win!!!""\n\n")
            playhangman()
        while True:
            choice = input("pick a letter  ")[0]
            if choice not in letters:
                print("letter already used")
            else:
                keyboard.remove(choice)
                break
        if choice not in word:
            print("try again")
            lives -= 1
        total = index = 0
        while index < len(word):
            if word[index : index + len(choice)] == choice:
                x.insert(index, word[index])
                x.pop(index + 1)
                print(index)
                #total, index += 1, len(choice)
            else:
                index += 1
        
    print("game over")

playhangman()