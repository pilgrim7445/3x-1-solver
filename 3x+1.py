print("3x+1 solver")

n = int(input("Number: "))

while True:
    if (n % 2) == 0:
       n = n/2
       print(n)
    else:
       n = n*3+1
       print(n)
       
    if n == 1:
        break