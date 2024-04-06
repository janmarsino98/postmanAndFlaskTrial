class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
class LinkedList:
    def __init__(self):
        self.head:Node = None
        self.last_node:Node = None
        
    def to_list(self):
        l = []
        if self.head is None:
            return l
        
        node = self.head
        while  node:
            l.append(node.data)
            node = node.next_node
            
        return l
        
    def print_ll(self):
        ll_string = ""
        node:Node = self.head
        if node is None:
            print(None)

        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node
            
        ll_string += " None"
        
        print(ll_string)
        
        
    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        else:
            self.head = Node(data, self.head)
    
    def insert_at_end(self, data):
        if not self.head:
            self.insert_beginning(data)
            return
        
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node
        
    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] == int(user_id):
                return node.data
            node = node.next_node
        return None