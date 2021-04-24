import unittest


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



# n = 30
# result = fizz_buzz(n)
# print(result)


class TestFizzBuzz(unittest.TestCase):

    def test_one_fizz_fuzz(self):

        actual = fizz_buzz(3)
        expected = ['1', '2', 'Fizz']
        self.assertEqual(expected, actual)

    def test_two_fizz_buzz(self):

        actual = fizz_buzz(15)
        expected = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()