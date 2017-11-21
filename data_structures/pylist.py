
class PyList:
    def __init__(self, contents=[], size=10):
        self.items = [None] * size
        self.numItems = 0
        self.size = size
        for e in contents:
            self.append(e)

    def append(self, item):
        if self.numItems == len(self.items):
            newlst = [None] * self.numItems * 2
            for k in range(len(self.items)):
                newlst[k] = self.items[k]
            self.items = newlst

        self.items[self.numItems] = item
        self.numItems += 1

    def __makeroom(self):
        newlen = (self.size // 4) + self.size + 1
        newlst = [None] * newlen
        for i in range(self.numItems):
            newlst[i] = self.items[i]

        self.items = newlst
        self.size = newlen

    def __getitem__(self, index):
        if index >= 0 and index < self.numItems:
            return self.items[index]
        raise IndexError('PyList index out of range')

    def __setitem__(self, index, val):
        if index >= 0 and index < self.numItems:
            self.items[index] = val
            return
        raise IndexError('PyList assignment index out of range ')

    def __add__(self, other):
        result =  PyList(size=self.numItems + other.numItems)
        for i in range(self.numItems):
            result.append(self.items[i])
        for i in range(other.numItems):
            result.append(other.items[i])
        return result

    def insert(self, i, e):
        if self.numItems == self.size:
            self.__makeroom()

        if i < self.numItems:
            for j in range(self.numItems-1, i-1, -1):
                self.items[j+1] = self.items[j]
                self.items[i] = e
                self.numItems += 1
        else:
            self.append(e)

    def __delitem__(self, index):
        for i in range(index, self.numItems-1):
            self.items[i] = self.items[i+1]
        self.numItems -= 1

    def __eq__(self, other):
        if type(other) != type(self):
            return False

        if self.numItems != other.numItems:
            return False
        for i in range(self.numItems):
            if self.items[i] != other.items[i]:
                return False
        return True

    def __iter__(self):
        for i in range(self.numItems):
            yield self.items[i]

    def __len__(self):
        return self.numItems

    def __contains(self, item):
        for i in range(self.numItems):
            if self.items[i] == item:
                return True
        return False

    def __str__(self):
        s = '['
        for i in range(self.numItems):
            s = s + repr(self.items[i])
            if i < self.numItems -1:
                s = s + ', '
        s = s + ']'
        return s

    def __repr__(self):
        s = "PyList(["
        for i in range(self.numItems):
            s = s + repr(self.items[i])
            if i < self.numItems - 1:
                s = s + ','
        s = s + "])"
        return s

x = PyList([1,2,3])
y = PyList(x)  # shallow copy of x
z = eval(repr(x))  # deep copy of x
print(str(z), repr(z))


