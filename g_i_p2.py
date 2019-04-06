def gap(g, m, n):
    '''
    find gap = g in lots of m and n.
    More effective way.
    '''
    prime_nums=[2]
    for i in range(3, n+1, 2):
	    if (i > 10) and (i%10==5):
		    continue
	    for j in prime_nums:
		    if j*j-1 > i:
			    prime_nums.append(i)
			    break
		    if (i % j == 0):
			    break
	    else:
		    prime_nums.append(i)

    for k in range(m, len(prime_nums)-1): #Find our g
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
