class Rectangle:

    def __init__(self, width, height, x, y):

        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def x(self) -> float:

        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def width(self) -> float:
        return self._width

    @property
    def height(self) -> float:
        return self._height

    @property
    def position(self) -> (float, float):
        return self._x, self._y

    @x.setter
    def x(self, x):

        self._x = x

    def area(self) -> float:

        area = self.width * self.height
        return area

    def find_min_on_x_axis(self, rectangle_one: 'Rectangle', rectangle_two: 'Rectangle'):

        return min(rectangle_one.x, rectangle_two.x)

    def find_max_on_x_axis(self, rectangle_one: 'Rectangle', rectangle_two: 'Rectangle'):

        return max(rectangle_one.x + rectangle_one.width, rectangle_two.x + rectangle_two.width)

    def find_min_on_y_axis(self, rectangle_one: 'Rectangle', rectangle_two: 'Rectangle'):

        return min(rectangle_one.y, rectangle_two.y)

    def find_max_on_y_axis(self, rectangle_one: 'Rectangle', rectangle_two: 'Rectangle'):

        return max(rectangle_one.y + rectangle_one.height, rectangle_two.y + rectangle_two.height)

    def collides_with(self, other_rect: 'Rectangle') -> bool:

        total_x_length = self.find_max_on_x_axis(self, other_rect) - self.find_min_on_x_axis(self, other_rect)
        total_y_length = self.find_max_on_y_axis(self, other_rect) - self.find_min_on_y_axis(self, other_rect)

        total_rectangles_width = self.width + other_rect.width
        total_rectangles_height = self.height + other_rect.height

        if total_rectangles_width > total_x_length and total_rectangles_height > total_y_length:
            return True
        else:
            return False


class Square(Rectangle):

    def __init__(self, length, x, y):

        super().__init__(length, length, x, y)

    @property
    def length(self):
        return self.width


if __name__ == '__main__':
    # my_rect = Rectangle(2, 4, 1, 6)
    # my_rect.x = 29
    # print(my_rect.x)

    rect_one = Rectangle(5, 2, 3, 3)
    rect_two = Rectangle(7, 4, 7, 2)

    print(rect_one.collides_with(rect_two))

    rect1 = Rectangle(1, 1, 1, 1)
    print(rect1.collides_with(Rectangle(1, 1, 2, 2)) == False)
    print(rect1.collides_with(Rectangle(1, 1, 1.5, 1.5)) == True)
    print(rect1.collides_with(Rectangle(1, 1, 1.5, 1.5)) == False)

    my_square = Square(3, 0, 0)
    print(my_square.area())

    square_two = Square(3, 2, 2)
    print(square_two.collides_with(my_square))

    square_three = Square(3, 9, 9)
    print(square_three.collides_with(square_two))