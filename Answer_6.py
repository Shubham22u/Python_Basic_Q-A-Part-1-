#Test Data:
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
#Expected Output:
{'Black', 'White'}

print(color_list_1 - color_list_2)
# OR
print(color_list_1.difference(color_list_2))