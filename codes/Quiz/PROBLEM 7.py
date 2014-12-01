def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    
    if n < 6:
        return False
    elif n%6 == 0 or n%9 == 0 or n%20 ==0:
        return True
    else:
        t = 0
        maxa = n/6 + 1
        maxb  = n/9 + 1
        maxc = n/10 + 1

        for a in range(maxa):
            if t == n:
                return True
    
            for b in range(maxb):
                if t == n:
                    return True

                for c in range(maxc):
                    t += a*20 + b*9 + c*6
    
                    if t == n:
                        return True
                    t = 0
        return False
    
    
    
def McNuggets(n):
    if n < 6:
        return False
    for i in [20, 9, 6]:
        if n == i or McNuggets(n - i):
            return True
    return False