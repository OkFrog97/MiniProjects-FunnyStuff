def primes (x):
    
    def is_prime(n):
        d = 2
        while n%d != 0:
            d +=1
        return d == n
    
    for num in range(0,x+1):
        if is_prime(num):
             yield num

print(list(primes(31)))
print([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])             
