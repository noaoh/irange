class irange:
    def __init__(self, *args):
        if len(args) == 0:
            raise TypeError("irange expected 1 arguments, got 0")

        elif len(args) > 3:
            raise TypeError(
                "irange expected at most 3 arguments got {l}"
                .format(l=len(args))
            )

        for x in args:
            if type(x) != int:
                raise TypeError(
                    "'{type_name}' object cannot be interpreted as an integer"
                    .format(type_name=type(x).__name__)
                )

        start_stop_and_step = len(args) == 3
        start_and_stop = len(args) == 2
        just_stop = len(args) == 1

        if start_stop_and_step:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
            if self.step == 0:
                raise ValueError("irange() arg 3 must not be zero")

        elif start_and_stop:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1

        elif just_stop:
            self.start = 0
            self.stop = args[0]
            self.step = 1

    def __iter__(self):
        no_values = None

        if not bool(self):
            return no_values

        value = self.start
        if self.start > self.stop:
            while value > self.stop:
                yield value
                value += self.step

        elif self.start < self.stop:
            while value < self.stop:
                yield value
                value += self.step

        if abs(self.stop - self.start) % abs(self.step) == 0:
            yield self.stop

    def __repr__(self):
        if self.step == 1:
            return (
                'irange({start}, {stop})'
                .format(start=self.start, stop=self.stop)
            )

        else:
            return (
                'irange({start}, {stop}, {step})'
                .format(start=self.start, stop=self.stop, step=self.step)
            )

    def __bool__(self):
        return not ((self.start == self.stop) or
                    (self.start > self.stop and self.step > 0) or
                    (self.start < self.stop and self.step < 0))

