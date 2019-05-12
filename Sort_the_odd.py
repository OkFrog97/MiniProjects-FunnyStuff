'''
Sort the odd from codewars.com
'''

def sort_array(source_array):
    pass























def test ():
    print('{} must be True'.format(sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]))
    print ('{} must be True'.format(sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]))
    print ('{} must be True'.format(sort_array([7, 4, 2, 1, 3]) == [1, 3, 2, 4, 7]))
    print ('{} must be False'.format(sort_array([5, 3, 1, 8, 0]) == [5, 1, 3, 8, 0]))

def main():
    test()

if __name__ == "__main__":
    main()