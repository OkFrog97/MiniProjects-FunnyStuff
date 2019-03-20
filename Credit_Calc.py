# RU:Программа расчета платежей по кредиту; EN: Program for calculation pay of credit;

# var

credit = float (input('Введите сумму кредита ')) # RU:Сумма кредита; EN: Amount of credit;
precent = float (input('Введите сумма процента годовых ')) # RU:Сумма процентов; EN: Interest credit;
time = float (input ('Введите срок кредита в годах ')) # RU:Срок кредита в годах; EN: Credit term;
print ()


month = time * 12 # yers to month;

x = credit / month # month credit;

y = (credit / 100 * precent) / 12 # month precent;

z = x + y # month pay;

print ('Ежемесячный платеж составляет ', round (z, 2), ';','\nИз которых сумма основного долга ', round (x, 2), ';','\nЕжемесячный платеж по процентам', round (y, 2), ';\n')
print ('Всего переплата составит ', y * month, ';\n')

input ()

# end
