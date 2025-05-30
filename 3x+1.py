print("3x+1 solver")

mode = int(input("Mode (1 or 2): "))
if mode == 1:
    n = int(input("Number: "))
    a = n
    iter = 0

    while True:
        if (a % 2) == 0:
           a = a/2
           print(int(a))
            iter += 1
        else:
           a = a*3+1
           print(int(a))
           iter += 1
        if a == 1:
            break
if mode == 2:
    print("wait for an upd")

print("")
print("The number ", n, "took", iter, "iterations to get to 1.")
