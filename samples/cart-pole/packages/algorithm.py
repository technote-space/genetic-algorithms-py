class Algorithm:
    def __init__(self, context):
        self.__context = context

    def start(self):
        self.__func31()

    def __func31(self):
        self.__context.action(0)
        if self.__context.perception(2):
            if self.__context.perception(0):
                return self.__func6()

            self.__context.action(1)
            return self.__func30()

        if self.__context.perception(1):
            return self.__func39()

        return self.__func7()

    def __func7(self):
        if self.__context.perception(3):
            self.__context.action(0)
            return self.__func30()

        return self.__func47()

    def __func47(self):
        self.__context.action(1)
        if self.__context.perception(2):
            if self.__context.perception(1):
                return self.__func3()

            if self.__context.perception(1):
                if self.__context.perception(1):
                    return self.__func38()

                return self.__func14()

            return self.__func27()

        return self.__func30()

    def __func30(self):
        if self.__context.perception(0):
            self.__context.action(1)
            return self.__func35()

        if self.__context.perception(2):
            return self.__func7()

        return self.__func50()

    def __func50(self):
        while True:
            if self.__context.perception(3):
                self.__context.action(0)
                continue

            self.__context.action(1)
            break

        return self.__func35()

    def __func35(self):
        if self.__context.perception(0):
            if self.__context.perception(2):
                if self.__context.perception(0):
                    return self.__func6()

                self.__context.action(1)
                return self.__func30()

            if self.__context.perception(1):
                return self.__func39()

            return self.__func7()

        self.__context.action(1)
        return self.__func47()

    def __func27(self):
        if self.__context.perception(0):
            if self.__context.perception(2):
                return self.__func7()

            return self.__func50()

        self.__context.action(0)
        return self.__func30()

    def __func14(self):
        if self.__context.perception(1):
            self.__context.action(0)
            return self.__func30()

        if self.__context.perception(2):
            if self.__context.perception(2):
                self.__context.action(0)
                return self.__func50()

            return self.__func12()

        return self.__func23()

    def __func23(self):
        if self.__context.perception(3):
            return self.__func35()

        if self.__context.perception(1):
            return self.__func3()

        if self.__context.perception(1):
            if self.__context.perception(1):
                return self.__func38()

            return self.__func14()

        return self.__func27()

    def __func12(self):
        if self.__context.perception(2):
            if self.__context.perception(2):
                return self.__func7()

            return self.__func50()

        self.__context.action(1)
        if self.__context.perception(1):
            return self.__func3()

        if self.__context.perception(1):
            if self.__context.perception(1):
                return self.__func38()

            return self.__func14()

        return self.__func27()

    def __func38(self):
        if self.__context.perception(2):
            self.__context.action(1)
            return self.__func35()

        if self.__context.perception(2):
            if self.__context.perception(0):
                return self.__func6()

            self.__context.action(1)
            return self.__func30()

        if self.__context.perception(1):
            return self.__func39()

        return self.__func7()

    def __func3(self):
        if self.__context.perception(1):
            return self.__func6()

        if self.__context.perception(1):
            if self.__context.perception(1):
                return self.__func38()

            return self.__func14()

        return self.__func27()

    def __func6(self):
        while True:
            if self.__context.perception(2):
                self.__context.action(0)
                break

            if self.__context.perception(2):
                if self.__context.perception(0):
                    continue

                self.__context.action(1)
                return self.__func30()

            if self.__context.perception(1):
                return self.__func39()

            return self.__func7()

        return self.__func2()

    def __func2(self):
        if self.__context.perception(3):
            if self.__context.perception(3):
                self.__context.action(0)
                return self.__func34()

            return self.__func39()

        self.__context.action(0)
        return self.__func30()

    def __func39(self):
        if self.__context.perception(3):
            self.__context.action(0)
            return self.__func30()

        return self.__func12()

    def __func34(self):
        if self.__context.perception(0):
            self.__context.action(0)
            return self.__func2()

        if self.__context.perception(3):
            if self.__context.perception(0):
                return self.__func48()

            return self.__func14()

        return self.__func3()

    def __func48(self):
        while True:
            if self.__context.perception(2):
                continue

            self.__context.action(1)
            if self.__context.perception(1):
                break

            if self.__context.perception(1):
                if self.__context.perception(1):
                    return self.__func38()

                return self.__func14()

            return self.__func27()

        return self.__func3()
