# l = [1, 2, 3, 4, 5]

# square = lambda x: x*x

# sqList = map(square, 1)
# print(list(sqList))


def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers)) # map returns a map object, convert to list.
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]