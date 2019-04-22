def scramble(s1, s2):
    count = 0
    s1_list = [i for i in s1]
    for i in s2:
        if i in s1_list:
            count +=1
            s1_list.remove(i)
    if count == len(s2):
        return True
    else:
        return False

print (scramble('rkqodlw', 'world'), True)
print(scramble('cedewaraaossoqqyt', 'codewars'), True)
print (scramble('katas', 'steak'), False)
print(scramble('scriptjava', 'javascript'), True)
print(scramble('scriptingjava', 'javascript'), True)
