def last_digit(n1, n2):
    
    digits = [int(str(int(str(n1)[len(str(n1))-1])**i)[len(str(n1**i))-1]) for i in range (1, 5)]
    
    return digits[n2%len(set(digits))-1]