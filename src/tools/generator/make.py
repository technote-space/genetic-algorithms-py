import shutil
import os
from functools import reduce
from .compressor import Compressor
from .classes import Algorithm, App, Context, Finished, Runner, Package


class Make:
    """
    Description:
    ------------
    生成クラス
    """

    def __init__(self, directory):
        self.__directory = directory

    def generate(self, _algorithm, target, genotype):
        settings = target.settings
        if settings.gym_id:
            save_directory = os.path.join(os.getcwd(), self.__directory)
            if os.path.exists(save_directory):
                shutil.rmtree(save_directory)
            os.makedirs(os.path.join(save_directory, 'packages'))
            blocks = genotype.phenotype.get_programming(target)
            self.__make(target, blocks, settings.gym_id, settings.fps, settings.action_limit, settings.step_limit, settings.action_number, settings.perception_number)

    def __make(self, target, blocks, gym_id, fps, action_limit, step_limit, action_number, perception_number):
        start = blocks[0]["next"]
        lines = reduce(lambda a, b: a + b, map(lambda block: Make.__block_to_function(block), Compressor.compress(blocks, start)))

        for maker in [
            Algorithm(self.__directory, lines, start),
            App(self.__directory),
            Context(self.__directory, target, fps, gym_id, action_limit, step_limit, action_number, perception_number),
            Finished(self.__directory),
            Runner(self.__directory, step_limit),
            Package(self.__directory),
        ]:
            maker.make()

    @staticmethod
    def __contains_self(block_id, next_id):
        if type(next_id) is int:
            return block_id == next_id
        return (next_id != next_id["next1"] and Make.__contains_self(block_id, next_id["next1"])) or \
               (next_id != next_id["next2"] and Make.__contains_self(block_id, next_id["next2"]))

    @staticmethod
    def __get_first_id(block_id, next_id):
        if type(next_id) is int:
            if next_id >= 0 and next_id != block_id:
                return next_id
            return None

        first_id = Make.__get_first_id(block_id, next_id["next1"])
        if first_id is None:
            first_id = Make.__get_first_id(block_id, next_id["next2"])
        return first_id

    @staticmethod
    def __parse_next(next_id, block_id, nested, break_id=None):
        if type(next_id) is int:
            if block_id is None or block_id != next_id:
                if break_id == next_id:
                    return ['break']
                return [f'return self.__func{next_id}()']

            if nested > 0:
                return ['continue']
            return []

        return Make.__parse_if_block(next_id, block_id, nested + 1, break_id)

    @staticmethod
    def __get_if_statement(block, actions1, actions2):
        deny_expression = ''
        if not actions1:
            deny_expression = 'not '
            actions1 = actions2
            actions2 = None
        if not actions2:
            return [f'if {deny_expression}{block["perception"]}:', '{'] + actions1 + ['}']
        return [f'if {block["perception"]}:', '{'] + actions1 + ['}', 'else:', '{'] + actions2 + ['}']

    @staticmethod
    def __parse_if_block(block, block_id, nested, break_id):
        same1 = []
        same2 = []

        n1 = 0
        n2 = 0
        len1 = len(block["actions1"])
        len2 = len(block["actions2"])
        while n1 < len1 and n2 < len2:
            if block["actions1"][n1] != block["actions2"]:
                break
            same1.append(block["actions1"][n1])
            n1 += 1
        while n2 - len1 - n1 and n2 < len2 - n1:
            if block["actions1"][len1 - 1 - n2] != block["actions2"][len2 - 1 - n2]:
                break
            same2.append(block["actions1"][len1 - 1 - n2])
            n2 += 1

        next1 = Make.__parse_next(block["next1"], block_id, nested, break_id)
        next2 = Make.__parse_next(block["next2"], block_id, nested, break_id)
        if '\n'.join(next1) == '\n'.join(next2):
            s1 = n1 == len1 - n2
            s2 = n1 == len2 - n2
            if s1 and s2:
                return same1 + list(reversed(same2)) + next1
            if s1:
                return same1 + Make.__get_if_statement(block, None, block["actions2"][n1: len2 - n2]) + list(reversed(same2)) + next1
            if s2:
                return same1 + Make.__get_if_statement(block, block["actions1"][n1: len1 - n2], None) + list(reversed(same2)) + next1
            return same1 + Make.__get_if_statement(block, block["actions1"][n1: len1 - n2], block["actions2"][n1: len2 - n2]) + list(reversed(same2)) + next1

        return same1 + Make.__get_if_statement(block, block["actions1"][n1:] + next1, None) + block["actions2"][n1:] + next2

    @staticmethod
    def __block_to_function(block):
        if Make.__contains_self(block["id"], block["next"]):
            first_id = Make.__get_first_id(block["id"], block["next"])
            next_block = Make.__parse_next(block["next"], block["id"], 0, first_id)
            if not next_block:
                return [
                           f'def __func{block["id"]}(self):',
                           '{',
                           'while True:',
                           '{',
                       ] + block["actions"] + [
                           '}',
                           '}',
                       ]

            length = len(next_block) - 1 if next_block[len(next_block) - 1] == 'continue' else len(next_block)
            block1 = [
                f'def __func{block["id"]}(self):',
                '{',
                'while True:',
                '{',
            ]
            block2 = block["actions"] + next_block[0:length]
            block3 = [
                '}',
            ]
            block4 = [] if first_id is None or first_id == block["id"] else [
                f'return self.__func{first_id}()',
            ]
            block5 = [
                '}',
            ]
            return block1 + block2 + block3 + block4 + block5

        block1 = [
            f'def __func{block["id"]}(self):',
            '{',
        ]
        block2 = block["actions"] + Make.__parse_next(block["next"], None, 5)
        block3 = [
            '}',
        ]
        return block1 + block2 + block3
