# Write your code here
def cakes(eggs, butter, flour):
    cakes_per_eggs = eggs // 5
    cakes_per_butter = butter // 250
    cakes_per_flour = flour // 250
    return min(cakes_per_eggs, cakes_per_butter, cakes_per_flour)