testimages = open("testimages", "r+")
blank = "                            "
number = False

class NumberContainer:
    numbers = []

    def add_number(self, number):
        self.numbers.append(number)

class Number:
    lines = []
    size = 0

    def __init__(self, lines):
        self.lines = lines

    def add_line(self, line):
        self.lines.append(line)

    def count_grid(self):
        for line in self.lines:
            for character in line:
                self.size += 1
        print(self.size)
                
    def print_self(self):
        for line in self.lines:
            print(line)

numberContainer = NumberContainer()

lines = []
count = 0

for line in testimages.read().split("\n"):
    if count != 28:
        lines.append(line)
        count += 1
    else:
        instance = Number(lines)
        numberContainer.add_number(instance)
        lines = []
        count = 0

numberContainer.numbers[2].print_self()
