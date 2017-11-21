import math
class FirstClass:
    "First class I ever created in python sweet!!!"
    pass

class Point:
    "Represents a point in 2d cartesian geometry"
    def __init__(self, x=0, y=0):
        """Initializes a point as input x and y arguments. If no initial arguments
        are given point is initialized as origin"""
        self.move(x, y)
        
    def move(self, x, y):
        "Changes point to the new x,y location given "
        self.x = x
        self.y = y
    
    def reset(self):
        "Resets point's x,y location to the origin i.e. 0,0 "
        self.move(0,0)

    def calc_distance(self, point):
        """calculates distance between point and point given as argument
        using pythagoras theorem. Returns floating point number: distance"""
        return math.sqrt(
            ((self.x - point.x)**2) +
                         ((self.y - point.y)**2))
        
def format_string(string, formatter=None):
    '''Demos nested class. defines a function with nested
    Default formatter class that defines a format method'''
    class DefaultFormatter:
        def format(self, string):
            return str(string).title()

    if not formatter:
            formatter = DefaultFormatter()
    return formatter.format(string)

class  ContactList(list):
    ''' Demos inheritance and extending python in built classes'''
    def search(self, name):
        match = []
        for contact in self:
            if name in contact.name:
                match.append(contact)
        return match
    
class Contact:
    ''' Demos static attributes & composition''' 
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print("Send "
              "'{}'order to'{}'".format(order, self.name))
























