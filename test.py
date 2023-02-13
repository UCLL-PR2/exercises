import numpy as np
import time

# create a large list/array of numbers
size = 100000000
my_list = list(range(size))
my_array = np.array(my_list)

# perform a mathematical operation on the list/array and time it
start_time = time.time()
new_list = [x * 2 for x in my_list]
end_time = time.time()
list_time = end_time - start_time

start_time = time.time()
new_array = my_array * 2
end_time = time.time()

array_time = end_time - start_time

# print the results
print(f"Python list time: {list_time:.6f} seconds")
print(f"NumPy array time: {array_time:.6f} seconds")
