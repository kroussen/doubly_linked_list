class ObjList:
    def __init__(self, data=None):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, node):
        self.__prev = node

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, data):

        new_obj = ObjList(data)

        if self.head is None:
            self.head = new_obj
            self.tail = new_obj
        else:
            new_obj.prev = self.tail
            self.tail.next = new_obj
            self.tail = new_obj

    def remove_obj(self):
        if self.tail is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None

    def get_data(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
