from Node_sandbox import Node
import logging

class Queue:
    def __init__(self, head_node=None, tail_node=None, size=0, max_size=None):
        self.head_node = head_node
        self.tail_node = tail_node
        self.size = size
        self.max_size = max_size

    def get_size(self):
        return self.size

    def has_space(self):
        if(self.max_size is None):
            return True
        else:
            if(self.max_size > self.get_size()):
                return True
            else:
                return False

    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if(self.is_empty()):
            print("¡No hay nada que ver aquí!")
        else:
            return self.head_node.get_value()
    
    def enqueue(self, value):
        if(self.has_space()):
            item_to_add = Node(value)
            print(f"¡Agregando {item_to_add.get_value()} a la cola!")
            if(self.is_empty()):
                self.head_node = item_to_add
                self.tail_node = item_to_add
            else:
                self.tail_node.set_next_node(item_to_add)
                self.tail_node = item_to_add
            self.size += 1
        else:
            logging.warning("¡Lo sentimos, no hay más espacio!")

    def dequeue(self):
        item_to_remove = Node(None)
        if(not self.is_empty()):
            item_to_remove = self.head_node
            logging.info("¡Eliminando" + str(item_to_remove.get_value()) + "de la cola!")
            if(self.get_size() == 1):
                self.head_node = None
            else:
                self.head_node = self.head_node.get_next_node()
            self.size = self.size - 1
        else:
            logging.info("¡Esta cola está totalmente vacía!")
        return item_to_remove.get_value()