class Node:
    def __init__(self , data=None , next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_begining(self , data):
        node = Node(data , self.head)
        self.head = node

    def insert_at_the_end(self, data):
        if self.head is None:
            self.head = Node(data , None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            
            itr.next = Node(data,None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_the_end(data)

    def get_len(self):
        counter = 0
        itr = self.head
        while itr:
            itr = itr.next
            counter += 1
        return counter

    def remove_at_index(self , index):
        if index < 0 or index >= self.get_len():
            raise Exception('index is out of range')
        if index == 0:
            self.head = self.head.next
            return
        
        counter = 0
        itr = self.head
        while itr:
            if counter == index -1:
                itr.next = itr.next.next
            counter += 1
            itr = itr.next

    def insert_at_index(self,index,data):
        if index < 0 or index >= self.get_len():
            raise Exception('index is out of range')
        if index == 0:
            self.insert_at_the_begining(data)

        counter = 0
        itr = self.head
        while itr:
            if counter == index -1:
                node = Node(data , itr.next)
                itr.next = node
                break
            
            counter += 1
            itr = itr.next
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next
    
    def remove_by_value(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next




    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next

        print(llstr)



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    # ll.print()
    # ll.insert_after_value("mango","apple") # insert apple after mango
    # ll.print()
    # ll.remove_by_value("orange") # remove orange from linked list
    # ll.print()
    ll.remove_by_value("figs")
    ll.print()
    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.remove_by_value("grapes")
    # ll.print()