def sum_of_intervals(intervals): #simple way
	numbers = []
	for interval in intervals:
		for i in range (interval[0], interval[1]):
			numbers.append(i)
	return len(set(numbers))

sum_of_intervals2 =lambda a:len(set.union(*(set(range(*i))for i in a))) #lambda hardway

    
def peresek_intervals (interval1, interval2): #Разбираемся с интервалвами и псевдокодом
    '''
    interval1 = [10, 11]
    interval2 = [7, 10]
    Непересечение:
    1 > 10 ЛИБО 5 < 7
    Т.е. либо А.начало(1) больше Б.конца(10),
    либо А.конец(5) меньше Б.начала(7)
    Пересечение:
    ЕСЛИ
    А.начало меньше либо равно Б.концу
    ИЛИ
    А.конец больше либо равне Б.началу
    ТО
    Пересекаются
    ИНАЧЕ
    Не пересекаются
    '''
    if interval1[0] <= interval2[1] and interval1[1] >= interval2[0]:
        return True
    else:
        return False
    
def union_intervals (interval1, interval2):
    
    unated_int = []
    if interval1[0] <= interval2[1] and interval1[1] >= interval2[0]:
        if interval1[0] <= interval2[0]:
            unated_int.append(interval1[0])
        else:
            unated_int.append(interval2[0])
        if interval1[1] >= interval2[1]:
            unated_int.append(interval1[1])
        else:
            unated_int.append(interval2[1])
    else:
        return False
    return unated_int

def Unated_tests():
    print ('Positive test, must return reseult:')
    print (union_intervals ([1,5], [4, 8]))
    print (union_intervals ([2,12], [9, 24]))
    print (union_intervals ([7,15], [1, 8]))
    print ('Negative tests, must return False:')
    print (union_intervals ([1,5], [6, 8]))
    print (union_intervals ([12,48], [4, 8]))
 
def main_test():
    print ('\t---MAIN FUNCTION TEST---\n')
    print ((sum_of_intervals([(1, 5)])), 'should be 4')
    print ((sum_of_intervals([(1, 5), (6, 10)])), 'should be 8')
    print ((sum_of_intervals([(1, 5), (1, 5)])), 'should be 4')
    print ((sum_of_intervals([(1, 4), (7, 10), (3, 5)])), 'should be 7')
    print ('\t***LAMBDA TESTS***\n')
    print ((sum_of_intervals2([(1, 5)])), 'should be 4')
    print ((sum_of_intervals2([(1, 5), (6, 10)])), 'should be 8')
    print ((sum_of_intervals2([(1, 5), (1, 5)])), 'should be 4')
    print ((sum_of_intervals2([(1, 4), (7, 10), (3, 5)])), 'should be 7')

def main():
    Unated_tests()
    main_test()
    input()

if __name__ == '__main__':
    main()
