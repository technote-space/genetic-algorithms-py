from enum import IntFlag, auto


class FieldFlags(IntFlag):
    """
    Description:
    ------------
    Flags
    """

    NONE = 0
    FOOD = auto()
    VISITED = auto()
