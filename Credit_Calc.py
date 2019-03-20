'''
RU:Программа расчета платежей по кредиту; EN: Program for calculation pay of credit;
'''

def Credit_Calc (credit, precent, time):
    month = time * 12 # yers to month;
    x = credit / month # month credit;
    y = (credit / 100 * precent) / 12 # month precent;
    z = x + y # month pay;
    overpall = z * month
    return z, x, y, overpall 

def main ():
    credit = float (input('Введите сумму кредита ')) # RU:Сумма кредита; EN: Amount of credit;
    precent = float (input('Введите сумма процента годовых ')) # RU:Сумма процентов; EN: Interest credit;
    time = float (input ('Введите срок кредита в годах ')) # RU:Срок кредита в годах; EN: Credit term;
    print('Ежемесячный платеж составляет {0};\nИз которых сумма основного долга {1};\nЕжемесячный платеж по процентам {2};\nВсего переплата составит {3}.'.format(Credit_Calc (credit, precent, time)))
    input()

if __name__ == '__main__':
    main()
