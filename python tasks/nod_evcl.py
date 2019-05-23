def evkl(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a>=b:
        return evkl(a%b,b)
    elif a<b:
        return evkl(a,b%a)