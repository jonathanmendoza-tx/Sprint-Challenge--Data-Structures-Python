class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        
        if node is not None:
            
            cur_node = node
            lis = []

            while cur_node is not None:
                lis.append(cur_node.value)
                cur_node = cur_node.get_next()

            cur_node = self.head

            if len(lis) == 1:

                self.head = node

            else:

                while len(lis) >= 1:

                    if cur_node is self.head:
                    
                        self.head = Node(lis.pop())
                        self.head.set_next(Node(lis.pop()))

                        cur_node = self.head.next_node

                    cur_node.set_next(Node(lis.pop()))

                    cur_node = cur_node.get_next()

        else:
            return None
