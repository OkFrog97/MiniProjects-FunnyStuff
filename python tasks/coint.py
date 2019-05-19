'''
This programm testing Probability thery with help of coint.
Without pussyes.
v. 0.1 programm was writeng;
v. 0.2 tabs/space error fix;
v. 0.3 plus test
v. 0.4 test found summ of 
'''

import random

def coint_stat (count_stop): # Coint flip statistik function; just new commit
    count = 0
    coint_orel = 0
    coint_reshka = 0
    while count < count_stop:
        coint = random.randrange(2) # Flip
        if coint == 0:
            coint_orel += 1
        elif coint == 1:
            coint_reshka += 1
        else:
            print ('Unknown error')
        count += 1
    return coint_orel, coint_reshka

for i in range (10):
    reshka = 0
    orel = 0
    ravno = 0
    i = 0
    while i < 100: #testing
        coint_orel, coint_reshka = coint_stat (10000)
        if coint_orel > coint_reshka:
            orel += 1
        elif coint_orel < coint_reshka:
            reshka += 1
        elif coint_orel == coint_reshka:
            ravno += 1
        i += 1
    print ('Преобладание орлов на количество итераций: '+str(orel) + '\n'+ 'Преобладание решек на количество итераций: ' +str(reshka) +'\n' + 'Преобладание равно на количество итераций: ' + str(ravno))


input()
