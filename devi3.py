
'''n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


n = int(input("Enter n: "))

for i in range(1, n + 1):
    print("Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()




n = int(input("Enter size: "))

num = 1
for i in range(n):
    for j in range(n):
        if num % 2 == 0:
            print("E", end=" ")
        else:
            print("O", end=" ")
        num += 1
    print()



n = int(input("Enter n: "))

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")



marks = [11, 22, 44, 55, 88]

for m in marks:
    if m >= 75:
        print(m, "- Distinction")
    elif m >= 50:
        print(m, "- Pass")
    else:
        print(m, "- Fail")'''



n = int(input("Enter rows: "))
m = int(input("Enter columns: "))

print("Enter first matrix:")
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter second matrix:")
B = []
for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

print("Result Matrix:")
for i in range(n):
    for j in range(m):
        print(A[i][j] + B[i][j], end=" ")
    print()
