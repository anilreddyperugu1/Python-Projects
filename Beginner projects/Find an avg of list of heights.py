heights = input("Enter the heights separated by commas:")
height_list = heights.split()
print(height_list)

#creating a variable for range instead of length function
count = 0
for height in height_list:
    count = count + 1
# print(count)

#converting strings into integers
for i in range(0, count):
    height_list[i] = int(height_list[i])
# print(height_list)

#created a variable to add all the values
sum = 0
for i in height_list:
    sum += i
# print(i)

#doing avg
avg = sum/count
print(f"The round is: {round(avg)}")