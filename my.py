# modulus = []
# value = input("Enter: ")
#
# for i in value:
#     f1 = ord(i)
#     for j in range(8):
#         md = int(f1 % 2)
#         f1 = f1 / 2
#         modulus.append(md)
#         modulus.reverse()
#     print('\n')
#     print(f1)
#
# x = []
# for i in modulus:
#     if i == 1:
#         x.append(f"\U0001F7E1")
#     else:
#         x.append(f"\U000026AB")
# # print(x)

x = open('sensitiveinfo.txt', 'r')
for i in x:
    print(i)