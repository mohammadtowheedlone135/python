# try:
#     a = 10
#     b = 0
#     print(a/b)

# except ZeroDivisionError:
#     print("Cannot divide by zero")



# try:
#     tp = (10, 20, 30)

#     tp[1] = 50

#     print(tp)

# except TypeError:
#     print("Tuple cannot be changed")


# try:
#     student = {
#         "name": "Ali",
#         "age": 20
#     }

#     print(student["marks"])

# except KeyError:
#     print("Key does not exist")




# try:
#     a = 10.0 ** 1000
#     print(a)
# except OverflowError:
#     print("The number is too large")



# try:
#     age = 5
#     assert age >= 18
#     print("hello")
# except AssertionError:
#     print("Age must be 18 or above")




# try:
#     file = open("abc.txt", "r")
# except FileNotFoundError:
#     print("File does not exist")


# try:
#     numbers = [10, 20, 30]

#     x = iter(numbers)

#     print(next(x))
#     print(next(x))
#     print(next(x))
#     print(next(x))

# except StopIteration:
#     print("There are no more items")


