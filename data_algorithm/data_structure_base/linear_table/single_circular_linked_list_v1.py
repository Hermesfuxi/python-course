class SingleCircularLinkedNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleCircularLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def size(self):
        index = -1
        if self.head is not None:
            index += 1
            current = self.head
            while True:
                current = current.next
                # 若返回原点，则跳出循环
                if current == self.head:
                    break
                else:
                    index += 1
        return index + 1

    def traverse(self):
        current = self.head
        for i in range(0, self.length):
            print(current.data, end=' ')
            current = current.next
        print()

    # 头盖
    def add(self, data):
        new_node = SingleCircularLinkedNode(data)
        if self.is_empty():
            new_node.next = new_node  # 单节点循环
            self.head = new_node
            self.length += 1
        else:
            if self.length > 0:
                # 找到尾节点
                tail = self.head
                while tail.next != self.head:
                    tail = tail.next

                new_node = SingleCircularLinkedNode(data)
                tail.next = new_node
                new_node.next = self.head
                self.head = new_node
                self.length += 1

                # while True:
                #     current = current.next
                #     # 找列表最后一个元素
                #     if current.next == self.head:
                #         new_node = SingleCircularLinkedNode(data)
                #         new_node.next = self.head
                #         current.next = self.head = new_node
                #         self.length += 1
                #         break

    # 尾追
    def append(self, data):
        new_node = SingleCircularLinkedNode(data)
        if self.is_empty():
            new_node.next = new_node  # 单节点循环
            self.head = new_node
            self.length += 1
        else:
            if self.length > 0:
                # 找到尾节点
                tail = self.head
                while tail.next != self.head:
                    tail = tail.next

                new_node = SingleCircularLinkedNode(data)
                tail.next = new_node
                new_node.next = self.head
                self.length += 1

    def insert(self, insert_index, data):
        if insert_index <= 0 or self.is_empty():
            self.add(data)
            return
        elif insert_index >= self.length:
            self.append(data)
            return
        else:
            # 插入中间位置 [1, length-1]
            current = self.head
            index = 0
            while True:
                previous = current
                current = current.next
                index += 1
                if index == insert_index:
                    new_node = SingleCircularLinkedNode(data)
                    new_node.next = current
                    previous.next = new_node
                    self.length += 1
                    break

    def remove(self, data):
        # 当 列表为非空时,可删除元素
        if self.length > 1:
            current = self.head
            while True:
                # 删除非头元素
                previous = current
                current = current.next

                # 移除非头元素
                # 因之前，索引已经右移，所以要从第二个元素开始匹配
                if current.data == data:
                    previous.next = current.next
                    self.length -= 1
                    break

                # 找列表最后一个元素,结束循环,并判断是否移除头部元素
                if current.next == self.head:

                    # 移除头元素
                    if self.head.data == data:
                        self.head = self.head.next
                        # 更改最后元素的next
                        current.next = self.head
                        self.length -= 1
                    break
        elif self.length == 1 and self.head.data == data:
            self.head = None
            self.length = 0

    def search(self, data):
        # 查找数据的索引
        current = self.head
        for i in range(self.length):
            if current.data == data:
                return i
            current = current.next
        return -1


if __name__ == '__main__':
    linked_list = SingleCircularLinkedList()
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
    linked_list_2 = SingleCircularLinkedList()
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
