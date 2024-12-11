# Escribe debajo el codigo de la clase Node y sus respectivos metodos     
class Node():
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self): 
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node
        if next_node is None or isinstance(next_node, Node) or isinstance(next_node, dict):
            self.next_node = next_node
        else:
            raise TypeError("next_node must be of type Node, dict, or None")