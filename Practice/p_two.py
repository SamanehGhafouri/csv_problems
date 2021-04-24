def prime_number(number):
    if number < 2:
        return False
    else:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True


num = 1
result = prime_number(num)
print(result)

