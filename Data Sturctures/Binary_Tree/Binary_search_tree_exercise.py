class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data: # checking if there is a clone of data
            return

        if data < self.data: # data goes to the left node as it is smaller than the parentnode
            if self.left: # checking if there is any left node for the self
                self.left.add_child(data) # recursing the add child method to add the child 
            else:
                self.left = BinarySearchTreeNode(data) # adding the data to the tree if there is no left node to self

        if data > self.data: # same as above for the right node
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def in_order_traversal(self):

        # in order traversal stores the data in the order : left-node , parent-node and right-node 

        elements = []

        if self.left:
            elements += self.left.in_order_traversal() # adding data to the elements recursively

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    

    def search(self , value):
        if self.data == value:
            return True
        
        if value < self.data:
            if self.left:
                return  self.left.search(value) # searching for data recursivly
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



def Build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    numbers = [15,12,7,14,27,20,23,88 ]
    numbers_tree = Build_tree(numbers)
    print("Input numbers:",numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())
    