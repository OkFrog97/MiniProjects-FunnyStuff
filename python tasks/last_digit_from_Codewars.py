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
    last_digit = [int(str(int(str(n1)[-1])**i)[-1]) for i in range (1,5)]
    return 1 if n2 ==0 else last_digit[(n2%4)-1]

    
if __name__ == '__main__':
    main()