class NumberContainer:
    numbers = []

    def __str__(self):
        string_thing = ""
        for item in self.numbers:
            string_thing += str(item)
        return string_thing 

    def add_number(self, number):
        self.numbers.append(number)


class Number:
    lines = []
    features = {}
    size = 0

    def __str__(self):
        string_thing = ""
        for item in self.lines:
            string_thing += str(item)
        return string_thing 

    def __init__(self, lines):
        self.lines = lines

    def print_self(self):
        for line in self.lines:
            print(line)

    def generate_features(self):
        count = 0
        for character in self.lines:
            if character == " ":
                features.update({count: 0})
            elif character == "#":
                features.update({count: 1})
            elif character == "+":
                features.update({count: 1})

    def size(self):
        self.size = len(self.features.items()) 
        return self.size


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
        number.append(line)
        count = 1

numberContainer.numbers[-9].print_self()
