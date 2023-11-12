# #List: ordered, mutable, allows duplicate elements
# mylist = ['banana', 'cherry', 'apple']
# print(mylist)
#
# mylist_2 = [5, 4, 56, True, 'apple']
# item = mylist_2[-2]
# print(item)
#
# for i in mylist_2:
#     print(i)
#
# if 'ap' in mylist_2:
#     print('yes')
# else:
#     print('no')
# #insert an item in a specific location
# mylist_2.insert(1, 'nukes')
# print(mylist_2)
#
# #sort
# mylist_2 =sorted(mylist)
#
# #Returns the last item and removbes it
# item = mylist_2.pop()
# print(item)
# print(mylist_2)
# #Remove a specipic element
# rev = mylist_2.remove(5)
# print(rev)
#
# #Reverse the list
# revess = mylist_2.reverse()
# print(revess)


# seclist = [0] * 5
# print(seclist)
#
# list_3 = [3,4,2,3,2,2]
# mynewlist = seclist + list_3
# print(mynewlist)
# print(sorted(mynewlist))

jamlist = [3,53,434,345,223]
a = jamlist[::-1]
print(a)

#copying a list
list_org = ['BANANA', 'CHERRY', 'APPLE']
list_cpy = list_org
print(list_cpy)
