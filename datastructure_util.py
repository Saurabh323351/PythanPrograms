from com.bridgelabz.util.utility import Utility


class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head = None

    def __init__(self):
        pass

    def append(self, data):

        node = Node(data)

        if self.head == None:

            self.head = node

        else:

            traverse = self.head

            while traverse.next != None:
                traverse = traverse.next

            traverse.next = node

    def show(self):

        traverse = self.head
        while traverse.next != None:
            print(traverse.data)
            traverse = traverse.next

        print(traverse.data)

    def is_empty(self):

        if self.head == None:
            return True
        else:
            return False

    def search_item(self, data):

        traverse = self.head
        while traverse.next != None:

            if traverse.data == data:
                return True
            traverse = traverse.next
        if traverse.data == data:
            return True
        else:
            return False

    def size(self):
        traverse = self.head
        count = 0
        while traverse.next != None:
            traverse = traverse.next
            count += 1
        return count + 1

    def index(self, data):

        traverse = self.head
        count = 0
        while traverse.next != None:

            if traverse.data == data:
                return count
            traverse = traverse.next
            count += 1
        count += 1
        if traverse.data == data:
            return count

    def insert(self, position, data):

        node = Node(data)
        traverse = self.head

        for i in range(0, position - 1):
            traverse = traverse.next
        temp = traverse.next
        traverse.next = node
        node.next = temp

    def pop(self):

        traverse = self.head

        while traverse.next is not None:

            t1 = traverse.next
            if t1.next is None:
                traverse.next = None
                return t1.data
            traverse = traverse.next

    def pop(self, position):

        traverse = self.head
        temp = self.head

        if position == 0:
            self.head = traverse.next
            return traverse.data

        for i in range(0, position - 1):
            traverse = traverse.next

        temp = traverse
        traverse = traverse.next
        temp.next = traverse.next
        return traverse.data

    def remove(self, data):

        traverse = self.head
        temp = self.head
        if traverse.data == data:
            self.head = traverse.next
            return traverse.data

        while traverse.next != None:

            temp = traverse.next
            if temp.data == data:
                traverse.next = temp.next
                return temp.data

            traverse = traverse.next


# if __name__=='__main__ ':


linkedlist_obj = LinkedList()
# list.append(10)
# list.append(20)
# list.append(30)
# list.append(40)
# list.append(50)
# list.append(60)
# list.append("rajat")
# list.insert(2,80)
# list.insert(7,90)
# print(list.is_empty())
# print(list.search_item("saurabh"))
# print(list.size())
# print(list.index(90))


# list.pop(3)
#
# list.show()
# list.pop()
# list.show()

file=open("LinkedList_File","w+")
list=['saurabh ','rajat ','shubham ','rohini']
file.writelines(list)
file.close()
file=open("LinkedList_File","r")
list=file.readlines()
s=list[0]
list=s.split()
#print(list)

for i in list:
    linkedlist_obj.append(i)

# linkedlist_obj.show()

result=linkedlist_obj.search_item('shubh')

if result==True:
    linkedlist_obj.remove('shubh')

if result==False:
    linkedlist_obj.append('shubh')


linkedlist_obj.show()




class OrderedList:
    head = None
    list = [10, 1, 2, 7, 5, 3]

    def __init__(self):
        pass

    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node

        else:
            traverse = self.head
            if self.head.data > node.data:
                self.head = node
                node.next = traverse

            if self.head.data < node.data:
               temp = self.head
               while traverse.next!=None:
                   if traverse.data<node.data:
                       temp=traverse
                   traverse = traverse.next

               if traverse.data < node.data:
                   temp = traverse

               temp1 = temp.next
               temp.next= node
               node.next = temp1


    def show(self):
        traverse = self.head
        while traverse.next != None:
            print(traverse.data)
            traverse = traverse.next
        print(traverse.data)


ordered_list = OrderedList()
ordered_list.add(10)
ordered_list.add(1)
ordered_list.add(2)
ordered_list.add(3)
ordered_list.add(4)
ordered_list.add(11)
ordered_list.add(5)
ordered_list.add(-1)
ordered_list.add(-2)
ordered_list.add(6)
ordered_list.show()
