print("3x+1 solver")

n = int(input("Number: "))
a = n

while True:
    if (a % 2) == 0:
       a = a/2
       print(int(n))
    else:
       a = a*3+1
       print(int(n))
       
    if a == 1:
        break

print("The number {a}")
