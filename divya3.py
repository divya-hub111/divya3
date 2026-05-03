
'''age=int(input("enter the age:"))
weight=int(input("enter the weight:"))
if age > 18:
    if weight > 48:
        print("you can donate blood")
    else:
            print(" age is low you cannot donate")
else:
                 print("weight is low you cannot donate")'''



'''for i in range(18):
    for j in range(14):
        print(i,j)
    print("*",end="")
print()'''


rows=int(input("enter number of rows:"))

for i in range(1,rows +5):
   print("*"*i)




'''data = {
    "divya": "1234",
    "motii": "abcd",
    "myili": "pass"
}

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in data and data[username] == password:
        print(" Login Successful")
        break
    else:
        attempts -= 1
        print(" Wrong details")
        print("Attempts left:", attempts)

if attempts == 0:
    print(" Account Locked")'''





'''snacks = ["momos", "sandwich", "samosa"]

item = input("Enter snacks name: ")

if item in snacks:
    print("Available")
else:
    print("Not Available")'''







'''numbers = [10, 20, 30, 40]

print(20 in numbers)      
print(10 in numbers)      
print(40 in numbers)'''





a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
