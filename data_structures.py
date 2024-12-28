# Lists
# names = ["John", "Christian", "Isingizwe", "Others"]
# print(names[0])
# Largest number in a list

number_list = [3,2,5,6,7,3,2]
smallest = number_list[0]
count = len(number_list)

while count > 0:
    if number_list[count-1] < smallest:
        smallest = number_list[count-1]
count -= 1

print(smallest)

# Tuples

numbering = (1,23,4,5,6)