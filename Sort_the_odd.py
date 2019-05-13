'''
Sort the odd from codewars.com
'''

def sort_array(source_array):

    odd_indexes = []
    
    for i in range(len(source_array)):
        if source_array[i]%2==1:
            odd_indexes.append(i)
    
    
    N = len (odd_indexes)
    for bypass in odd_indexes:
        for k in odd_indexes[:len(odd_indexes)-1]:
            if source_array[k] > source_array [k+1]:
               source_array[k], source_array[k+1] = source_array[k+1], source_array[k]

    return source_array
















def test ():
    print('{} must be True'.format(sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]))
    print ('{} must be True'.format(sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]))
    print ('{} must be True'.format(sort_array([7, 4, 2, 1, 3]) == [1, 3, 2, 4, 7]))
    print ('{} must be False'.format(sort_array([5, 3, 1, 8, 0]) == [5, 1, 3, 8, 0]))

def main():
    test()

if __name__ == "__main__":
    main()