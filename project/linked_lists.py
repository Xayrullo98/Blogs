class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data
class Linkedlist:
    def __init__(self,nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head=node
            for elem in nodes:
                node.next=Node(data=elem)
                node=node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return str(nodes)

    def add_first(self,node):
        node.next = self.head
        self.head=node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail = node
        return self

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == target_node_data:
                if previous_node is None:
                    self.head = new_node
                else:
                    previous_node.next = new_node
                new_node.next = current_node
                return

            previous_node = current_node
            current_node = current_node.next
    """
    def add_before(self, target_node_data, new_node):
    if self.head is None:
        raise Exception("List is empty")

    if self.head.data == target_node_data:
        return self.add_first(new_node)

    prev_node = self.head
    for node in self:
        if node.data == target_node_data:
            prev_node.next = new_node
            new_node.next = node
            return
        prev_node = node
    
    """




linkedlist_object = Linkedlist(nodes=["1",'2','3','4','4'])
linkedlist_object.add_after('3',Node("Salom"))
print(linkedlist_object)
# linkedlist_object.add_last(Node(1))
# linkedlist_object.add_last(Node(2))
# linkedlist_object.add_last(Node(3))
# current_node = linkedlist_object.head
# while current_node is not None:
#     print(current_node)
#     current_node = current_node.next
# # first_node  = Node("Hello")
# # linkedlist_object.head=first_node
# # second_node = Node("bye")
# # third_node = Node("well")
# # first_node.next=second_node
# # second_node.next=third_node
# print(linkedlist_object)

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add_last(self, node):
#         if self.head is None:
#             self.head = node
#             self.tail = node
#             return
#
#         self.tail.next = node
#         self.tail = node
#
# # Create a linked list
# linked_list = LinkedList()
#
# # Add some nodes to the linked list
# linked_list.add_last(Node(1))
# linked_list.add_last(Node(2))
# linked_list.add_last(Node(3))
# print(linked_list.head)
# # Print the linked list
# current_node = linked_list.__repr__()
