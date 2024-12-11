# Se importa la clase Node 
from Node_sandbox import Node

# Escribe debajo el codigo de la clase LinkedList y sus respectivos metodos     
class LinkedList():
    def __init__(self, value=None):
        if value is not None:
            self.head_node = Node(value)
        else:
            self.head_node = None
        
    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node is not None:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.head_node
        
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            current_node = None 
        else:
            while current_node is not None:
                next_node = current_node.get_next_node()
                if next_node is not None and next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    next_node = None 
                    break  
                current_node = next_node
                
    
    def swap_nodes(self, val1, val2):
        if val1 == val2:
            print('Los elementos son iguales por lo que no es necesario intercambiarlos')
            return None
        
        node1 = self.get_head_node()
        node2 = self.get_head_node()
        node1_prev = None
        node2_prev = None

        while node1 is not None:
            if node1.get_value() == val1:
                break
            node1_prev = node1
            node1 = node1.get_next_node()

        while node2 is not None:
            if node2.get_value() == val2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()

        if(node1 is None or node2 is None):
            print('No es posible realizar el intercambio: uno o más elementos no están en la lista')
            return None
        
        if (node1_prev == None):
            self.head_node = node2
        else:
            node1_prev.set_next_node(node2)
            
        if (node2_prev == None):
            self.head_node = node1
        else:
            node2_prev.set_next_node(node1)

        pivote = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(pivote)