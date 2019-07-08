import sys
num_steps = int(sys.argv[1])
    
def stair(n):    
    for i in range (n):
		for j in range (n):
			if j+1 < n-i:
			    print (" ", end="")
			else:
			    print ("#", end="")
		print()

stair (num_step)

