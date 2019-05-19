def gap(g, m, n):
    '''
    find gap = g in lots of m and n.
    '''

    def isPrime(num):
        '''
        Chek m is prime.
        '''
        for i in range (2, num):
            if num%i == 0:
                return False
        return True
    
    while isPrime(m) == False: #find first prime number m
        m += 1
    
    siev = [True for i in range (0, n+1)]
    prime_nums = []
    
    for i in range(2, len(siev)): # Siev of Erathosthenes
        if siev[i] == True:
            for j in range (2*i, len(siev), i):
                siev[j] = False
    for l in range (m, n+1): # append prime numbers befor m and n
        if siev[l] == True:
            prime_nums.append(l)
    
    
    for k in range(len(prime_nums)-1): #Find our g
        if  (prime_nums[k+1]-prime_nums[k]) == g:
            return [prime_nums[k], prime_nums[k+1]]
   
    return None

def main ():
    
    print (gap(4,100,110),'\n*************\n')
    print (gap(2,100,110),'\n*************\n')
    print (gap(6,100,110),'\n*************\n')
    print (gap(8,300,400),'\n*************\n')
    print (gap(10,300,400),'\n*************\n')

if __name__ == '__main__':
    main ()