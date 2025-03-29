class SingleCircularLinkedNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SingleCircularLinkedList:
    def __init__(self, node: SingleCircularLinkedNode = None):
        self.head = node

    def is_empty(self):
        return self.head is None

    def size(self):
        index = -1
        if not self.is_empty():
            index += 1
            current = self.head
            # 当列表为一个值时
            if current.next == current:
                index = 0
            else:
                # 当列表为多个值时，找到最后一个值的索引
                while current.next != self.head:
                    index += 1
                    current = current.next
        return index + 1

    def traverse(self):
        if not self.is_empty():
            current = self.head
            # 当列表为一个值时
            if current.next == current:
                print(current.data, end=' ')
            else:
                # 当列表为多个值时，找到最后一个值的索引
                while current.next != self.head:
                    print(current.data, end=' ')
                    current = current.next
                else:
                    print(current.data, end=' ')
        print()

    # 头盖
    def add(self, data):
        new_node = SingleCircularLinkedNode(data)
        # 当 列表为空时，初始化
        if self.is_empty():
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            # 当列表为一个值时，头部元素挤占
            if self.size() == 1:
                new_node.next = self.head
                current.next = self.head = new_node
            else:
                # 当列表为多个值时，头部元素挤占
                while current.next != self.head:
                    current = current.next
                else:
                    new_node.next = self.head
                    current.next = self.head = new_node

    # 尾追
    def append(self, data):
        new_node = SingleCircularLinkedNode(data)
        # 当 列表为空时，初始化
        if self.is_empty():
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            # 当列表为一个值时，尾部元素挤占
            if self.size() == 1:
                new_node.next = current
                current.next = new_node
            else:
                # 当指针指向最后一个元素，尾部元素挤占
                while current.next != self.head:
                    current = current.next
                else:
                    new_node.next = self.head
                    current.next = new_node

    def insert(self, insert_index, data):
        new_node = SingleCircularLinkedNode(data)
        # 当 列表为空时，初始化
        if self.is_empty():
            self.head = new_node
            self.head.next = self.head
        else:
            list_size = self.size()
            insert_index = insert_index % list_size

            # 处理头部插入情况
            if insert_index == 0:
                self.add(data)
            else:
                current = self.head
                index = 0
                # 指针停留在插入的元素前一位
                while index < insert_index-1:
                    index += 1
                    current = current.next
                else:
                    # 执行插入
                    new_node.next = current.next
                    current.next = new_node

    def remove(self, data):
        # 当 列表为非空时
        list_size = self.size()
        if list_size > 0:
            # 当列表为一个值时，尾部元素挤占
            if list_size == 1 and self.head.data == data:
                self.head = None
            elif list_size >= 2:
                current = self.head
                # 除去头部
                if self.head.data == data:
                    last = None
                    # 获取最后一个节点
                    while current.next != self.head:
                        current = current.next
                    else:
                        last = current
                    last.next = self.head = self.head.next
                else:
                    # 除去非头部元素
                    # 回到原点,则什么都
                    while current.next != self.head:
                        previous = current
                        current = current.next
                        if current.data == data:
                            previous.next = current.next
                            break
                    else:
                        previous = current
                        current = current.next
                        if current.data == data:
                            previous.next = current.next


    def search(self, data):
        data_index = index = -1
        # 当列表为空值时
        if not self.is_empty():
            index += 1
            # 当列表为一个值时
            current = self.head
            if current.next == current and self.head.data == data:
                data_index = 0
            else:
                # 当列表为多个值时(索引从0开始)，找到最后一个值的索引
                while current.next != self.head:
                    if current.data == data:
                        data_index = index
                    index += 1
                    current = current.next
                else:
                    if current.data == data:
                        data_index = index
        return data_index


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
    linked_list_2 = SingleCircularLinkedList()
    linked_list_2.append(1)
    linked_list_2.remove(1)
    print(linked_list_2.size())
    linked_list_2.append(2)
    linked_list_2.traverse()

    # linked_list_2.insert(0, 3)
    linked_list_2.insert(1, 20)
    linked_list_2.insert(2, 3)
    linked_list_2.insert(2, 30)
    linked_list_2.traverse()
