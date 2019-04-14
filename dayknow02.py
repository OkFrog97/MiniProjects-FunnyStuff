#Programm functions


def dateformat (strng): #Testing True
    '''
    This function get date in sting and return date in integer numbers.
    '''
    strng = strng.lower() #String get low registr
    strng = ''.join (i for i in strng if i not in '.!@#$%^&*_+=?:%;№"- \\,/|') #Delit not digital and letter symbols.
    #Vars:
    day = None
    month = None
    year = None
    
    if strng.isdigit():
        day = int(strng[0] + strng[1])
        month = int(strng[2] + strng[3])
        year = int(strng[4]+strng[5]+strng[6]+strng[7])
    
    elif strng.isalnum():
        day = int(strng[0] + strng[1])
        strng = strng [2:len(strng)]
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
            if i in strng:
                month = int(diction[i])
                break
        strng = ''.join(k for k in strng if k.isdigit())
        year = int(strng[0]+strng[1]+strng[2]+strng[3])
    return day, month, year


def dateday (day, mon, year): #Testing True
    '''
    This function get date and return day of week.
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


def test (day, mon, year):
    if not 0 < day <= 31 or not 0 < mon <= 12 or not 1560 < year:
        return False
    else:
        return True


#Programm body

user_input = None

while user_input != 'выход':
    print ('\tПрограмма - вечный календарь.\nВозвращает день недели при вводе даты.\nВведите данные в порядке день-месяц-год в любом формате.\nНо не забудьте ноль перед числами первой десятки.\nКалендарь работает с 1560 года\n')
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