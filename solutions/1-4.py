# Write a function to calculate the square of a number
def square(n):
    return n*n

# Write a list comprehension using the square function to calculate the square of the numbers between 20 and 25 inclusive
[square(n) for n in range(20,25+1)]