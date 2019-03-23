def data_reverse(data):
    '''
    This program revers 4-bits data.
    '''
    answ = []
    for i in range (len(data)-1,0,-4):
	    for i in range (i-3,i+1):
		    answ.append (data[i])
    return answ

def tests():
    pass

def main():
    pass

if __name__ == '__main__':
    main()