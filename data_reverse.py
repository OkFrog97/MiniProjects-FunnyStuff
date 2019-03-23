def data_reverse(data):
    '''
    This program revers 4-bits data.
    '''
    answ = []
    for i in range (len(data)-1,0,-4):
	    for j in range (i-3,i+1):
		    answ.append (data[j])
    return answ

def tests():
    data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
    data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
    print (data_reverse(data1)==data2)

def main():
    tests()

if __name__ == '__main__':
    main()