from random import random

class RandomIterator:
    def __init__(self,k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

def main ():
    x = RandomIterator(3)
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))

if __name__ == "__main__":
    main()
