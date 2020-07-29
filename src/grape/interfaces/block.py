from typing import List, Union


class INextBlock:
    """
    Description:
    ------------
    Next block interface
    """

    __perception: str
    __actions1: List[str]
    __next1: Union['INextBlock', int]
    __actions2: List[str]
    __next2: Union['INextBlock', int]

    def __init__(self, perception: str, actions1: List[str], next1: Union['INextBlock', int], actions2: List[str], next2: Union['INextBlock', int]):
        self.__perception = perception
        self.__actions1 = actions1
        self.__next1 = next1
        self.__actions2 = actions2
        self.__next2 = next2

    @property
    def perception(self) -> str:
        return self.__perception

    @property
    def actions1(self) -> List[str]:
        return self.__actions1

    @property
    def next1(self) -> Union['INextBlock', int]:
        return self.__next1

    @next1.setter
    def next1(self, value: Union['INextBlock', int]) -> None:
        self.__next1 = value

    @property
    def actions2(self) -> List[str]:
        return self.__actions2

    @property
    def next2(self) -> Union['INextBlock', int]:
        return self.__next2

    @next2.setter
    def next2(self, value: Union['INextBlock', int]) -> None:
        self.__next2 = value


class IFuncBlock:
    """
    Description:
    ------------
    Function block interface
    """

    __id: int
    __actions: List[str]
    __next: Union[INextBlock, int]

    def __init__(self, block_id: int, actions: List[str], next_item: Union[INextBlock, int]):
        self.__id = block_id
        self.__actions = actions
        self.__next = next_item

    @property
    def id(self) -> int:
        return self.__id

    @property
    def actions(self) -> List[str]:
        return self.__actions

    @property
    def next(self) -> Union[INextBlock, int]:
        return self.__next

    @next.setter
    def next(self, value: Union[INextBlock, int]) -> None:
        self.__next = value
