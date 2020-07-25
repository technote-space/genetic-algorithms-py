from .field_flags import FieldFlags


class Helper:
    """
    Description:
    ------------
    Helper
    """

    __field = None
    __count = None

    @staticmethod
    def position_to_index(x, y, width):
        return x + width * y

    @staticmethod
    def get_name():
        return 'Santa Fe Trail'

    @staticmethod
    def get_width():
        return 32

    @staticmethod
    def get_height():
        return 32

    @staticmethod
    def get_energy():
        return 400

    @staticmethod
    def get_step_limit():
        return 800

    @staticmethod
    def __get_foods():
        return (
            [1, 0],
            [2, 0],
            [3, 0],
            [3, 1],
            [3, 2],
            [3, 3],
            [3, 4],
            [3, 5],
            [4, 5],
            [5, 5],
            [6, 5],
            [8, 5],
            [9, 5],
            [10, 5],
            [11, 5],
            [12, 5],
            [12, 6],
            [12, 7],
            [12, 8],
            [12, 9],
            [12, 10],
            [12, 12],
            [12, 13],
            [12, 14],
            [12, 15],
            [12, 18],
            [12, 19],
            [12, 20],
            [12, 21],
            [12, 22],
            [12, 23],
            [11, 24],
            [10, 24],
            [9, 24],
            [8, 24],
            [7, 24],
            [4, 24],
            [3, 24],
            [1, 25],
            [1, 26],
            [1, 27],
            [1, 28],
            [2, 30],
            [3, 30],
            [4, 30],
            [5, 30],
            [7, 29],
            [7, 28],
            [8, 27],
            [9, 27],
            [10, 27],
            [11, 27],
            [12, 27],
            [13, 27],
            [14, 27],
            [16, 26],
            [16, 25],
            [16, 24],
            [16, 21],
            [16, 20],
            [16, 19],
            [16, 18],
            [17, 15],
            [20, 14],
            [20, 13],
            [20, 10],
            [20, 9],
            [20, 8],
            [20, 7],
            [21, 5],
            [22, 5],
            [24, 4],
            [24, 3],
            [25, 2],
            [26, 2],
            [27, 2],
            [29, 3],
            [29, 4],
            [29, 6],
            [29, 9],
            [29, 12],
            [28, 14],
            [27, 14],
            [26, 14],
            [23, 15],
            [24, 18],
            [27, 19],
            [26, 22],
            [23, 23],
        )

    @staticmethod
    def get_field():
        if Helper.__field is None:
            Helper.__field = {}
            for food in Helper.__get_foods():
                Helper.__field[Helper.position_to_index(food[0], food[1], Helper.get_width())] = FieldFlags.FOOD

        return Helper.__field

    @staticmethod
    def get_count():
        if Helper.__count is None:
            Helper.__count = len(Helper.__get_foods())

        return Helper.__count
