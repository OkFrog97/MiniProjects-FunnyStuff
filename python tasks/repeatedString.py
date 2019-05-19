def repeatedString(s, n):
    a = s.count("a")
    answer = 0
    
    answer = a * (n//len(s))
    
    for i in range(n%len(s)):
        if s[i] == 'a':
            answer += 1
    
    return answer

def main ():
    print(repeatedString('abraca', 10))
    
if __name__ == "__main__":
    main()