class Compressor:
    """
    Description:
    ------------
    圧縮クラス
    """

    @staticmethod
    def compress(program, start: int, threshold: int = 6):
        blocks = {}
        for block in program:
            blocks[block["id"]] = block

        Compressor.__replace_small_blocks(blocks, threshold)
        Compressor.__remove_unused_block(start, blocks)

        return blocks.values()

    @staticmethod
    def __calc_if_block_size(block, threshold, prev):
        if block["next1"] == block or block["next2"] == block:
            return 10000

        size = len(block["actions1"]) + len(block["actions2"])
        if prev + size > threshold:
            return size
        size += 2 if type(block["next1"]) is int else Compressor.__calc_if_block_size(block["next1"], threshold, prev + size)
        if prev + size > threshold:
            return size
        size += 2 if type(block["next2"]) is int else Compressor.__calc_if_block_size(block["next2"], threshold, prev + size)
        return size

    @staticmethod
    def __calc_block_size(block, threshold):
        return len(block["actions"]) + (1 if type(block["next"]) is int else Compressor.__calc_if_block_size(block["next"], threshold, 0))

    @staticmethod
    def __get_replace_target_key(blocks, threshold, exclude):
        targets = blocks.keys()
        targets = map(lambda key: {**blocks[key], "size": Compressor.__calc_block_size(blocks[key], threshold)}, targets)
        targets = filter(lambda block: block["size"] <= threshold and block["id"] not in exclude, targets)
        targets = sorted(targets, key=lambda block: block["size"])
        if len(targets) > 0:
            return targets[0]["id"]

        return None

    @staticmethod
    def __replace_if_block(block_id, block, replace):
        edited = False
        for index in (1, 2):
            key = f'next{index}'
            if type(block[key]) is int:
                if block_id != block[key] and block[key] == replace["id"]:
                    block[f'actions{index}'].extend(replace["actions"])
                    block[key] = replace["next"]
                    edited = True
            elif block != block[key]:
                edited = Compressor.__replace_if_block(block_id, block[key], replace) or edited

        return edited

    @staticmethod
    def __replace_block(block_id, block, replace):
        if type(block["next"]) is int:
            if block["next"] == block_id:
                return False

            if block["next"] == replace["id"]:
                block["actions"].extend(replace["actions"])
                block["next"] = replace["next"]
                return True
        else:
            return Compressor.__replace_if_block(block_id, block["next"], replace)

        return False

    @staticmethod
    def __replace_small_blocks(blocks, threshold):
        exclude = {}
        while True:
            target_key = Compressor.__get_replace_target_key(blocks, threshold, exclude)
            if target_key is None:
                break

            exclude[target_key] = True
            target_next_ids = {}
            Compressor.__get_all_if_next_ids(blocks[target_key]["next"], target_next_ids)

            for key in blocks.keys():
                if key == target_key:
                    continue

                next_ids = {}
                Compressor.__get_all_if_next_ids(blocks[key]["next"], next_ids)

                filtered = list(filter(lambda next_id: next_id in next_ids, target_next_ids))
                if not filtered:
                    Compressor.__replace_block(blocks[key]["id"], blocks[key], blocks[target_key])

    @staticmethod
    def __get_all_if_next_ids(block, next_ids):
        if type(block) is int:
            next_ids[block] = block
            return

        if block != block["next1"]:
            Compressor.__get_all_if_next_ids(block["next1"], next_ids)
        if block != block["next2"]:
            Compressor.__get_all_if_next_ids(block["next2"], next_ids)

    @staticmethod
    def __get_all_next_ids(start, blocks):
        next_ids = {start: start}
        for block in blocks.values():
            Compressor.__get_all_if_next_ids(block["next"], next_ids)

        return next_ids.values()

    @staticmethod
    def __remove_unused_block(start, blocks):
        next_ids = Compressor.__get_all_next_ids(start, blocks)
        while True:
            deleted = False
            for key in list(blocks.keys()):
                if blocks[key]["id"] not in next_ids:
                    del blocks[key]
                    deleted = True
            if not deleted:
                break
