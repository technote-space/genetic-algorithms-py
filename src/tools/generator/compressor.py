from typing import Iterable, List, MutableMapping, Union, Optional, Callable, Tuple, cast
from grape import IFuncBlock, INextBlock


class Compressor:
    """
    Description:
    ------------
    圧縮クラス
    """

    @staticmethod
    def compress(program: List[IFuncBlock], start: int, threshold: int = 6) -> Iterable[IFuncBlock]:
        blocks: MutableMapping[int, IFuncBlock] = {}
        for block in program:
            blocks[block.id] = block

        Compressor.__replace_small_blocks(blocks, threshold)
        Compressor.__remove_unused_block(start, blocks)

        return blocks.values()

    @staticmethod
    def __calc_if_block_size(block: INextBlock, threshold: int, prev: int) -> int:
        if block.next1 == block or block.next2 == block:
            return 10000

        size = len(block.actions1) + len(block.actions2)
        if prev + size > threshold:
            return size

        if type(block.next1) is int:
            size += 2
        else:
            next_block1 = cast(INextBlock, block.next1)
            size += Compressor.__calc_if_block_size(next_block1, threshold, prev + size)
        if prev + size > threshold:
            return size
        if type(block.next2) is int:
            size += 2
        else:
            next_block2 = cast(INextBlock, block.next2)
            size += Compressor.__calc_if_block_size(next_block2, threshold, prev + size)

        return size

    @staticmethod
    def __calc_block_size(block: IFuncBlock, threshold: int) -> int:
        size = len(block.actions)
        if type(block.next) is int:
            size += 1
        else:
            next_block = cast(INextBlock, block.next)
            size += Compressor.__calc_if_block_size(next_block, threshold, 0)

        return size

    @staticmethod
    def __get_replace_target_key(blocks: MutableMapping[int, IFuncBlock], threshold: int, exclude: MutableMapping[int, bool]) -> Optional[int]:
        lambda_func1: Callable[[int], Tuple[IFuncBlock, int]] = lambda key: (blocks[key], Compressor.__calc_block_size(blocks[key], threshold))
        lambda_func2: Callable[[Tuple[IFuncBlock, int]], bool] = lambda item: item[1] <= threshold and item[0].id not in exclude
        lambda_func3: Callable[[Tuple[IFuncBlock, int]], int] = lambda item: item[1]
        targets = sorted(filter(lambda_func2, map(lambda_func1, blocks.keys())), key=lambda_func3)
        if len(targets) > 0:
            return targets[0][0].id

        return None

    @staticmethod
    def __replace_if_block(block_id: int, block: INextBlock, replace: IFuncBlock) -> bool:
        edited = False
        if type(block.next1) is int:
            next_id = cast(int, block.next1)
            if block_id != next_id and next_id == replace.id:
                block.actions1.extend(replace.actions)
                block.next1 = replace.next
                edited = True
        else:
            next_block = cast(INextBlock, block.next1)
            if block != next_block:
                edited = Compressor.__replace_if_block(block_id, next_block, replace) or edited

        if type(block.next2) is int:
            next_id = cast(int, block.next2)
            if block_id != next_id and next_id == replace.id:
                block.actions2.extend(replace.actions)
                block.next2 = replace.next
                edited = True
        else:
            next_block = cast(INextBlock, block.next2)
            if block != next_block:
                edited = Compressor.__replace_if_block(block_id, next_block, replace) or edited

        return edited

    @staticmethod
    def __replace_block(block_id: int, block: IFuncBlock, replace: IFuncBlock) -> bool:
        if type(block.next) is int:
            next_id = cast(int, block.next)
            if next_id == block_id:
                return False

            if next_id == replace.id:
                block.actions.extend(replace.actions)
                block.next = replace.next
                return True
        else:
            next_block = cast(INextBlock, block.next)
            return Compressor.__replace_if_block(block_id, next_block, replace)

        return False

    @staticmethod
    def __replace_small_blocks(blocks: MutableMapping[int, IFuncBlock], threshold: int) -> None:
        exclude: MutableMapping[int, bool] = {}
        lambda_func: Callable[[int], bool] = lambda next_id: next_id in next_ids
        while True:
            target_key = Compressor.__get_replace_target_key(blocks, threshold, exclude)
            if target_key is None:
                break

            exclude[target_key] = True
            target_next_ids: MutableMapping[int, int] = {}
            Compressor.__get_all_if_next_ids(blocks[target_key].next, target_next_ids)

            for key in blocks.keys():
                if key == target_key:
                    continue

                next_ids: MutableMapping[int, int] = {}
                Compressor.__get_all_if_next_ids(blocks[key].next, next_ids)

                filtered = list(filter(lambda_func, target_next_ids))
                if not filtered:
                    Compressor.__replace_block(blocks[key].id, blocks[key], blocks[target_key])

    @staticmethod
    def __get_all_if_next_ids(block: Union[INextBlock, int], next_ids: MutableMapping[int, int]) -> None:
        if type(block) is int:
            block = cast(int, block)
            next_ids[block] = block
            return

        block = cast(INextBlock, block)
        if block != block.next1:
            Compressor.__get_all_if_next_ids(block.next1, next_ids)
        if block != block.next2:
            Compressor.__get_all_if_next_ids(block.next2, next_ids)

    @staticmethod
    def __get_all_next_ids(start: int, blocks: MutableMapping[int, IFuncBlock]) -> Iterable[int]:
        next_ids = {start: start}
        for block in blocks.values():
            Compressor.__get_all_if_next_ids(block.next, next_ids)

        return next_ids.values()

    @staticmethod
    def __remove_unused_block(start: int, blocks: MutableMapping[int, IFuncBlock]) -> None:
        next_ids = Compressor.__get_all_next_ids(start, blocks)
        while True:
            deleted = False
            for key in list(blocks.keys()):
                if blocks[key].id not in next_ids:
                    del blocks[key]
                    deleted = True
            if not deleted:
                break
