def decode(dataset:str):
    '''
    decode genome_dataset from wordsNums_format to onlyWords_format.
    >decode(a3B4f2)
    >aaaBBBBff
    '''
    answer = ""
    
    for i in range(len(dataset)-1):
        if dataset[i].isalpha():
            if dataset[i+1].isdigit() and dataset[i+2].isdigit():
                answer += dataset[i]*(int(dataset[i+1]+dataset[i+2]))
            else:
                answer += dataset[i]*int(dataset[i+1])
    
    return answer


def main():
    # open file with genome coding data
    with open ("dataset_3363_2.txt") as data:
       dataset = data.readline()
    
    #decoding
    decoding_data = decode(dataset)
    
    #write decoding data in file
    with open ("decode_data.txt", "w") as out:
        out.write(decoding_data)
    
    
if __name__ == "__main__":
    main()
