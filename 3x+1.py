print("3x+1 solver")

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

print("")
print("The number ", a, "took", iter, "iterations to get to 1.")
