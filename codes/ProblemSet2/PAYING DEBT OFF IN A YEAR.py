# Paste your code into this box
if balance > 0:
    lp = 0
    lastbalance = 1
    while lastbalance >= 0:
        lp += 10
        lastbalance = balance
        for n in range(12):
            upb = lastbalance - lp
            lastbalance = upb + (annualInterestRate / 12.0) * upb
                    
    print "Lowest Payment:", lp