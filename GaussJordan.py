main_list = [[0, 0, 0],[0, 0, 0]]
print("First Equation:")
main_list[0][0] = float(input("Enter co-efficient of x:- "))
main_list[0][1] = float(input("Enter co-efficient of y:- "))
main_list[0][2] = float(input("Enter constant:- "))
print("Second Equation:")
main_list[1][0] = float(input("Enter co-efficient of x:- "))
main_list[1][1] = float(input("Enter co-efficient of y:- "))
main_list[1][2] = float(input("Enter constant:- "))

for i in range(len(main_list)):
    if main_list[i][i] != 0:
        multiplicative_inverse = 1/main_list[i][i]
    else:
        multiplicative_inverse = 0
    for j in range(len(main_list[i])):
        main_list[i][j] *= multiplicative_inverse

    if i == 0:
        additive_inverse = main_list[i+1][i] * -1
        for k in range(len(main_list[i+1])):
            main_list[i+1][k] += (main_list[i][k] * additive_inverse)
    if i == 1:
        additive_inverse = main_list[i-1][i] * -1
        for k in range(len(main_list[i-1])):
            main_list[i-1][k] += (main_list[i][k] * additive_inverse)

print(" x = ", main_list[0][-1], "\n", "y = ", main_list[1][-1])