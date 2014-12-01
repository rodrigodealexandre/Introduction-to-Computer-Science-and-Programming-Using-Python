def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    guessed = ""
    guessedtf = True
    if len(lettersGuessed) == 0:
        return False
    elif len(secretWord) != 0:
        for letter in secretWord:
            for guess in lettersGuessed:
                if letter != guess:
                    guessed = False
                else:
                    guessed = True
                    break
            guessedtf = guessedtf and guessed
        return guessedtf