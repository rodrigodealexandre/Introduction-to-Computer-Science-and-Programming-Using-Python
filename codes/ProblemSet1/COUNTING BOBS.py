 # Paste your code into this box
if len(s) > 0:
    count_bob = 0
    for n in range(len(s)):
        if s.startswith( 'bob', n ) == True:
            count_bob += 1
    print "Number of vowels:", count_bob
    