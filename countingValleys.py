'''
Task from hakkerrank.com
'''

def countingValleys(s): #missing n-argument!
    #WRONG!
    way = []
    seaLevel = 0
    Valleys = 0
    for i in s:
        if i == "U": #and seaLevel < 0?
            seaLevel+=1
            way.append(seaLevel)
        elif i == "D":
            seaLevel-=1
            way.append(seaLevel)
    
    return way











def tests():
    s1 = ["D","D","U","U","U","U","D","D"]
    s2 = ["U","D","D","D","U","D","U","U"]    
    print ('{} should be 2.'.format(countingValleys(s1)))
    print ('{} should be 1.'.format(countingValleys(s2)))

def main ():
    tests ()


if __name__ == "__main__":
    main()