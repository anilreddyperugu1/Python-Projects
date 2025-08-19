numbers = input("Enter the numbers separated by space:")
numbers_list = numbers.split()
print(numbers_list)

#creating a variable to find length instead of using len function
count = 0
for i in numbers_list:
    count = count + 1

# converting string numbers into integers in the list
for i in range(0, count):
    numbers_list[i]= int(numbers_list[i])
print(numbers_list)

# finding the max number
max_num = numbers_list[0]
for i  in numbers_list:
    if i > max_num:
        max_num = i
print(f"The max number is: {max_num}")