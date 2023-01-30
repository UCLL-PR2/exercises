my_list = [0, 3, -10, 2]

def is_it_sorted(my_list):
    for index, current_num in enumerate(my_list):
        if index == 0:
            prev_num = current_num
        elif prev_num > current_num:
            return index
        prev_num = current_num
        
    return "sorted!"

    #---other solution
    # for index,_ in enumerate(my_list):
    #     if index > 0:
    #         if my_list[index] < my_list[index - 1]:
    #             return index
    # return "sorted!"
