# Linked list

# Creating a class Node
class Node :
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add a function to push an element at list
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self,data):
        new_node = Node(data)
        new_node.next = None
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next



# Main function
if __name__ == '__main__':
    list = LinkedList()

    list.head = Node(1)
    list.push(5)
    list.push(7)

    list.append(9)
    list.append(10)

    list.printlist()

