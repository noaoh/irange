class irange:
    def __init__(self, *args):
        if len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]

        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1

        else:
            self.start = 0
            self.stop = args[0]
            self.step = 1

    def __iter__(self):
        return irange_iter(self.start, self.stop, self.step)


class irange_iter:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            old_start = self.start
            self.start += self.step
            return old_start

        else:
            raise StopIteration()

