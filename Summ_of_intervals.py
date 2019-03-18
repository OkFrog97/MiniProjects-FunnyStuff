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