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

        if self.head == None:
            print("Linked List  is empty")
            return

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

        if self.head == None:
            return -1

        if self.head.next == None:
            self.head = None
            return traverse.data

        while traverse.next is not None:

            t1 = traverse.next

            if t1.next is None:
                traverse.next = None
                return t1.data
            traverse = traverse.next

    def pop_position(self, position):

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
#
#
# linkedlist_obj = LinkedList()
# linkedlist_obj.append(10)
# linkedlist_obj.append(20)
# linkedlist_obj.append(30)
# linkedlist_obj.append(40)
# linkedlist_obj.append(50)
# print(linkedlist_obj.size())
# linkedlist_obj.pop()
# linkedlist_obj.pop()
# linkedlist_obj.pop()
# linkedlist_obj.pop()
# linkedlist_obj.pop()

# list.append("rajat")
# list.insert(2,80)
# list.insert(7,90)
# print(list.is_empty())
# print(list.search_item("saurabh"))
# print(list.size())
# print(list.index(90))
#
# linkedlist_obj.pop()
# linkedlist_obj.pop()
# linkedlist_obj.pop()
# linkedlist_obj.pop()
# linkedlist_obj.pop()
# linkedlist_obj.pop()
# print(linkedlist_obj.pop())
# linkedlist_obj.show()

# list.pop()
# list.show()
#
# file=open("LinkedList_File","w+")
# list=['saurabh ','rajat ','shubham ','rohini']
# file.writelines(list)
# file.close()
# file=open("LinkedList_File","r")
# list=file.readlines()
# s=list[0]
# list=s.split()
# #print(list)
#
# for i in list:
#     linkedlist_obj.append(i)
#
# # linkedlist_obj.show()
#
# result=linkedlist_obj.search_item('ram')
#
# if result==True:
#     linkedlist_obj.remove('ram')
#
# if result==False:
#     linkedlist_obj.append('ram')
#
#
# linkedlist_obj.show()


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
                while traverse.next != None:
                    if traverse.data < node.data:
                        temp = traverse
                    traverse = traverse.next

                if traverse.data < node.data:
                    temp = traverse

                temp1 = temp.next
                temp.next = node
                node.next = temp1

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

    def is_empty(self):

        if self.head == None:
            return True
        else:
            return False

    def size(self):
        traverse = self.head
        count = 1
        while traverse.next != None:
            traverse = traverse.next
            count += 1
        return count

    def index(self, data):

        traverse = self.head
        count = 0
        while traverse.next != None:

            if traverse.data == data:
                return count
            traverse = traverse.next
            count += 1

        if traverse.data == data:
            return count

    def pop(self):

        traverse = self.head

        while traverse.next is not None:

            t1 = traverse.next
            if t1.next is None:
                traverse.next = None
                return t1.data
            traverse = traverse.next

    def pop_position(self, position):

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

    def show(self):
        traverse = self.head
        while traverse.next != None:
            print(traverse.data)
            traverse = traverse.next
        print(traverse.data)


ordered_list = OrderedList()


# ordered_list.add(10)
# ordered_list.add(1)
# ordered_list.add(2)
# ordered_list.add(3)
# ordered_list.add(4)
# ordered_list.add(-11)
# ordered_list.add(5)
# ordered_list.add(-1)
# ordered_list.add(-2)
# ordered_list.add(6)

# ordered_list.remove(-11)
# ordered_list.remove(10)
# print(ordered_list.search_item(0))
# print(ordered_list.is_empty())
# print(ordered_list.index(1))
# print(ordered_list.pop())
# print(ordered_list.pop_position(0))
# print(ordered_list.size())
# ordered_list.show()


class Stack:
    top = 0
    head = None

    def __init__(self):
        pass

    def push(self, data):

        node = Node(data)

        if self.head == None:

            self.head = node


        else:

            traverse = self.head

            while traverse.next != None:
                traverse = traverse.next

            traverse.next = node

    def size(self):
        traverse = self.head

        if self.head == None:
            return 0
        size = 1
        while traverse.next != None:
            traverse = traverse.next
            size += 1
        return size

    def show(self):
        traverse = self.head

        if self.top <= -1:
            print(" Stack Underflow")
            return
        if traverse == None:
            print("Stack is empty")
            return

        while traverse.next != None:
            print(traverse.data)
            traverse = traverse.next
        print(traverse.data)

    def pop(self):

        traverse = self.head

        if self.head == None:
            return -1

        if self.head.next == None:
            self.head = None

            return traverse.data

        while traverse.next is not None:

            t1 = traverse.next
            if t1.next is None:
                traverse.next = None

                return t1.data
            traverse = traverse.next

    def peek(self):
        traverse = self.head

        if self.head == None:
            return "empty stack"
        self.top = self.size() - 1
        for i in range(0, self.top):
            traverse = traverse.next

        return traverse.data

    def is_empty(self):

        if self.size() == 0:
            return True
        else:
            return False


stack = Stack()
stack1 = Stack()
# stack.push(56)
# stack.push(57)
# stack.push(58)
# stack.push(59)
# stack.push(60)
# stack.push(61)
# stack.push(62)


# stack.pop(57)
# stack.pop(58)
# stack.pop(59)
# stack.pop(60)
# stack.pop(61)
# stack.pop(62)
# stack.pop(63)
# print(stack.size())
# print(stack.peek())
# print(stack.is_empty())
# stack.show()

string = "{(([{}]))}"

for i in string:
    # print(i)
    if i == '(' or i == '[' or i == '{':
        stack.push(i)
        # stack.show()

    if ((stack.peek() == '(' and i == ')') or (stack.peek() == '[' and i == ']') or (
            stack.peek() == '{' and i == '}')) and stack.size() > 0:
        stack.pop()
        continue

    if i == ')' or i == ']' or i == '}':
        stack.push(i)


#
# if stack.size()==0:
#     print("Balanced Parenthesis ")
# else:
#     print("Parenthesis is not Balanced ")
# print(stack.size())
# stack.show()


class Queue:
    front = None
    rear = None

    def __init__(self):
        pass

    def enqueue(self, data):

        node = Node(data)

        if self.front == None and self.rear == None:

            self.front = node
            self.rear = node

        else:

            # while traverse.next != None:
            #     traverse = traverse.next

            self.rear.next = node
            self.rear = self.rear.next

    def show(self):

        if self.front == None:
            print("Linked List  is empty")
            return

        while self.front.next != None:
            print(self.front.data)
            self.front = self.front.next

        print(self.front.data)

    def dequeue(self):

        temp = self.front
        self.front = self.front.next
        return temp.data

    def is_empty(self):

        if self.front == None:
            return True
        else:
            return False

    def size(self):

        size = 1
        traverse = self.front
        if self.front == None:
            return 0

        while traverse.next != None:
            traverse = traverse.next
            size += 1
        return size


queue = Queue()



# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.enqueue(40)
# queue.enqueue(50)
#
# queue.dequeue()
# queue.dequeue()
#
# queue.show()
# print(queue.is_empty())
# print(queue.size())

class Deque:
    front = None
    rear = None

    def __init__(self):
        pass

    def add_front(self, data):
        node = Node(data)
        if self.front == None and self.rear == None:
            self.front = node
            self.rear = node

        else:
            node.next = self.front
            self.front = node

    def add_rear(self, data):

        node = Node(data)

        if self.front == None and self.rear == None:

            self.front = node
            self.rear = node

        else:

            self.rear.next = node
            self.rear = node

    def show(self):

        if self.front == None:
            print("Queue  is empty")
            return

        while self.front.next != None:
            print(self.front.data)
            self.front = self.front.next

        print(self.front.data)

    def remove_front(self):

        temp = self.front
        self.front = self.front.next
        return temp.data

    def remove_rear(self):

        traverse = self.front
        if self.rear == self.front:
            self.rear = None
            self.front = None
            return traverse.data

        while traverse.next != self.rear:
            traverse = traverse.next

        rear_value = self.rear
        self.rear = traverse
        traverse.next = None
        return rear_value.data

    def is_empty(self):

        if self.front == None:
            return True
        else:
            return False

    def size(self):

        size = 1
        traverse = self.front
        if self.front == None:
            return 0

        while traverse.next != None:
            traverse = traverse.next
            size += 1
        return size


deque = Deque()


# deque.add_rear(40)

# deque.add_rear(60)
# deque.add_rear(70)

# deque.remove_front()
# deque.remove_front()

# print( deque.remove_rear())
# print( deque.remove_rear())


# deque.remove_rear()
# deque.remove_rear()

# print(deque.is_empty())
# print(deque.size())

# deque.show()


class BinaryTreeNode:

    # def __init__(self, data,left=None, right=None):
    #     self.data = data
    #     self.left = left
    #     self.right=right
    def __init__(self):
        pass

    def count_binary_search_tree(self, test_cases):

        for i in test_cases:
            fact1 = 1
            for j in range(1, (i * 2) + 1):
                fact1 = fact1 * j

            fact2 = 1
            num = i + 1
            for l in range(1, num + 1):
                fact2 = fact2 * l

            nfact = 1

            for k in range(1, i + 1):
                nfact = nfact * k

            number_of_bst = (fact1 // (fact2 * nfact)) % 100000007
            print(number_of_bst)


utility_obj = Utility()


class Logic:

    def __init__(self):
        pass

    def anagram_stack(self):
        for i in utility_obj.get_anagram_prime():
            stack.push(i)

        for i in range(0, stack.size()):
            print(stack.pop())

    def anagram_queue(self):
        for i in utility_obj.get_anagram_prime():
            queue.enqueue(i)

        for i in range(0, queue.size()):
            print(queue.dequeue())

    def prime_no_2d_array(self):

        list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

        print(list[3][0])

    def prime_number_2d_array(self):

        prime_list = utility_obj.get_prime()
        row = 10
        column = 25
        limit = 100

        two_d_array = [[0 for j in range(column)] for i in range(row)]

        k = 0
        for i in range(row):

            for j in range(column):

                if k < len(prime_list):
                    if prime_list[k] <= limit:
                        two_d_array[i][j] = prime_list[k]
                        k += 1

            limit += 100

        for i in range(row):

            for j in range(column):

                if two_d_array[i][j] != 0:
                    print(two_d_array[i][j], end=" ")

            print()

    def anagram_2d_array(self):
        prime_list = utility_obj.get_prime()
        anagram_list = utility_obj.get_anagram_prime()
        not_anagram = []
        row = 10
        column = 25

        two_d_array = [[0 for j in range(column)] for i in range(row)]
        k = 0
        index = 0
        for i in prime_list:
            if anagram_list.__contains__(i) != True:
                not_anagram.append(i)

        for i in range(row):

            for j in range(column):

                if k < len(anagram_list):
                    two_d_array[i][j] = anagram_list[k]
                    k += 1

                if k >= len(anagram_list) and index < len(not_anagram):
                    two_d_array[i][j] = not_anagram[index]
                    k += 1
                    index += 1
        for i in range(row):

            for j in range(column):

                if two_d_array[i][j] != 0:
                    print(two_d_array[i][j], end=" ")

            print()

    def calender(self, month, year):

        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1
        d = 1

        m = month
        y = year
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        if utility_obj.isleap_year(str(year)):
            days[1] = 29
        row = 6
        column = 7
        two_d_array = [[0 for j in range(column)] for i in range(row)]

        print('Your Calender is Ready\n')

        for i in range(0, 6 + 1):
            print(day[i], end=' ')
        print()
        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:
                    if i == 0 and j < d0:
                        two_d_array[i][j] = ' '
                        continue

                    two_d_array[i][j] = values
                    values += 1

        for i in range(row):

            for j in range(column):
                if two_d_array[i][j] != 0:
                    x = two_d_array[i][j]
                    x1 = str(x).ljust(2)
                    print(x1, end=" ")

            print()

    def calender_queue(self, month, year):

        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1
        d = 1

        m = month
        y = year
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        if utility_obj.isleap_year(str(year)):
            days[1] = 29
        row = 6
        column = 7


        print('Your Calender is Ready\n')

        for i in range(0, 6 + 1):
            print(day[i], end=' ')
        print()
        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:
                    if i == 0 and j < d0:
                        queue.enqueue(' ')
                        continue

                    queue.enqueue(values)
                    values += 1

        for i in range(row):

            for j in range(column):
                if queue.size() > 0:
                    x = queue.dequeue()
                    x1 = str(x).ljust(2)
                    print(x1, end=" ")

            print()




    def calender_stack(self, month, year):
        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1
        d = 1

        m = month
        y = year
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        if utility_obj.isleap_year(str(year)):
            days[1] = 29
        row = 6
        column = 7


        print('Your Calender is Ready\n')

        for i in range(0, 6 + 1):
            print(day[i], end=' ')
        print()
        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:
                    if i == 0 and j < d0:
                        stack.push(' ')
                        continue

                    stack.push(values)
                    values += 1

        for i in range(stack.size()):
            stack_element=stack.pop()
            stack1.push(stack_element)


        for i in range(row):

            for j in range(column):
                if stack1.size() > 0:
                    x = stack1.pop()
                    x1 = str(x).ljust(2)
                    print(x1, end=" ")

            print()


logic_obj = Logic()
