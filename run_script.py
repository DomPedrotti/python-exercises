number = input("enter an integer")
print("|number    |squared   |cubed     |")
print("|----------|----------|----------|")
for i in range(1,int(number)+1):
    blank_space_number = (10-len(str(i))) * ' '
    blank_space_square = (10 -len(str(i**2))) * " "
    blank_space_cube = (10 -len(str(i**3))) * " "
    print("|" + str(i) + blank_space_number + "|" + str(i**2) + blank_space_square + "|" + str(i**3) + blank_space_cube + "|")
