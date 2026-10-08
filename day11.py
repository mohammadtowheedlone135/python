# class dog:
#     def speak(self):
#         print("bhow bhow")
# class cat:
#     def speak(self):
#         print("meow meow")
# K = dog()
# M = cat() 
# K.speak()
# M.speak()

# class Ils:
#     def institute(self):
#         print('this is ils srinagar')
# class techbox(Ils):
#     def institute(self):
#         super().institute()
#         print('this is branch of the ils')
# t = techbox() 
# t.institute()     




class ils:
    def __init__(self):
        print('this is damn constructor')
        # self.__fee()
    def hello(self):
        print('this is in the pubblic domain')
    def _bye(self):
        print('this is the protceted')
    def __fee(self):
        print('this is private')        

a = ils()
a.hello()
a._bye()
a._ils__fee()        







              
              