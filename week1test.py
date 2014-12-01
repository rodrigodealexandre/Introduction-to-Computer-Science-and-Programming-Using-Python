# Week 1 simple exercises

varB = 2
varA = 2

if type(varA) == str or type(varB) == str:
    print("string involved")
else:
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    elif varA < varB:
        print("smaller")
