cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)

print(f"The first items in the list are: {cubes[:3]}")
print(f"Three items from the middle of the list are: {cubes[3:6]}")
print(f"The last three items in the list are: {cubes[-3:]}")