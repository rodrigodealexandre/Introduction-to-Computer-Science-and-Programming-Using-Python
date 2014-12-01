#The game is think of a number, and the pc will guess what number it was.

# x is a fictice variable used for the infinite loop, mini and maxi are the minimal and maximal values, answ is the predicted answer.
x = -2
mini = 0
maxi = 100
answ = -1

print "Please think of a number between 0 and 100!"
# loop for figuring out the number you guessed.
while answ != x:
     answ = (maxi + mini)/2
     print "Is your secret number ",
     print answ,
     print "?"
     s = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
     
     #if the answer is higher than the number you thought.
     if s == "h":
         maxi = answ
            
     #if the answer is lower than the number you thought.            
     elif s == "l":
         mini = answ
                
     #if the answer is correct.                
     elif s == "c":
         print "Game over. Your secret number was: ", str(answ)
         break
                    
     #if the imput is no c, h, or l.                    
     else:
         print "Sorry, I did not understand your input."
     