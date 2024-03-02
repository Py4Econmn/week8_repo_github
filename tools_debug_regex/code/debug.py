# Useful resources
# https://www.youtube.com/watch?v=w8QHoVam1-I
# https://www.youtube.com/watch?v=6YLMWU-5H9o
# https://www.youtube.com/watch?v=ChuU3NlYRLQ
# https://docs.python.org/3/library/pdb.html
# https://realpython.com/python-debugging-pdb/#using-breakpoints

# debug a function - example

import pdb

def func(input):
    k = 7 + input
    h = 8 
    # a = 1/(input-input)
    # print("hi")
    # print(k)

for i in range(10,100):
    y = i + 10 
    func(15)
    print(i)
    # pdb.set_trace() # matlab : keyboard
    if i >= 3:
        a = 1/(i-5)



# func() # step into, step out - inside function


# class myStrangeError(Exception):
#     # do correction here
#     print("My strange error occurred!")
    
# a = 1
# try:
#     if a > 5:
#         a = a + 100 
#     else:
#         raise myStrangeError()
# except myStrangeError:
#     print("My strange error occurred!, so adding only 10")
#     a = a + 10
# except:
#     print("Another error occurred!, so adding 1000")
#     a = int(a) + 1000


# import pdb


# a = 5
# pdb.set_trace()
# a = 7

# # error
# b = a/0