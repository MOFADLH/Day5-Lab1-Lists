Q\1
list = [5, 4, 17, 19, 30, 2, 7, 10, 45]
print(list)
print("sum of list: ",sum(list))

Q\2
heights = [5, 4, 17, 19, 30, 2, 7, 10, 45]
largest_number = heights[0]
for number in heights:
    if number > largest_number:
        largest_number = number
print(largest_number)

Q\3
list1 = [5, 4, 17, 19, 30, 2, 7, 10, 45]
for num in list1:
    if num % 2 == 0:
        print(num, end=" ")

Q\4
print(lst[0:5])