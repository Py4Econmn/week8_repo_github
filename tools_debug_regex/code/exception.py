## Exception
randomList = [5,15.5,20,0,'a', 0, 2,40,51,0.2]


for entry in randomList:
    r = 1/int(entry)
    print(r)

for entry in randomList:
    try: 
        r = 1/int(entry)
        print(r)
    except:
        # print("Warning! Not converting. Variable {} is of {} type".format(entry,type(entry)))
        print("Entry is {}. Using default val without converting.".format(entry))
        r = 1
        print(r)


import sys
# error system message
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        print("It works!")
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        continue
    print("The reciprocal of", entry, "is", r)

# errors handled differently
for entry in randomList:
    try:
       # do something
        r = 1/int(entry)
        print("Success.")
    except ValueError:
       # handle ValueError exception
       print('Division by wrong type!')
       entry = 5
       r = 1/int(entry)
    except (TypeError, ZeroDivisionError):
       # handle multiple exceptions
       # TypeError and ZeroDivisionError
       print('Division by Zero!')
       entry = entry+1
       r = 1/int(entry)
    
    print("Inverse of entry is " + str(r))
   

# User defined exception
class myStrangeError(Exception):
    # do correction here
    print("My strange error occurred!")
    
a = 6
# a = '51'
try:
    if a > 5:
        a = a + 100 
        print("Result: {}".format(a))
    else:
        raise myStrangeError()
except myStrangeError:
    print("My strange error occurred!, so adding only 10")
    a = a + 10
    print("Result: {}".format(a))
except:
    print("Another error occurred!, so adding 1000")
    a = int(a) + 1000
    print("Result: {}".format(a))


# # User defined exception
# class myStrangeError(Exception):
#     # do correction here
#     print("My strange error occurred!")
    
# # a = 4
# a = '51'
# try:
#     if a > 5:
#         a = a + 100 
#         print("Result: {}".format(a))
#     else:
#         raise myStrangeError()
# except myStrangeError:
#     print("My strange error occurred!, so adding only 10")
#     a = a + 10
#     print("Result: {}".format(a))
# except:
#     print("Another error occurred!, so adding 1000")
#     a = int(a) + 1000
#     print("Result: {}".format(a))