class Node:
    def __init__(self, value = None, next_ = None) -> None:
        self.value = value
        self.next = next_
        
    def __str__(self) -> str:
        return 'Node value: '+ str(self.value)
        
class LinkedList:
    def __init__(self) -> None:
        self.first = None
        self.last = None
    
    def clear(self):
        self.__init__()
    
    def __str__(self) -> str:
        R = ''
        
        pointer = self.first
        while pointer is not None:
            R += str(pointer.value)
            pointer = pointer.next
            if pointer is not None:
                R += ' '

        return R
    
    def __iter__(self):  # объявляем класс как итератор
        self.current = self.first  # в текущий элемент помещаем первый
        return self  # возвращаем итератор

    def __next__(self):  # метод перехода
        if self.current is None:  # если текущий стал последним
            raise StopIteration  # вызываем исключение
        else:
            node = self.current  # сохраняем текущий элемент
            self.current = self.current.next  # совершаем переход
            return node  # и возвращаем сохраненный
        
    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count
    
    def pushleft(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node
    
    
    def pushright(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node    
            self.last = new_node
        
    
            
    def popleft(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return node  # возвращаем сохраненный
        
        
    def popright(self): 
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last: #  если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node #  и возвращаем сохраненный элемент
        else:
            node = self.last  # сохраняем последний
            pointer = self.first  # создаем указатель
            while pointer.next is not node:  # пока не найдем предпоследний
                pointer = pointer.next
            pointer.next = None  # обнуляем указатели, чтобы
            self.last = pointer  # предпоследний стал последним
            return node  # возвращаем сохраненный
LL = LinkedList()

LL.pushright(1)
LL.pushleft(2)
LL.pushright(3)
LL.popright()
LL.pushleft(4)
LL.pushright(5)
LL.popleft()

print(LL)