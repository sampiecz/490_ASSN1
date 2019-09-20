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
    label = ""
    lines = []
    features = {}
    size = 0
    # TODO: add label to this class
    # TODO: calculate the probability of each feature

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
        for line in self.lines:
            for character in line:
                if character == " ":
                    self.features.update({count: 0})
                elif character == "#":
                    self.features.update({count: 1})
                elif character == "+":
                    self.features.update({count: 1})
                count += 1

    def size(self):
        self.size = len(self.features) 
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

label_counter = 0
testlabel = open("testlabels")
for label in testlabel:
    numberContainer.numbers[label_counter].label = label
    label_counter += 1

numberContainer.numbers[0].print_self()
numberContainer.numbers[0].generate_features()
print(numberContainer.numbers[0].features)
print(numberContainer.numbers[0].label)
