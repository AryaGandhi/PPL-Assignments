given_list = []
n = int(input("Enter number of pages between 1 and 25 : "))
print("Enter the list of pages between 1 and 25: ")
for i in range(0, n):
    element = int(input())
    given_list.append(element)
missing = [x for x in range(1, 26) if x not in given_list]
print("The list of pages missing in the book are : ")
print(missing)
