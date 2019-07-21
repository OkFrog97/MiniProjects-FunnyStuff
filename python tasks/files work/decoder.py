def decode(dataset:str):
    '''
    decode genome_dataset from wordsNums_format to onlyWords_format.
    >decode(a3B4f2)
    >aaaBBBBff
    '''
    return "".join(dataset[i]*int(dataset[i+1]) for i in range(len(dataset)-1) if dataset[i].isalpha())


def main():
    
    with open ("dataset_3363_2.txt") as data:
       dataset = data.readline()
    
    decoding_data = decode(dataset)
    
    print(decoding_data)
    
if __name__ == "__main__":
    main()