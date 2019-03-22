def last_digit(n1, n2):
   '''
    Task from codewars.
    n1 is a number. n2 is elevating number.
    Return last digit of elevating.
    >last_digit (2, 3) # 2**3=8;
    >8
    >last_digit (5, 3) # 5**3=125;
    >5
    '''
    if n2 == 0:
        return 1
    elif int(str(n1)[len(str(n1))-1]) in [0,1,5]: #if last n1 digit in list return it cose answer is not change.
        return int(str(n1)[len(str(n1))-1])
    else:
        return int(str(n1**(n2%4))[len(str(n1**(n2%4)))-1]) #Remainder of division is elevating number for n1 (or last n1 digital) which can show last n1**n2 digital.