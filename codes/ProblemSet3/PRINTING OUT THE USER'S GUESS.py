guessed_words = ""
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    global guessed_words
    letters = ""
    if len(secretWord) > 0:
        for let1 in secretWord:
            for let2 in lettersGuessed:
                if let1 == let2:
                    letters = True
                    break
                else:
                    letters = False
            break
        if letters == True:
            guessed_words += let1
            return getGuessedWord(secretWord[1:], lettersGuessed)
        else:
            guessed_words += "_ "
            return getGuessedWord(secretWord[1:], lettersGuessed)
    else:
        output = guessed_words
        guessed_words = ""
        return output