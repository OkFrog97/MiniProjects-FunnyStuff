'''
This programm is endless calendar.
It have 3 functions:
- dateformat for conver input string in three int vars: day, month and year.
- dateday for calculating the day of the week.
- test for checking input about correct date.
It is govnocode.
'''


#Programm functions.


def dateformat (user_input_str): #Testing passed.
    '''
    This function get date in sting and return date in integer numbers.
    '''
    user_input_str = user_input_str.lower() #String get low registr
    user_input_str = ''.join (i for i in user_input_str if i not in '.!@#$%^&*_+=?:%;№"- \\,/|') #Delete not digital and letter symbols.
    #Vars:
    day = None
    month = None
    year = None
    
    if user_input_str.isdigit(): # Only numbers converting.
        day = int(user_input_str[0] + user_input_str[1])
        month = int(user_input_str[2] + user_input_str[3])
        year = int(user_input_str[4]+user_input_str[5]+user_input_str[6]+user_input_str[7])
    
    elif user_input_str.isalnum(): # Numbers and chars converting.
        day = int(user_input_str[0] + user_input_str[1])
        user_input_str = user_input_str [2:len(user_input_str)] #Delete days in string.
        diction = {'январ':1,
                   'феврал':2,
                   'март':3,
                   'апрел':4,
                   'май':5,
                   'июн':6,
                   'июл':7,
                   'август':8,
                   'сентябр':9,
                   'октябр':10,
                   'ноябр':11,
                   'декабр':12}
        for i in diction: 
            if i in user_input_str:
                month = int(diction[i])
                break
        user_input_str = ''.join(k for k in user_input_str if k.isdigit()) #Delite char.
        year = int(user_input_str[0]+user_input_str[1]+user_input_str[2]+user_input_str[3]) 
    return day, month, year


def dateday (day, mon, year): #Testing passed.
    '''
    This function get date in int vars and return day of week.
    '''
    # day list
    days = ['Вс','Пн','Вт','Ср','Чт','Пт','Сб']
    # insaid variables
    var_a = (14 - int(mon)) // 12
    var_y = int(year) - var_a
    var_m = int(mon) + 12 * var_a - 2
    # Algorithm
    week_day = (int(day) + var_y + var_y // 4 - var_y // 100 + var_y // 400 + (31 * var_m) // 12) % 7
    return days[week_day]


def test (day, mon, year): #Testing passed.
    if not 0 < day <= 31 or not 0 < mon <=12 or not 1560 <= year: #Date validation check.
        return False
    elif (year % 4 == 0 or (year % 100 != 0 and year % 400 == 0)) and mon == 2 and day > 29: # Leap year check.
        return False
    elif (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)) and mon == 2 and day > 28: # Non-leap year check.
        return False
    else:
        return True


#Programm body

user_input = None

while user_input != 'выход':
    print ('\t\t\tПрограмма - вечный календарь.\n\nВозвращает день недели при вводе даты.\nВведите данные в порядке день-месяц-год в любом формате.\nНо не забудьте ноль перед числами первой десятки.\nКалендарь работает с 1560 года\n')
    user_input = input ('Введите дату или "выход": ')
    try:
        if user_input == 'выход':
            continue
        else:
            day, mon, year = dateformat(user_input)
            if test (day, mon, year) == False:
                print ('Вы ввели неверную дату. Возможно, такого числа месяца или месяца в году не существует. Проверьте себя.\n')
            else:
                print ('Дата {0} пришлась на день недели: {1}\n\n'.format (user_input, dateday(day, mon, year)))
    except Exception:
        print ('Похоже, вы где-то ошиблись. Попробуйте еще раз.\n')
    input ('\nНажмите Enter для продолжения.\n ')

input ('Нажмите Enter что-бы выйти. ')