def diamond (n):
   '''
   This cata must return diamond building by * with max weight n.
   >print (deamond (3))
   > *
   >***
   > *
   '''
    if n <= 2:
        return None
    else:
        answer = ""
        for i in range (1,n+1,2):
	        answer += (" "*((n-i)//2) + i*'*' + '\n')
        
        for i in range (n-2,0,-2):
            answer += (" "*((n-i)//2) + i*'*'+'\n')
        
        return answer
     
     
 diamond2 = lambda n: None if n <= 2 else ''.join([(" "*((n-i)//2) + i*'*' + '\n') for i in range (1,n+2,2)]+[(" "*((n-i)//2) + i*'*'+'\n') for i in range (n-2,0,-2)])