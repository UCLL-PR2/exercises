my_list = [0, 1, -10, 2]

def is_it_sorted(my_list):
    for index, current_num in enumerate(my_list):
        if index == 0:
            prev_num = current_num
        elif prev_num > current_num:
            return index
        prev_num = current_num
        
    return "sorted!"