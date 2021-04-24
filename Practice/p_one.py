import unittest


def triangle_is_valid(side_one, side_two, side_three):
    if side_one <= 0 or side_two <= 0 or side_three <= 0:
        return False
    elif side_one + side_two < side_three or side_one + side_three < side_two or side_two + side_three < side_one:
        return False
    else:
        return True


class TestTriangle(unittest.TestCase):

    def test_all(self):

        test_data = [
            ((0, 0, 0), False),
            ((-1, -4, 2), False),
            ((3, 2, 1), True)
        ]

        for sides, expected in test_data:
            with self.subTest(sides=sides):
                actual = triangle_is_valid(*sides)
                self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
