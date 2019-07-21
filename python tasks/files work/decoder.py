def decode(dataset:str):
    '''
    decode dataset from wordsnums to only words format.
    >decode(a3B4f2)
    >aaaBBBBff
    '''
    pass














def main():
    
    with open ("dataset_3363_2.txt") as data:
       dataset = data.readline()
    
    print(type(dataset))
    
    decoding_data = decode(dataset)
    
    
if __name__ == "__main__":
    main()