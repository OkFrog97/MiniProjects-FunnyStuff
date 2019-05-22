def fib_mod (n, m):
    count = 0
	f=[0,1]
	for i in range (2,n+1):
		temp = (f[i-1]+f[i-2])%m
		f.append(temp)
	    count ++ 1
        if f[i] == 1 and f[i-1] ==0:
            break
    return f[n%count]