def diamond (n):
   '''
   This cata must return diamond building by * with max weight n.
   >print (deamond (3))
   > *
   >***
   > *
   '''
    if n == 0:
        return None
    else:
        answer = ""
        for i in range (1,n+1,2):
	        answer += (" "*((n-i)//2) + i*'*' + " "*((n-i)//2)+'\n')
        for i in range (n-1,1,-2):
            answer += (" "*((n-i)//2) + i*'*' + " "*((n-i)//2)+'\n')