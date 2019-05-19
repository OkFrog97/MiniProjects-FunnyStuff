'''
Sort the odd from codewars.com
'''

def sort_array(source_array):

    for i in range (len(source_array)):
        for j in range (i, len(source_array)): #i is start of iteration for minimal operations
            if source_array[i]%2==1 and source_array[j]%2==1 and source_array[j] < source_array[i]: #RUS: Если элемент из итерации i и элемент из итерации j - нечетные, а так же, если элемент из итерации j больше (j так как в этой итерации просматривабтся все элементы от i и до конца списка), поменять местами i и j
                source_array[i], source_array[j] = source_array[j], source_array[i]
    return source_array

def test ():
    print ('____TEST SORT ARRAY____')
    print('{} must be True'.format(sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]))
    print ('{} must be True'.format(sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]))
    print ('{} must be True'.format(sort_array([7, 4, 2, 1, 3]) == [1, 4, 2, 3, 7]))
    print ('{} must be False'.format(sort_array([5, 3, 1, 8, 0]) == [5, 1, 3, 8, 0]))

def main():
    test()

if __name__ == "__main__":
    main()