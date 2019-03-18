def sum_of_intervals(intervals):
    '''
    This function accepts an array of intervals, 
    and returns the sum of all the interval lengths.
    Overlapping intervals should only be counted once.
    '''
    answer = 0
    for i in intervals:
        answer += (i[1] - i[0])

    return answer