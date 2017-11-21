
class CapitalIterable:
    def __init__(self, string):
         self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)

class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self



def main():
    iterable = CapitalIterable("Night gathers and now my watch begins.")
    iterator = iter(iterable)

    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break
    for i in iterable:
        print("\n",i)

if __name__ == "__main__":
    main()




        
