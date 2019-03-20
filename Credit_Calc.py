'''
RU:Программа расчета платежей по кредиту; EN: Program for calculation pay of credit;
'''

def Credit_Calc (credit, precent, time):
    month = round ((time * 12), 2) # yers to month;
    x = round ((credit / month), 2) # month credit;
    y = round (((credit / 100 * precent) / 12), 2) # month precent;
    z = round ((x + y), 2) # month pay;
    overpall = y * month
    return z, x, y, overpall 

def main ():
    try:
        credit = float (input('Введите сумму кредита ')) # RU:Сумма кредита; EN: Amount of credit;
        precent = float (input('Введите сумма процента годовых ')) # RU:Сумма процентов; EN: Interest credit;
        time = float (input ('Введите срок кредита в годах ')) # RU:Срок кредита в годах; EN: Credit term;
        day_pay, main_sum, proc_sum, bank_sum  = Credit_Calc (credit, precent, time)
        print('Ежемесячный платеж составляет {0};\nИз которых сумма основного долга {1};\nЕжемесячный платеж по процентам {2};\nВсего переплата составит {3}.'.format(day_pay, main_sum, proc_sum, bank_sum))
        input()

    except ValueError:
        print ('Вы ввели не число.')
        input()

if __name__ == '__main__':
    main()
