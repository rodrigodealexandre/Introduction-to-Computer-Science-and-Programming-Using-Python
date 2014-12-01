balance = 999999
annualInterestRate = 0.18

# Paste your code into this box
if balance > 0:
    
    lastbalance = 1
    mir = (annualInterestRate / 12.0)
    mini = balance/12
    maxi = (balance * (1 + mir)**12)/12.0
    
    while lastbalance > 0.01 or lastbalance < -0.01:
        lp = (maxi + mini)/2
        lastbalance = balance
        for n in range(12):
            upb = lastbalance - lp
            lastbalance = upb + mir * upb
        if lastbalance < 0:
            maxi = lp
        else:
            mini = lp
                    
                                            
    print "Lowest Payment:", round(lp,2)