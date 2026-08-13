# write python code  find max without using max() function.

nums = [-6,-5,-7,-8,-2]


# ---> use float("-inf")  , not use maxi = 0 

maxi =float("-inf")  
for num in nums:
    if num > maxi:
        maxi = num

print(maxi)