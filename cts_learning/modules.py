## In this we learn ###
## Modules
## More built-in python functions
## Python Standard Library

# import time

# print(time.asctime())
# print(time.timezone)

##### from below module we can import the sleep syntax for defined time ####
# from time import asctime, sleep

# print(asctime())
# sleep (5)
# print(asctime())

## from import time we can see the list of dir from module ##  not working as expected

# import time
# dir(time) 
# print(dir)

# import say
# for path in sys.path:
#     print(path)

import say_hi
say_hi.say_hi
def say_hi():
    print('Hi!')
    