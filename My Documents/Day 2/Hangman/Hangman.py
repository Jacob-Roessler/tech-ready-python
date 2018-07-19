import gb
 
def getword():
    word = str(input("Enter the word to guess: "))
    return word
def getguess():
    letter = str(input("Enter the letter to guess: "))
    return letter

def game(timesran, lives):
    while True:
        if timesran == 0:
            word = getword()
            template = []
            guesses = []
            for x in word:
                template.append('*')
        print("Word is: ", template)

        guess = getguess()
        guesses.append(guess)

        if guess in word:
            for x in range(len(word)):
                if word[x] == guess:
                    template[x] = guess
                    correct = 0
                    correct +=1
        else:
            print("Incorrect")
            lives-=1
            if lives == 5:
                gb.board1w()
            if lives == 4:
                gb.board2w()
            if lives == 3:
                gb.board3w()
            if lives == 2:
                gb.board4w()
            if lives == 1:
                gb.board5w()
            if lives == 0:
                gb.board6w()
        print("You have guessed:", guesses)
        if '*' not in template or lives == 0:
            print("Game Over", end = '')
            if lives == 0:
                print(", you lost")
            break
        timesran+=1
gb.board()
game(timesran=0,lives = 6)
