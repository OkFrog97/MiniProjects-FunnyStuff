def number(bus_stops):

    passangers = 0
    for i in range (len(bus_stops)):
        passangers += bus_stops[i][0]
        passangers -= bus_stops[i][1]
    return passangers


def test ():
    print (number([[10,0],[3,5],[5,8]]), '\nAnswer: 5')
    print (number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]), '\nAnswer: 17')
    print (number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]), '\nAnswer: 21')

test ()
input ()
