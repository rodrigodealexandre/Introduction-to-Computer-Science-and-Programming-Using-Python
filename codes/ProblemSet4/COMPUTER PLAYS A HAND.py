def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    
    # Create a new variable to store the maximum score seen so far (initially 0)
    t_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    b_word = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList) == True:
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > t_score:
                # Update your best score, and best word accordingly
                t_score = score
                b_word = word

    # return the best word you found.
    return b_word, t_score

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total_points = 0
    
    while calculateHandlen(hand) > 0:
        return_value = 0
        print ("Current Hand:"),
        return_value = displayHand(hand)
        word_score = compChooseWord(hand, wordList, n)
        if word_score[0] != None:
            total_points += word_score[1]
            print '"'+ word_score[0]+ '"', "earned",  word_score[1], "points. Total:", total_points, "points"
            hand = updateHand(hand, word_score[0])
        else:
            break
    print "Total score:", total_points, "points."