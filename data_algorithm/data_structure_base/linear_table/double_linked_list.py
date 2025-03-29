class DoubleLinkedNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self, node: DoubleLinkedNode = None):
        self.head = node
        self.length = 0 if self.head is None else 1

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.length

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    # 头插
    def add(self, data):
        current = self.head
        self.head = DoubleLinkedNode(data)
        self.length += 1
        if current is not None:
            self.head.next = current
            current.prev = self.head

    # 尾插
    def append(self, data):
        current = self.head
        self.length += 1
        if current is None:
            self.head = DoubleLinkedNode(data)
        else:
            while current.next is not None:
                current = current.next
            current.next = DoubleLinkedNode(data)
            current.next.prev = current

    def insert(self, insert_index, data):
        # 处理头部插入情况
        if insert_index <= 0:
            self.add(data)
        elif insert_index >= self.size():
            self.append(data)
        else:
            current = self.head
            index = 0
            while index < insert_index:
                current = current.next
                index += 1
            new_node = DoubleLinkedNode(data)

            new_node.next = current
            new_node.prev = current.prev
            new_node.prev.next = new_node
            new_node.next.prev = new_node
            self.length += 1

    def remove(self, data):
        if self.head is not None:
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
                    self.head.prev = None
                    # 其 next指向 和 被prev指向 操持不变，也没有 被next指向
                    self.length -= 1
            else:
                current_node = self.head
                while current_node is not None:
                    if current_node.data == data:
                        current_node.prev.next = current_node.next
                        current_node.next.prev = current_node.prev
                        self.length -= 1
                        break
                    else:
                        current_node = current_node.next

    def search(self, data):
        current_node = self.head
        for i in range(0, self.length):
            if current_node.data == data:
                return i
            current_node = current_node.next
        return -1

if __name__ == '__main__':
    linked_list = DoubleLinkedList()
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

    print('3' * 20)
    linked_list.insert(3, 5)
    linked_list.insert(40, 6)
    linked_list.traverse()
    linked_list.remove(5)
    linked_list.remove(6)
    linked_list.remove(60)
    linked_list.traverse()
    print(linked_list.search(5))

    print('&' * 20)
    linked_list_2 = DoubleLinkedList()
    linked_list_2.append(1)
    linked_list_2.remove(1)
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
