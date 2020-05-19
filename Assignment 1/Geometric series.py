a = int(input("Enter first term of GP : "))
r = int(input("Enter common ratio : "))
print("The first 10 terms of the GP are : ")
for i in range(0, 10):
    term = a * (r**i)
    print(term)
