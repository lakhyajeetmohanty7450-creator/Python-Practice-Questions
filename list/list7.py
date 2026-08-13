# Given a list of numbers (which may contain duplicates), write a
# Python script that takes an integer as input from the user and
# removes all occurrences of that integer from the list.


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
my_list = [10, 20, 10, 30, 20, 10, 40,1,1,1,1,1,1,1,1,1,1, ]
#  this is wrong method 
def remove_duplicates():
    print(my_list)
    num =int(input("Enter your remove element: "))
    for i in my_list:
        if i == num:
            my_list.remove(i)
    return my_list
print(remove_duplicates())

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# method one 

my_list = [10, 20, 10, 30, 20, 10, 40,1,1,1,1,1,1,1,1,1,1 ]

def remove_all_target():
    print(my_list)
    new_lst = []
    target = int(input("Enter your remove number: "))
    for i in my_list:
        if i != target:
            new_lst.append(i)
    return new_lst

print(remove_all_target())


#method two
my_list = [10, 20, 10, 30, 20, 10, 40,2,2,2,2,2,2,2,2,2 ]

def remove_target(lst):
    print(lst)
    target = int(input("Enter your remove number: "))
    while target in lst:
        lst.remove(target)
    return lst

print(remove_target(my_list))

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  