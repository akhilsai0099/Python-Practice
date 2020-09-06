class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, child):
        if self.data == child:
            return 
    
        if child < self.data:
            if self.left:
                self.left.add_child(child) 
            else:
                self.left = BinarySearchTreeNode(child)
    
        if child > self.data:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = BinarySearchTreeNode(child)


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


    def find_min(self): # finding the minimum of the list 
        if self.left is None:
            return self.data # using this method because all the less values are stored in the left-node
        return self.left.find_min()        
    
    def find_max(self): # finding the maximum of the list 
        if self.right is None:
            return self.data # using this method because all the less values are stored in the right-node
        return self.right.find_max()

    def calculate_sum(self): # calculating the sum of all the data in the tree
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def pre_order_traversal(self):
        # pre_order_traversal stores the data in the order : self-node , left-node and right-node
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        # post_order_traversal stores the data in the order : left-node right-node and self-node
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)
        return elements


    def delete(self , value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value  > self.data:
            if self.right:
                self.right = self.right.delete(value)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            
            max_value = self.left.find_max()
            self.data = max_value
            
            self.left = self.left.delete(max_value)
        return self



def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]
