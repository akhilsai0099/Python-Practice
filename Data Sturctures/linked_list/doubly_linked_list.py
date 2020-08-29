class Node:
    def __init__(self, data = None , next = None , prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_begining(self , data):
        node = Node(data , self.head , None)
        self.head.prev = node
        self.head = node

    def insert_at_the_end(self , data):
        if self.head is None:
            self.head = Node(data,None ,None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next

            itr.next = Node(data , None,itr)
    
    def print_forward(self):
        if self.head is None:
            print("Your linked list is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Your linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ""

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.prev
        print(llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr


    def insert_values(self , data_list):
        for data in data_list:
            self.insert_at_the_end(data)

    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
            itr = itr.next
            counter += 1
        print(f"Length of linked list is {counter}") 
        return counter

    def remove_at_index(self , index):
        if index < 0 or index >= self.get_length():
            raise Exception("The index is not valid")

        if index == 0:
            self.head = self.head.next
            self.prev = None
            return

        itr = self.head
        counter = 0
        while itr:
            if counter == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            counter += 1
            itr = itr.next

    def insert_at_index(self , index , data):
        if index < 0 or index >= self.get_length():
            raise Exception("The index is not valid")
        
        if index == 0:
            self.insert_at_the_begining(data)
        
        itr = self.head
        counter = 0

        while itr:
            if counter == index -1:
                node = Node(data , itr.next,itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            counter += 1



if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    # ll.get_len()
    # ll.insert_at_index(0,1)
    # ll.get_last_node()
    ll.print_forward()