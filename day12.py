class A:
    def ok(self):
        print('this is from A')
class B:
    def ok(self):
        print('this is from B')
class C(A,B):
    pass
c = C()
c.ok()
print(C.mro())



# a = 257
# b = 257
# print(a is b)


# a = [10,20,30]
# b = [10,20,30]
# print(a is b)

# a = (1,2,3)
# b = (1,2,3)
# print(a is b)
