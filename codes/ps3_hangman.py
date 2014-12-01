# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"
guessed_words = ""
started = False
nguess = 8

lettersGuessed = []

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


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
                    
         





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
