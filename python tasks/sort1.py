deth = [15,13,0,11,7,22,5,8,33]
for i in range (len(deth)):
    for k in range (0, len(deth)):
        if deth[k+1]<len(deth) and deth [k] > deth [k+1]:
    	    deth[k], deth[k+1] = deth [k+1], deth[k]
print (deth)

input ()
