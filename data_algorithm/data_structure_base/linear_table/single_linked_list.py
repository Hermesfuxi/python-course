class SingleLinkedNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self, node: SingleLinkedNode = None):
        self.head = node

    def is_empty(self):
        return self.head is None

    def size(self):
        index = -1
        if self.head is not None:
            index += 1
            current = self.head
            while current.next is not None:
                index += 1
                current = current.next
        return index + 1

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

    def add(self, data):
        current = self.head
        self.head = SingleLinkedNode(data)
        self.head.next = current

    def append(self, data):
        current = self.head
        if current is None:
            self.head = SingleLinkedNode(data)
        else:
            while current.next is not None:
                current = current.next
            else:
                current.next = SingleLinkedNode(data)

    def insert(self, insert_index, data):
        # 处理头部插入情况
        if insert_index <= 0:
            insert_index = 0

        # 当前指针
        index = -1
        current_node = SingleLinkedNode()
        current_node.next = self.head
        while current_node.next is not None:
            index += 1
            previous_node = current_node
            current_node = current_node.next
            if index == insert_index:
                previous_node.next = SingleLinkedNode(data)
                previous_node.next.next = current_node
                if insert_index == 0:
                    self.head = previous_node.next
                break
        else:
            # 处理尾部插入情况
            if index < insert_index:
                current_node.next = SingleLinkedNode(data)


    def remove(self, data):
        if self.head is not None:
            if self.head.data == data:
                self.head = self.head.next
                return
            else:
                current_node = self.head
                previous_node = SingleLinkedNode(0)
                while current_node.next is not None:
                    if current_node.data == data:
                        previous_node.next = current_node.next
                        break
                    else:
                        previous_node = current_node
                        current_node = current_node.next

    def search(self, data):
        flag = False
        current_node = self.head
        if current_node is not None and current_node.data == data:
            flag = True
        else:
            while current_node is not None:
                if current_node.data == data:
                    flag = True
                current_node = current_node.next
        return flag


if __name__ == '__main__':
    linked_list = SingleLinkedList()
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
    linked_list.remove(5)
    linked_list.remove(6)
    linked_list.remove(60)
    linked_list.traverse()
    print(linked_list.search(5))

    print('&' * 20)
    linked_list_2 = SingleLinkedList()
    linked_list_2.append(1)
    linked_list_2.remove(1)
    print(linked_list_2.size())
    linked_list_2.append(2)
    linked_list_2.traverse()
    print('=' * 20)
    linked_list_2.insert(0, 3)
    linked_list_2.traverse()
    linked_list_2.remove(3)

    linked_list_2.insert(1, 20)
    linked_list_2.insert(2, 3)
    linked_list_2.insert(2, 30)
    linked_list_2.traverse()
