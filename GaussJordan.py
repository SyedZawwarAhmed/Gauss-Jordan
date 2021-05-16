main_list = [[0, 0, 0],[0, 0, 0]]
print("First Equation:")
main_list[0][0] = float(input("Enter co-effiecient of x:- "))
main_list[0][1] = float(input("Enter co-effiecient of y:- "))
main_list[0][2] = float(input("Enter constant:- "))
print("Second Equation:")
main_list[1][0] = float(input("Enter co-effiecient of x:- "))
main_list[1][1] = float(input("Enter co-effiecient of y:- "))
main_list[1][2] = float(input("Enter constant:- "))

for i in range(len(main_list)): 
    multiplicative_inverse = main_list[i][i]
    for j in range(len(main_list[i])):
        main_list[i][j] *= (1/multiplicative_inverse)

    if i == 0:
        additive_inverse = main_list[i+1][i] * -1
        for k in range(len(main_list[i+1])):
            main_list[i+1][k] = main_list[i+1][k] + (main_list[i][k] * additive_inverse)
    if i == 1:
        additive_inverse = main_list[i-1][i] * -1
        for k in range(len(main_list[i-1])):
            main_list[i-1][k] = main_list[i-1][k] + (main_list[i][k] * additive_inverse)

print(" x = ", main_list[0][-1], "\n", "y = ", main_list[1][-1])