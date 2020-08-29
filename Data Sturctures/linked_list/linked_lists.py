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

    def insert_at_the_end(self,data):
        if self.head is None:
            self.head = Node(data , None)
            return 
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data , None)
    

    def insert_values(self , data_list):
        self.head = None
        for data in data_list:
            self.insert_at_the_end(data)


    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
             counter += 1
             itr = itr.next
        return counter


    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('this is not valid index')
        if index == 0:
            self.head = self.head.next
            return
        count = 1
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


    def insert_at(self, index,data):
        if index < 0 or index >= self.get_length():
            raise Exception('this is not valid index')
        
        if index == 0:
            self.insert_at_the_begining(data)
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
                
            itr = itr.next
            count += 1

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
    ll.insert_values(['hello world', 'this', 'is', 'akhil'])
    ll.insert_at(0,1)
    ll.get_length
    ll.print()
    
