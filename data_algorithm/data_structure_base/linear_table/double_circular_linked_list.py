class DoubleCircularLinkedNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class DoubleCircularLinkedList:
    def __init__(self, node: DoubleCircularLinkedNode = None):
        self.head = node
        self.length = 0 if self.head is None else 1

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def traverse(self):
        current = self.head
        for i in range(0, self.length):
            print(current.data, end=' ')
            current = current.next
        print()

    # 头盖
    def add(self, data):
        new_node = DoubleCircularLinkedNode(data)
        # 当 列表为空时，初始化
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            current = self.head
            self.head = new_node
            new_node.next = current
            new_node.prev = current.prev
            new_node.next.prev = new_node
            new_node.prev.next = new_node
        self.length += 1

    # 尾追
    def append(self, data):
        # 当 列表为空时，初始化
        if self.is_empty():
            self.add(data)
        else:
            # 尾部节点
            current = self.head.prev
            new_node = DoubleCircularLinkedNode(data)
            new_node.prev = current
            new_node.next = self.head
            new_node.next.prev = new_node
            new_node.prev.next = new_node
            self.length += 1


    def insert(self, insert_index, data):
        if insert_index <= 0 or self.is_empty():
            self.add(data)
            return
        elif insert_index >= self.length:
            self.append(data)
            return
        else:

            current = self.head
            index = 0
            while index < insert_index:
                current = current.next
                index += 1
            new_node = DoubleCircularLinkedNode(data)
            new_node.next = current
            new_node.prev = current.prev
            new_node.next.prev = new_node
            new_node.prev.next = new_node
            self.length += 1


    def remove(self, data):
        if self.length > 0:
            # 处理头节点删除问题
            if self.head.data == data:
                # 只有一个头节点时，直接赋空
                if self.length == 1:
                    self.head = None
                    self.length = 0
                else:
                    # 有多个节点时，删除头节点，由第二节点担任头节点，并处理其前后指针：当前节点的前后指针、指向当前节点的指针
                    current_node = self.head
                    self.head = current_node.next
                    self.head.prev = current_node.prev
                    self.head.prev.next = self.head
                    self.length -= 1
                return
            # 处理非头节点删除问题
            else:
                current_node = self.head
                index = 0
                while index < self.length:
                    if current_node.data == data:
                        current_node.prev.next = current_node.next
                        current_node.next.prev = current_node.prev
                        return
                    current_node = current_node.next
                    index += 1

    def search(self, data):
        current_node = self.head
        for i in range(0, self.length):
            if current_node.data == data:
                return i
            current_node = current_node.next
        return -1


if __name__ == '__main__':
    linked_list = DoubleCircularLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(6)
    linked_list.append(7)
    linked_list.append(8)
    linked_list.append(9)
    linked_list.append(10)
    linked_list.traverse()
    print(linked_list.size())
    print('*' * 20)

    linked_list.add(0)
    linked_list.traverse()
    print(linked_list.size())
    print(linked_list.search(0))

    print('1' * 20)
    linked_list.append(12)
    print(linked_list.search(12))
    print(linked_list.search(6))
    linked_list.traverse()
    print(linked_list.size())

    print('2' * 20)
    linked_list.remove(0)
    linked_list.traverse()
    print(linked_list.search(0))
    linked_list.remove(10)
    linked_list.traverse()
    print(linked_list.search(10))

    print('3'*20)
    linked_list.insert(3, 5)
    linked_list.insert(40, 6)
    linked_list.traverse()
    linked_list.remove(5)
    linked_list.remove(6)
    linked_list.remove(60)
    linked_list.traverse()
    print(linked_list.search(5))

    print('&' * 20)
    linked_list_2 = DoubleCircularLinkedList()
    linked_list_2.append(1)
    linked_list_2.remove(1)
    linked_list_2.traverse()
    print(linked_list_2.size())
    linked_list_2.append(2)
    linked_list_2.traverse()

    linked_list_2.insert(0, 3)
    linked_list_2.traverse()
    linked_list_2.remove(3)
    linked_list_2.insert(1, 20)
    linked_list_2.insert(2, 3)
    linked_list_2.insert(2, 30)
    linked_list_2.traverse()
