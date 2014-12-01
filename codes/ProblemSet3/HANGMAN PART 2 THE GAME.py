started = False
nguess = 8
lettersGuessed = []
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    global started, nguess, lettersGuessed
    if started == False:
        print "Welcome to the game, Hangman!"
        print "I am thinking of a word that is ",
        print len(secretWord),
        print " letters long."
        started = True
        return hangman(secretWord)
    
    else:
        print "-------------"
        print "You have",; print nguess,; print "guesses left."
        print "Available Letters:",; print getAvailableLetters(lettersGuessed)
        letter1 = raw_input("Please guess a letter:").lower()
        if len(lettersGuessed) != 0:
            for item in lettersGuessed:
                if item.find(letter1) != -1:
                    presence = True
                    break
                else:
                    presence = False
        else:
            presence = False
            
        if presence == False:
            lettersGuessed.append(letter1)
        else:
            print "Oops! You've already guessed that letter:",
            print getGuessedWord(secretWord, lettersGuessed)
            return hangman(secretWord) 
           
        if isWordGuessed(secretWord, lettersGuessed) == False:
            if nguess > 1:
                if secretWord.find(letter1) >= 0:
                    print "Good guess:",
                    print getGuessedWord(secretWord, lettersGuessed)
                    return hangman(secretWord)
                else:
                    print "Oops! That letter is not in my word:",
                    print getGuessedWord(secretWord, lettersGuessed)
                    nguess -= 1
                    return hangman(secretWord)
            else:
                print "Oops! That letter is not in my word:",
                print getGuessedWord(secretWord, lettersGuessed)
                print "-----------"
                print "Sorry, you ran out of guesses. The word was",
                print secretWord, ; print "."
                nguess = 8
                started = False
                lettersGuessed = []
        else:
            print "Good guess:",
            print getGuessedWord(secretWord, lettersGuessed)
            print "------------"
            print "Congratulations, you won!"
            started = False
            lettersGuessed = []
            nguess = 8