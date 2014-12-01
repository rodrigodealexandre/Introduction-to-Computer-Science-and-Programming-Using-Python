 # Paste your code into this box
if len(s) > 0:
    s += ' '
    count_let = 0
    current_let = ''
    long_alp = ''
    lst = []
    for l in s:
        if l >= current_let:
            long_alp += l   
            current_let = l
            
        else:
            lst.append(long_alp)
            long_alp = l
            current_let = l
    j = 0
    my = ''
    for n in lst:
        if len(n) > j:
            j = len(n)
            my = n
    print "Longest substring in alphabetical order is:", my
    