# Given a list, remove all duplicate elements while
# preserving the original order of the unique items.
data = [10, 20, 30, 20, 10, 40, 50, 40]

def remove_duplicate(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

print(remove_duplicate(data))