def sparse_search(data, search_val):
    print("Datos: " + str(data))
    print("Valor de búsqueda: " + str(search_val))

    first = 0
    last = len(data) - 1
    
    while first <= last:
        mid = (first + last) // 2
        
        if (data[mid] == ""):
            left = mid - 1
            right = mid + 1
            
            while (True):
                if (left < first and right > last):
                    print(f"{search_val} no está en el conjunto de datos")
                    return
                elif(right <= last and data[right] != ""):
                    mid = right
                    break
                elif(left >= first and data[left] != ""):
                    mid = left
                    break
                else:
                    left -= 1
                    right += 1
                    
        if (data[mid] == search_val):
            print(f"{search_val} encontrado en la posicion {mid}")
            return
        if (search_val < data[mid]):
            last = mid - 1
        if (search_val > data[mid]):
            first = mid + 1

    print(f"{search_val} no está en el conjunto de datos")
            