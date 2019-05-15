#This programm search prime number

while True:    
    print ('Программа определяет, является ли введенное число простым т.е. делится только на 1 и на само себя.')
    
    try:
        numb = int (input('Введите целое число '))
        tmp = True
        for i in range (2,numb):
                    if numb % i == 0:
                        print (numb, ' не является простым числом', 'и делится на', i)
                        tmp = False
                        break
        if tmp == True:
            print (numb, ' это простое число')
            
    except ValueError:
        print ('Вы ввели не целое число')

    input ()
