# Using list comprehension, create a list of squares of all odd numbers from 1 to 20

new_list1 =[i*i for i in range(1,21) if not i%2==0 ] 
new_list2  =[i*i for i in range(1,21) if  i%2==1 ] 


print(new_list1)
print(new_list2)
