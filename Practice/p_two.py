import unittest


def prime_number(n):

    if n < 2:
        return False
    else:
        for num in range(2, n):

            if n % num == 0:
                return False
        return True


class TestPrimeNumber(unittest.TestCase):

    def test_one_prime_number(self):

        actual = prime_number(0)
        expected = False
        self.assertEqual(expected, actual)

    def test_two_prime_number(self):

        actual = prime_number(1)
        expected = False
        self.assertEqual(expected, actual)

    def test_three_prime_number(self):

        actual = prime_number(2)
        expected = True
        self.assertEqual(expected, actual)

    def test_four_prime_number(self):

        actual = prime_number(7)
        expected = True
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
