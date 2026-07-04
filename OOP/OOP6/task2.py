# Взявши за основу код прикладу example_5.py, розширте функціональність класу MyList, додавши методи
# очищення списку, додавання елемента у довільне місце списку, видалення елемента з кінця та довільного
# місця списку.
class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        self._length = 0  # длина списка
        self._head = None  # первый элемент
        self._tail = None  # последний элемент

        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        node = MyList._ListNode(element)

        if self._tail is None:
            # список пустой
            self._head = self._tail = node
        else:
            # добавление в конец
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)

    # === НОВІ МЕТОДИ ===

    def clear(self):
        """Очистити список повністю"""
        self._head = None
        self._tail = None
        self._length = 0

    def insert(self, index, value):
        """Додати елемент у довільне місце (за індексом)"""

        if not 0 <= index <= self._length:
            raise IndexError('list index out of range')

        # вставка в кінець — те саме, що append
        if index == self._length:
            self.append(value)
            return

        # вставка на початок
        if index == 0:
            new_node = MyList._ListNode(value, prev=None, next=self._head)
            if self._head is not None:
                self._head.prev = new_node
            self._head = new_node
            if self._tail is None:
                self._tail = new_node
            self._length += 1
            return

        # загальний випадок: всередину списку
        current = self._head
        for _ in range(index):
            current = current.next

        # current — вузол, ПЕРЕД яким ми вставляємо
        prev_node = current.prev
        new_node = MyList._ListNode(value, prev=prev_node, next=current)

        if prev_node is not None:
            prev_node.next = new_node
        current.prev = new_node

        self._length += 1

    def pop(self):
        """Видалити елемент з кінця списку і повернути його значення"""

        if self._tail is None:
            raise IndexError('pop from empty MyList')

        value = self._tail.value

        # якщо один елемент
        if self._head is self._tail:
            self._head = self._tail = None
        else:
            new_tail = self._tail.prev
            new_tail.next = None
            self._tail = new_tail

        self._length -= 1
        return value

    def remove_at(self, index):
        """Видалити елемент за довільним індексом"""

        if not 0 <= index < self._length:
            raise IndexError('list index out of range')

        # видалення першого елемента
        if index == 0:
            value = self._head.value
            if self._head is self._tail:
                # один елемент
                self._head = self._tail = None
            else:
                self._head = self._head.next
                self._head.prev = None
            self._length -= 1
            return value

        # видалення останнього елемента
        if index == self._length - 1:
            return self.pop()

        # загальний випадок
        current = self._head
        for _ in range(index):
            current = current.next

        value = current.value

        prev_node = current.prev
        next_node = current.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self._length -= 1
        return value


def main():
    my_list = MyList([1, 2, 5])
    print("Початковий список:", my_list)

    # вставка за індексом
    my_list.insert(1, 100)  # [1, 100, 2, 5]
    print("Після insert(1, 100):", my_list)

    # видалення з кінця
    last = my_list.pop()  # видаляємо 5
    print("Після pop(), видалено:", last)
    print("Список зараз:", my_list)

    # видалення за індексом
    removed = my_list.remove_at(1)  # видаляємо 100
    print("Після remove_at(1), видалено:", removed)
    print("Список зараз:", my_list)

    # очищення
    my_list.clear()
    print("Після clear():", my_list, "довжина =", len(my_list))


if __name__ == '__main__':
    main()