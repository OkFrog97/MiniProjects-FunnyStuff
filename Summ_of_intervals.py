def sum_of_intervals(intervals):
    '''
    This function accepts an array of intervals, 
    and returns the sum of all the interval lengths.
    Overlapping intervals should only be counted once.
    '''
    answer = []
    
    for i in set(intervals):
        answer.append(i[1] - i[0])

    return sum(answer)
    
    #Разбираемся с интервалвами и псевдокодом

def peresek_intervals (interval1, interval2):
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
 
def main():
    Unated_tests()
    input()

if __name__ == '__main__':
    main()
    
