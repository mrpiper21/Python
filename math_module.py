import math

x = 9.6
# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
#result = math.ceil(x) #always rounding a floating number
#print(result)

#CIRCUMFERNCE OF A CIRCLE
# radius = float(input('Enter the radius of a circle: '))
# circumference = 2 * math.pi * radius
# cr = math.ceil(circumference)
# print(f'circumference is {cr}')

#AREA OF A CIRCLE
# radius = float(input('Enter the radius of the circle: '))
# Area = math.pi * pow(radius, 2)
# print(f'The area of the circle is {round(Area)}cm^2')

#FINDING HYPOTHNUS
opp = int(input('Enter the opposite value: '))
adj = int(input('Enter the adjascent value: '))
sum = pow(opp, 2) + pow(adj, 2)
hyp = math.sqrt(sum)
print(f'The hypotenus is {round(hyp)}')
