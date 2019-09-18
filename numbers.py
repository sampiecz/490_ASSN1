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

for line in testimages.read().split("\n"):
    if(line == blank):
        number = False
    elif(line != blank and number == False):
        number = True
        new_number = Number()
        new_number.add_line(line)
    elif(line != blank and number == True):
        new_number.add_line(line)
        number = True
    elif(line == blank and number == True):
        numberContainer.numbers.append(new_number)
        number = False

for number in numberContainer.numbers:
    print(count(number.lines))
