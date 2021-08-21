hight =int(input("Высота треугольника:"))
for row in range(hight+1):
    for column in range(hight):
        if hight - row < column:
            print("*",end='')
        else:
            print('', end="")
    print()

