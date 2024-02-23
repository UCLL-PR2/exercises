# Write your code here
 
def cakes(eggs, butter, flour):
    max_eggs = eggs// 5
    max_butter = butter // 250
    max_flour = flour // 250

    return min(max_eggs,max_butter,max_flour)