from typing import Any, Optional


class ObjList:
    """Класс для представления элемента в двусвязном списке.

    Атрибуты:
        __data (Any): Данные, хранящиеся в узле.
        __prev (Optional[ObjList]): Ссылка на предыдущий узел в списке.
        __next (Optional[ObjList]): Ссылка на следующий узел в списке.
    """

    def __init__(self, data: Any = None) -> None:
        """Инициализирует узел с данными, а также предыдущим и следующим узлами, установленными в None."""
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self) -> Any:
        """Возвращает данные узла."""
        return self.__data

    @data.setter
    def data(self, value: Any) -> None:
        """Устанавливает данные узла."""
        self.__data = value

    @property
    def prev(self) -> Optional['ObjList']:
        """Возвращает предыдущий узел списка."""
        return self.__prev

    @prev.setter
    def prev(self, node: 'ObjList') -> None:
        """Устанавливает предыдущий узел списка."""
        self.__prev = node

    @property
    def next(self) -> Optional['ObjList']:
        """Возвращает следующий узел списка."""
        return self.__next

    @next.setter
    def next(self, node: 'ObjList') -> None:
        """Устанавливает следующий узел списка."""
        self.__next = node


class LinkedList:
    """Класс для представления двусвязного списка.

    Атрибуты:
        head (Optional[ObjList]): Начало списка.
        tail (Optional[ObjList]): Конец списка.
    """

    def __init__(self) -> None:
        """Инициализирует пустой двусвязный список."""
        self.head = None
        self.tail = None

    def add_obj(self, data: Any) -> None:
        """Добавляет новый объект в конец списка.

        Параметры:
            data (Any): Данные для добавления в список.
        """
        new_obj = ObjList(data)
        if self.head is None:
            self.head = new_obj
            self.tail = new_obj
        else:
            new_obj.prev = self.tail
            self.tail.next = new_obj
            self.tail = new_obj

    def remove_obj(self) -> None:
        """Удаляет последний объект из списка."""
        if self.tail is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None

    def get_data(self) -> list:
        """Собирает и возвращает список всех данных в элементах списка.

        Возвращает:
            list: Список данных всех элементов списка.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
