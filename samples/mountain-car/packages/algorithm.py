class Algorithm:
    def __init__(self, context):
        self.__context = context

    def start(self):
        self.__func38()

    def __func38(self):
        if self.__context.perception(5):
            return self.__func6()

        if self.__context.perception(0):
            if self.__context.perception(6):
                return self.__func22()

            return self.__func33()

        return self.__func24()

    def __func24(self):
        while True:
            if self.__context.perception(0):
                if self.__context.perception(8):
                    break

                if self.__context.perception(3):
                    return self.__func33()

                if self.__context.perception(6):
                    continue

                return self.__func25()

            self.__context.action(0)
            self.__context.action(0)
            self.__context.action(0)
            if self.__context.perception(6):
                return self.__func48()

            return self.__func33()

        return self.__func45()

    def __func42(self):
        if self.__context.perception(6):
            return self.__func48()

        return self.__func33()

    def __func33(self):
        while True:
            if self.__context.perception(7):
                self.__context.action(0)
                self.__context.action(0)
                self.__context.action(0)
                break

            self.__context.action(2)
            self.__context.action(2)
            self.__context.action(2)
            self.__context.action(2)

        return self.__func42()

    def __func48(self):
        if self.__context.perception(7):
            if self.__context.perception(6):
                return self.__func24()

            return self.__func25()

        self.__context.action(2)
        self.__context.action(2)
        self.__context.action(2)
        self.__context.action(2)
        return self.__func33()

    def __func6(self):
        if self.__context.perception(6):
            return self.__func24()

        return self.__func25()

    def __func25(self):
        while True:
            if self.__context.perception(7):
                if self.__context.perception(6):
                    break

                continue

            if self.__context.perception(7):
                if self.__context.perception(3):
                    return self.__func33()

                if self.__context.perception(6):
                    break

                continue

            return self.__func27()

        return self.__func24()

    def __func27(self):
        if self.__context.perception(4):
            self.__context.action(0)
            return self.__func47()

        self.__context.action(2)
        self.__context.action(2)
        return self.__func33()

    def __func47(self):
        if self.__context.perception(1):
            self.__context.action(1)
            self.__context.action(2)
            if self.__context.perception(6):
                return self.__func22()

            return self.__func33()

        return self.__func27()

    def __func50(self):
        if self.__context.perception(6):
            return self.__func22()

        return self.__func33()

    def __func22(self):
        while True:
            if self.__context.perception(0):
                break

            if self.__context.perception(6):
                continue

            return self.__func33()

        return self.__func3()

    def __func3(self):
        if self.__context.perception(5):
            if self.__context.perception(0):
                if self.__context.perception(6):
                    return self.__func22()

                return self.__func33()

            return self.__func24()

        return self.__func19()

    def __func19(self):
        if self.__context.perception(4):
            self.__context.action(2)
            return self.__func33()

        return self.__func50()

    def __func45(self):
        if self.__context.perception(0):
            self.__context.action(2)
            self.__context.action(2)
            return self.__func33()

        return self.__func2()

    def __func2(self):
        if self.__context.perception(2):
            self.__context.action(0)
            if self.__context.perception(6):
                return self.__func48()

            return self.__func33()

        return self.__func19()
