def sum_of_factors(num):
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum += i
    return sum


x = 0
fact_sum = []
amicable = []


def generate():
    i = 1
    while not len(amicable) == 10:
        t = sum_of_factors(i)
        if (i, t) in fact_sum and (not i == t):
            amicable.append((i, t))
            print((i, t))
        fact_sum.append((t, i))
        i += 1


print("The first 10 pairs of amicable numbers are : ")
generate()
