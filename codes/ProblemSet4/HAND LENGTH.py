def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    hand_length = 0
    for letter in hand.keys():
        for j in range(hand[letter]):
             hand_length += 1
    return hand_length

