colors = ['black', 'red', 'blue', 'white']

print(colors)
colors.append("orange")
colors.remove("blue")
print(colors[1])


for color in colors:
    print(color)

print(len(colors))

print("red in colours? ", "red" in colors)


colors.sort()

print(colors)

print("colors.index = " , colors.index("orange"))

print("Slice: ", colors[0:2])

print (colors)
