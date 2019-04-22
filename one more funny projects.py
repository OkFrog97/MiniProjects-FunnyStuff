def primeFactors(n):

    def prime_factor_decomp (num):
        i = 2
        primfac = []
        while i * i <= num:
            while num % i == 0:
                primfac.append(int(i))
                num = num / i
            i = i + 1
        if num > 1:
            primfac.append(int(num))
        return primfac
    
    def make_answer (prime_list):
        answer = ''
        non_rep_nums = list(set(prime_list))
        non_rep_nums.sort()
        for i in non_rep_nums:
            if 1 < prime_list.count(i):
                answer += '({0}**{1})'.format(i, prime_list.count(i))
            else:
                answer += '({0})'.format(i)
        return answer
    return make_answer(prime_factor_decomp(n))

print ('---test # 1---')
print ('(7)(5113051)')
print (primeFactors(35791357))
print ('---test # 2---')
print ('(3)(17**2)(31)(677)')
print (primeFactors(18195729))

input()
 
