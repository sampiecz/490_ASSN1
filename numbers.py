class NumberContainer:
    numbers = []

    def add_number(self, number):
        self.numbers.append(number)


class Number:
    lines = []
    size = 0

    def __init__(self, lines):
        self.lines = lines

    def print_self(self):
        for line in self.lines:
            print(line)


# Try out the classes / read data
testimages = open("testimages")
numberContainer = NumberContainer()
number = []
count = 0

for line in testimages.read().split("\n"):
    if count <= 27:
        number.append(line)
        count += 1
    else:
        instance = Number(number)
        numberContainer.add_number(instance)
        number = []
        count = 1

numberContainer.numbers[-1].print_self()
