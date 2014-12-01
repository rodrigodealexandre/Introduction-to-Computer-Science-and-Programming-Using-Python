def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    dic = string.ascii_lowercase
    
    for letter in lettersGuessed:
        if dic.find(letter) >= 0:
            dic = dic.replace(letter, "")
    return dic