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

        elif start_and_stop:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1

        elif just_stop:
            self.start = 0
            self.stop = args[0]
            self.step = 1

        if self.step == 0:
            raise ValueError("irange() arg 3 must not be zero")


    def __iter__(self):
        no_values = None

        if self.start == self.stop:
            return no_values

        if self.start > self.stop and self.step > 0:
            return no_values

        elif self.start < self.stop and self.step < 0:
            return no_values

        while self.start != self.stop:
            yield self.start
            self.start += self.step

        yield self.stop

