def decode(dataset:str):
    '''
    decode genome_dataset from wordsNums_format to onlyWords_format.
    >decode(a3B4f2)
    >aaaBBBBff
    '''
    pass
    
    answer = ""
    
    for i in range(len(dataset)-1):
        if dataset[i].isalpha():
            answer += dataset[i]*int(dataset[i+1]
    
    return answer
    
    



genome = input()+' '
s = 0
n=genome[0]
for i in genome:       
    if n!=i:
        print(n + str(s), end = '')
        s=0
        n=i
    s+=1









def main():
    
    with open ("dataset_3363_2.txt") as data:
       dataset = data.readline()
    
    decoding_data = decode(dataset)
    
    
if __name__ == "__main__":
    main()