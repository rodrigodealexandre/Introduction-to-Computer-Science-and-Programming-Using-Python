balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

if balance > 0:
    tp = 0
    for n in range(12):
        month = n+1
        print "Month:", month
        mpr = monthlyPaymentRate * balance
        tp += mpr
        upb = balance - mpr
        print "Minimum monthly payment:", round(mpr, 2)
        balance = upb + (annualInterestRate / 12.0) * upb
        print "Remaining balance:", round(balance, 2)
    print "Total paid:", round(tp, 2)
    print "Remaining balance:", round(balance, 2)