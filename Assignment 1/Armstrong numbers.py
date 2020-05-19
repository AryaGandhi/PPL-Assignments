lower_bound = int(input("Enter lower bound of the range : "))
upper_bound = int(input("Enter upper bound of the range : "))
for i in range(lower_bound, upper_bound + 1):
    sum = 0
    num = i
    while num > 0:
        digit = num % 10
        sum = sum + digit**3
        num = num // 10
    if sum == i:
        print(i)
