def linear_search_v1(search_list, target_value):
    found_index = None
    
    for i in range(len(search_list)):
        if(search_list[i] == target_value):
            found_index = i
            break
            
    if(found_index is not None):
        return found_index
    else:
        raise ValueError("{0} no esta en la lista".format(target_value))

def linear_search_v2(search_list, target_value):
    found_index = []
    
    for i in range(len(search_list)):
        if(search_list[i] == target_value):
            found_index.append(i)
            
    if(found_index is not None):
        return found_index
    else:
        raise ValueError("{0} no esta en la lista".format(target_value))

def linear_search_vFail(search_list, target_value):
    found_index = None
    
    for i in range(len(search_list)):
        if(search_list[i] == target_value):
            found_index = i
            
    if(found_index is not None):
        return found_index
    else:
        raise ValueError("{0} no esta en la lista".format(target_value))


def linear_search_v3(search_list):
    found_index = None
    value = 0
    for i in range(len(search_list)):
        if(search_list[i] >= value):
            value = search_list[i]
            found_index = i
            
    if(found_index is not None):
        return found_index
    else:
        raise ValueError("{0} no esta en la lista".format(target_value))