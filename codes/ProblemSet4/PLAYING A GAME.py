def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    global HAND_SIZE, hand, copyhand
    n= HAND_SIZE
    
    command = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:').lower()
    if command == "n":
        hand = dealHand(n)
        copyhand = hand
        playHand(hand, wordList, n)
        return playGame(wordList)
    elif command == "r":
        if 'hand' in globals():
            hand = copyhand
            playHand(hand, wordList, n)
            return playGame(wordList)
        else:
            print "You have not played a hand yet. Please play a new hand first!"
            return playGame(wordList) 
    elif command == "e":
        if 'hand' in globals():
            del hand
            del copyhand
            return None
        else:
            return None

    else:
        print "Invalid command."
        return playGame(wordList)

