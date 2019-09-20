import pprint

class NumberContainer:
    numbers = []

    def __str__(self):
        string_thing = ""
        for item in self.numbers:
            string_thing += str(item)
        return string_thing 

    def add_number(self, number):
        self.numbers.append(number)

    def print_size(self):
        print("This many images in container: " + str(len(self.numbers)))


class Number:
    label = ""
    lines = []
    features = {}
    size = 0
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
        print("I am: " + str(self.label))
        print("Size: " + str(len(self.features)))

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

def main():

# Instantiate vars 
    testimages = open("testimages")
    numberContainer = NumberContainer()
    number = []
    count = 0

# read those test numbers and store them
    for line in testimages.read().split("\n"):
        if count <= 27:
            number.append(line)
            count += 1
        else:
            instance = Number(number)
            instance.generate_features()
            numberContainer.add_number(instance)
            number = []
            number.append(line)
            count = 1

    # do label stuff
    label_counter = 0
    testlabel = open("testlabels")
    for label in testlabel:
        numberContainer.numbers[label_counter].label = label
        label_counter += 1

    # weights
    weights = {0: {},1: {},2: {},3: {},4: {},5: {},6: {},7: {},8: {},9: {},}
    times_number_has_appeared = {0: 0,1: 0,2: 0,3: 0,4: 0,5: 0,6: 0,7: 0,8: 0,9: 0,}

    # make sure weights isn't empty -- initialize with counters and zeros
    for weight in weights.values():
        count = 1
        while count != 785:
            weight.update({count: 0})
            count += 1

    # see how many times each number appears
    for number in numberContainer.numbers:
        times_number_has_appeared[int(number.label)] += 1


    # loop through numbers, then loop through their features, for each feature, if it 
    # is a 1, then we need to let weights know to increment current value at that index in weights grid
    for number in numberContainer.numbers:
        for featureNumber, featureValue in number.features.items():
            if featureValue == 1:
                temp = weights[int(number.label)][featureNumber]
                temp += 1
                weights[int(number.label)].update({featureNumber: temp})
                thing = weights[int(number.label)][featureNumber]


    # I need to replace the values in the weights, with the weights divided by the
    # times_number_has_appeared
    for weightNum, weightContainer in weights.items():
        for featureNum, featureValue in weightContainer.items(): 
            times_num_occured = times_number_has_appeared[weightNum]  
            temp = featureValue / times_num_occured
            weights[int(number.label)].update({featureNumber: temp})

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(weights)

if __name__ == "__main__":
    main()

# check stuff with printing
#numberContainer.numbers[0].print_self()
#numberContainer.numbers[0].generate_features()
#print(numberContainer.numbers[0].features)
#print(numberContainer.numbers[0].label)
