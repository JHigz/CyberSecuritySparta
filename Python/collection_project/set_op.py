colors = {'Black', 'Grey', 'Red', 'Green'}


print (colors)

for i in colors:
    print(i)

colors.add('white')
print(colors)

colors.discard('Grey')
print (colors)


print('================ Math and Sets =============')
colors1 = {'black', 'grey', 'red', 'blue'}
colors2 = {'black', 'blue'}

print(colors1)
print(colors2)

print("Intersect :", colors1 & colors2)
print('Union :', colors1 | colors2)
print('Difference: ', colors1 - colors2)
print('Superset :', colors1 > colors2) # if all of colors2 is in colors1

items = set(('coffee', 'tea', 'black', 'white'))
print (items)
