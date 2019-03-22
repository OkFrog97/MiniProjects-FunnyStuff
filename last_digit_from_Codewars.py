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
    return pow(n1, n2, 10)
    
if __name__ == '__main__':
    main()