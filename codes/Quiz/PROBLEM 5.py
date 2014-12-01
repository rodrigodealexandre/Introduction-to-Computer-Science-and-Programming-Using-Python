def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    x = ''
    if len(s1) > 0 and len(s2) == 0:
        return s1
    elif len(s1) == 0 and len(s2) > 0:
        return s2
    elif len(s1) == 0 and len(s2) == 0:
        return ""
    elif len(s1) == len(s2):
        for n in range(len(s1)):
            x += s1[n] + s2[n]
        return x
    elif len(s1) < len(s2):
        for n in range(len(s1)):
            x += s1[n] + s2[n]
        z = len(s2) - len(s1)
        x += s2[len(s2)-z:]
        return x
    elif len(s1) > len(s2):
        for n in range(len(s2)):
            x += s1[n] + s2[n]
        z = len(s1) - len(s2)
        x += s1[len(s1)-z:]
        return x