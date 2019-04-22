

def ask_number (question, low, hight, step = 1):
    response = None
    while response not in range (low, hight, step):
        response = int(input(question))
    return response
    

def main ():
    q = 'Ipnut number from 0 to 5 '
    print (ask_number (q, 0, 6, 2))
    input ()
main ()

