class RandomIterator:
    def __next__(self):
        return 0

def main ():
    x = RandomIterator()
    print(next(x))

if __name__ == "__main__":
    main()
