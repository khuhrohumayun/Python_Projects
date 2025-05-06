
           # In python functions is a block of code that can reuse to perform a specific task.
           # A function is defined using the def keyword, followed by the function name and parentheses.

def get_choice():
    player_choice = "rock"
    computer_choice = "paper"

    return player_choice



choices = get_choice()

print(choices)


# A simple fuction to add two numbers

def add_numbers(a, b):
    return a + b

#using the function
result = add_numbers(5, 7)
print("The sum is: ", result)



# A function to calculate the square of a number
def square(num):
    return num * num


print('Square: ', square(4))




# A function to find the maxinum of two numbers
def maximum(a, b):
    if a > b:
        return a 
    else:
        return b

print('Maximum: ', maximum(10, 20))



# A function to check if a number is even or odd
def is_even(num):
    if num %  2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print(f"The number {number} is {is_even(number)}")



# A function to calculate the averate of a list of numbers
def average(numbers):
    return sum(numbers) / len(numbers)


print('Average: ', average([10, 20, 30, 40]))




# A function to reverse a string
def reverse_string(s):
    return s[::-1]  

print('Reversed string: ', reverse_string("Hello"))


# A function to check if a string is a palindrome  

def is_palindrome(s):
    return s == s[::-1]

print('Is palindrome: ', is_palindrome("madam"))




        # Assingment given by the ChatGPT

# A function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

print('Area of rectangle: ', rectangle_area(5, 3))  # output: 15




 # A function to find if a number is positive, negative or zero
def number_type(num):
        if num > 0:
            return "Positive"
        elif num < 0:
            return "Negative"
        else:
            return "Zero"
        
print(f"The number is: {number_type(-7)}") # output: Negative



# A function to return the first character of a string
def first_character(s):
    return s[0]


print(f"First character: {first_character('Machine')}") # output: 'M'