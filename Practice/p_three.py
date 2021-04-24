def fizz_buzz(n):

    li = []
    for i in range(1, n + 1):

        if i % (3 * 5) == 0:
            li.append('FizzBuzz')
        elif i % 3 == 0:
            li.append('Fizz')
        elif i % 5 == 0:
            li.append('Buzz')
        else:
            li.append(str(i))
    return li


n = 30
result = fizz_buzz(n)
print(result)