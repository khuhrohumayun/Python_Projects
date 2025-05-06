student = {
    "name": "Muhammad Humayun",
    "age": 21,
    "major": "Computer Science"
}

print(student)
print(student["name"])  # Accessing a value





 # search minimum:

L = [1, 2, 3, 4, 66, 88, -10, 0, 20]

minValue = L[1]
counter = 2

while(counter <= len(L)):
    v = L[counter - 1]
    if v < minValue:
        minValue = v
    counter += 1
else:
    print("Minimum value is: ", minValue)





