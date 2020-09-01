class BinarySearchTreeNode:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self , data):
        if self.data == data:
            return

        if data < self.data:#add data in left sub tree
            if self.left:
                self.left.add_child(data)
            else :
                self.left = BinarySearchTreeNode(data)
        
        else:
            if self.right:
                self.right.add_child(data)
            else :
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self , value):
        if self.data == value:
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
        

def Build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    numbers = [32,343,123 ,23 ,4342,345]
    numbers_tree = Build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(1238))
    print(numbers_tree.search(32))
    print(numbers_tree.search(12))