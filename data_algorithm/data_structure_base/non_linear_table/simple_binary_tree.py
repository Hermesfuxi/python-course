import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self, root: BinaryTreeNode = None):
        self.root = root

    def insert(self, data):
        node = BinaryTreeNode(data)

    def insert_left(self, data):
        node = BinaryTreeNode(data)

    def insert_right(self, data):
        node = BinaryTreeNode(data)

    # 定义add函数，表示添加节点
    def add(self, data):
        new_node = BinaryTreeNode(data)
        # 判断根节点是否为空
        if self.root is None:
            self.root = new_node
            return
        tree_node_queue = queue.Queue()
        tree_node_queue.put(self.root)
        while True:
            tree_node = tree_node_queue.get()
            if tree_node.left_child is None:
                tree_node.left_child = new_node
                break
            else:
                tree_node_queue.put(tree_node.left_child)

            if tree_node.right_child is None:
                tree_node.right_child = new_node
                break
            else:
                tree_node_queue.put(tree_node.right_child)

    # 遍历二叉树：广度优先遍历，（逐层遍历，一层一层的遍历）
    def breadth(self):
        print(f'{'——' * 3} 广度优先遍历 {'——' * 3} ')
        # 判断根节点是否为空
        if self.root is None:
            return

        tree_node_queue = queue.Queue()
        tree_node_queue.put(self.root)
        print(self.root.data, end=' ')
        while not tree_node_queue.empty():
            tree_node = tree_node_queue.get()
            if tree_node.left_child is not None:
                tree_node_queue.put(tree_node.left_child)
                print(tree_node.left_child.data, end=' ')

            if tree_node.right_child is not None:
                tree_node_queue.put(tree_node.right_child)
                print(tree_node.right_child.data, end=' ')
        print()

    # 深度优先之先序遍历（根左右）
    def preorder(self):
        print(f'{'——' * 3} 先序遍历（根左右） {'——' * 3} ')
        def depthTraversal(node):
            if node is None:
                return
            print(node.data, end=' ')
            depthTraversal(node.left_child)
            depthTraversal(node.right_child)
        depthTraversal(self.root)
        print()

    # 深度优先之中序遍历（左根右）
    def inorder(self):
        print(f'{'——' * 3} 中序遍历（左根右） {'——' * 3} ')

        def depthTraversal(node):
            if node is None:
                return
            depthTraversal(node.left_child)
            print(node.data, end=' ')
            depthTraversal(node.right_child)

        depthTraversal(self.root)
        print()

            #   2.1 找到左的上级中，再找到中的右节点，
            #   2.2 将右节点视为新的根节点，再左中右递归

            # print(tree_node.data, end=' ')
            # if tree_node.left_child is not None:
            #     tree_node_queue.put(tree_node.left_child)
            #     continue
            # elif tree_node.right_child is not None:
            #     tree_node_queue.put(tree_node.right_child)
            #     print(tree_node.right_child.data, end=' ')
            #     continue

    # 深度优先之后序遍历（左右根）
    def postorder(self):
        print(f'{'——'*3} 后序遍历（左右根） {'——'*3} ')
        def depthTraversal(node):
            if node is None:
                return
            depthTraversal(node.left_child)
            depthTraversal(node.right_child)
            print(node.data, end=' ')
        depthTraversal(self.root)
        print()

def tree_test_case():
    bt = BinaryTree()
    bt.add(11)
    bt.add(21)
    bt.add(72)
    bt.add(3)
    bt.add(48)
    bt.add(86)
    bt.add(64)
    bt.add(9)
    bt.add(29)
    bt.add(55)
    bt.add(4)
    bt.add(95)
    bt.add(5)
    bt.add(1)
    bt.add(51)
    bt.add(15)
    bt.add(52)
    bt.add(15)
    bt.add(32)
    bt.add(0)
    bt.add(70)
    bt.add(67)
    bt.add(24)
    bt.add(32)
    bt.breadth()
    bt.preorder()
    bt.inorder()
    bt.postorder()


if __name__ == '__main__':
    tree_test_case()
