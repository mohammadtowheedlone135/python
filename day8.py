
# def prime(n):
#     if n <=1:
#         print("Not Prime")
#     else:

#         for i in range(2,n):
        
#             if n%i==0:
#                 print("Not Prime")
#                 break
#         else:
#             print("Prime number")

# n = int(input("Enter an number:-"))
# prime(n)


def palindrome():
    n = input("Enter an word:-")

    word = n[::-1]

    if n == word:
        print("Palindrome")
    else:
        print("Not Palindrome")
# x = input("Enter an string:-")

palindrome()





