import sys, inspect, weakref, copy


def get_classes():
    classes = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            classes.append(obj)
    return classes


def all_names():
    for i in Thing._all:
        name = 'Name: {}    id: {}    Type:{}'.format(i.name, i.id, i.type)
        yield name


def to_object(dic):
    if isinstance(dic, dict):
        x = [i() for i in get_classes() if i.__name__ == dic['type']]
        if x: obj = x[0]
        else: return
        obj.name = dic['name']
        obj.id = dic['id']
        obj.multiplicity = dic['multiplicity']
        if 'parent' in dic.keys() and dic['parent']:
            x = [i for i in Thing._all if i.id == dic['parent']]
            if x: obj.parent = x[0]
        if dic['children']:
            temp = []
            for d in dic['children']:
                if isinstance(d, str):
                    temp.append(d)
                else:
                    temp.append(Thing.to_object(d))
            obj._children = temp
        if hasattr(obj, 'value') and 'value' in dic:
            obj._value = dic['value']
        return obj


class Thing:
    _count = 0
    _all = []

    def __init__(self, name=None, multiplicity=None, parent=None):
        self._type = self.__class__.__name__
        if parent:
            self._parent = weakref.ref(parent)
            self.parent.add_child(self)
        else:
            self._parent = None
        self._children = []
        if multiplicity is not None:
            self._multiplicity = str(multiplicity)
        else:
            self._multiplicity = str(1)   # set default multiplicity to 1
        if name:
            if self.parent:
                try:
                    self._name = name
                    self._fullname = self.parent.fullname + '.' + name
                    if len([ i for i in self.parent.children if i.name==name]) > 1:
                        raise Exception('Name already exists in present context, rename model element')
                except Exception as e:
                    return repr(e)
            else:
                self._name = name
                self._fullname = name
        else:
            self._name = self._type + str(self.__class__._count)
            self._fullname = (self.parent.fullname+'.'+self._name) if self.parent else self._name
        Thing._count += 1
        Thing._all.append(self)

    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()

    @parent.setter
    def parent(self, thing):
        self._parent = weakref.ref(thing)
        thing.add_child(self)

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def multiplicity(self):
        return self._multiplicity

    @multiplicity.setter
    def multiplicity(self, mult):
        self._multiplicity = mult

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, nom):
        self._name = nom

    @property
    def fullname(self):
        return self._fullname

    def add_child(self, *items):
        for i in items:
            self._children.append(i)

    def to_dict(self):
        return {"name": self._name, "parent": self.parent.fullname if self._parent else None, "type": self._type,
                "multiplicity": self._multiplicity, "fullname": self._fullname}


class ModelElement(Thing):
    _all = []
    _count = 0

    def __init__(self, name=None, multiplicity=None, parent=None):
        super().__init__(name, multiplicity, parent)
        ModelElement._count += 1
        ModelElement._all.append(self)

    def to_dict(self):
        dic = super().to_dict()
        return {**dic, "children": [p.to_dict() for p in self._children] if self._children else []}


class Property(Thing):
    _count = 0
    _all = []

    def __init__(self, name=None, multiplicity=None, parent=None):
        if multiplicity is None:
            multiplicity = '*'
        super().__init__(name, multiplicity, parent)
        Property._count += 1
        Property._all.append(self)

    def to_dict(self):
        dic = super().to_dict()
        return {**dic, "children": [m.to_dict() for m in self._children] if self._children else []}


class Containment(Property):
    _count = 0
    _all = []

    def __init__(self, name=None, multiplicity=None, parent=None):
        super().__init__(name, multiplicity, parent)
        Containment._count += 1
        Containment._all.append(self)


class Dependency(Property):
    _count = 0
    _all = []

    def __init__(self, name=None, multiplicity=None, parent=None):
        super().__init__(name, multiplicity, parent)
        Dependency._count += 1
        Dependency._all.append(self)


class Importation(Dependency):
    _count = 0
    _all = []

    def __init__(self, name=None, multiplicity=None, parent=None):
        super().__init__(name, multiplicity, parent)
        Importation._count += 1
        Importation._all.append(self)


class Package(ModelElement):
    _all = []
    _count = 0

    def __init__(self, name=None, multiplicity=None, parent=None):
        super().__init__(name, multiplicity, parent)
        self._contents = Containment(name='contains', parent=self)
        self._imports = Importation(name='imports', parent=self)
        self._children.extend([self._imports, self._contents])
        Package._count += 1
        Package._all.append(self)

    def add_content(self, *items):
        for i in items:
            try:
                i.parent = self
                self._contents.add_child(i)
            except Exception as e:
                return repr(e)

    def add_import(self, *pac):  # names in namespace pac may be used without fullname
        for i in pac:
            self._contents.add_child(copy.copy(i))  # TODO check side effects of deep/shallow copy

    def names(self):   # return names in this namespace
        names = []
        for i in self._contents:
            names.append(i.name)
        for pac in self._imports:
            names.extend(pac.names())
        return names










x = ModelElement()
y = Property(parent=x)
z = ModelElement(parent=y)

print( y.to_dict())
print(x.to_dict())
print(z.to_dict())


