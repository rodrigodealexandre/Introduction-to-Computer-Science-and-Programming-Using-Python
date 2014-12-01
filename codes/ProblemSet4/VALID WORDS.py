def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    
    newword = {}
    for x in word:
        newword[x] = newword.get(x,0) + 1
    
    for l in newword:
        if newword.get(l,0) > hand.get(l, 0):
            return False
    
    is_valid = False
    for n in wordList:
        if word == n:
            return True
            
    return False