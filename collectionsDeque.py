#1/usr/bin/evn python3

'''
Thisis programm is tasting Deque data structure from collections.
'''

def test_mode ():
    #import modules
    from collections import deque
    import time
   
    #add vars (deq and usual list
    test_list = []
    test_deq = deque()
   
    #list test
    print ("----list tests----")
    
    now = time.time()
    for i in range (1000000):
        test_list.append(i)
    then = time.time()
    print ("Time to append 1 000 000 numbers: {}".format(then-now))
    
    now = time.time()
    for i in range (100000):
        test_list.pop()
    then = time.time()
    print ("Time to delite 100 000 numbers from tail: {}".format(then-now))
    
    now = time.time()
    for i in range (100000):
        test_list.pop(0)
    then = time.time()
    print("Time to delite 100 000 number from top: {}".format(then-now))
    
    #deque test
    print("----deque tests----")
    now = time.time()
    for i in range (1000000):
        test_deq.append(i)
    then = time.time()
    print ("Time to append 1 000 000 numbers: {}".format(then-now))
    
    now = time.time()
    for i in range (100000):
        test_deq.pop()
    then = time.time()
    print ("Time to delite 100 000 numbers from tail: {}".format(then-now))
    
    now = time.time()
    for i in range (100000):
        test_deq.popleft()
    then = time.time()
    print("Time to delite 100 000 number from top: {}".format(then-now))


def main():
    test_mode()

if __name__ == "__main__":
    main ()