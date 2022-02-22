lucky_numbers = [1, 2, 3, 4, 5, 6]
friends = ["John", "Mike", "Kevin", "Kevin", "Jim", "Karl", "Chen"]


# friends.extend(lucky_numbers)  # add two list
friends.insert(1, "Kelly")  # insert value at index and push the rest of the list up
friends.remove("Mike")  # remove element from list
# friends.clear()  # clear the list
friends.pop()  # removes the last element in the list
print(friends)
print(friends.index("Jim"))  # get index of Kevin, if Kevin exists in the list
print(friends.count("Kevin"))  # count number of the parameter in the list
friends.sort()  # alphabetical order
print(friends)
lucky_numbers.reverse()  # reverse list order
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)
