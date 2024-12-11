# Agrega el codigo de la funcion nth_last_element() debajo
from Node_sandbox import Node

def nth_last_element(ll, n):
    lead_pointer = ll.get_head_node()
    follow_pointer = ll.get_head_node()

    for _ in range(n):
        if lead_pointer is None:
            return None
        lead_pointer = lead_pointer.get_next_node()

    while lead_pointer is not None:
        lead_pointer = lead_pointer.get_next_node()
        follow_pointer = follow_pointer.get_next_node()

    return follow_pointer
