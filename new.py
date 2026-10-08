# n=int(input("Enter a number: "))
# bus=False

# for i in range(2,n):
#     if n%i==0:
#         bus=True
#         break
# if n<=1:
#     print("not prime")
# elif bus==True:
#     print("not prime")
# else:
    
#     print("prime")



while True:
    n=int(input("Enter a number: "))
    if n <=1:
        print("Not Prime")
    else:
    
        for i in range(2,n):
        
            if n%i==0:
                 print("Not Prime")
                 break
        else:
            print("Prime number")
            ch = input("enter(yes) to repeat:-")
            if ch!='yes':
                break
        
             
        




    