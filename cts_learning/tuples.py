## A tuple is an immutable list.
## Tuples are ordered.
## Value accessed by index.
## Iteration, looping, concatenation.
## Use when data should not change.
## You can't modify values in a tuple.
## This will raise an exception.

# days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Sunday')
# monday = days_of_the_week[0]
# print(monday)
# for day in days_of_the_week:
#     print(day)


##### Exception Error ###

# days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Sunday')
# days_of_the_week[0] = 'New Monday'
# print(days_of_the_week)

# days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Sunday')
# print(days_of_the_week)
# del days_of_the_week
# print(days_of_the_week)


## list() Built-in finction returns a list.
## tuple() Built-in function returns a tuple.
## type() Built-in function returns an object's type.
## The max() built-in function returns the largest item that is passed to it.
## The min() built-in function returns the smallest item that is passed to it.

##### type function #######

# weekend_tuple = ('Saturday', 'Sunday')
# weekend_list = list(weekend_tuple)
# print('weekend_tuple is {}.'.format(type(weekend_tuple)))
# print('weekend_tupe is {}.'.format(type(weekend_list)))

####### for loop #####

# weekend_days = ('Saturday', 'Sunday')
# for day in weekend_days:
#     print(day)


# contact_info = ['555-0123', 'amir@xyz.com'] 
# (phone, email) = contact_info
# print(email)
# print(phone)

#### tuple function ###

# def high_and_low(numbers):
#     """Determibe the hihest and lowest number"""
#     highest = max(numbers)
#     lowest = min(numbers)
#     return (highest, lowest)

# lottery_numbers = [16, 4, 42, 15, 23, 8]
# (highest, lowest) = high_and_low(lottery_numbers)
# print('The highest number is: {}'.format(highest))
# print('The lowest number is: {}'.format(lowest))
