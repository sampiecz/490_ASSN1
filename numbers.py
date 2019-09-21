import pprint

class NumberContainer:
    numbers = []
    timesNumberHasAppeared = {0: 0,1: 0,2: 0,3: 0,4: 0,5: 0,6: 0,7: 0,8: 0,9: 0,}

    def __str__(self):
        stringThing = ""
        for item in self.numbers:
            stringThing += str(item)
        return stringThing 

    def addNumber(self, number):
        self.numbers.append(number)

    def printSize(self):
        print("This many images in container: " + str(len(self.numbers)))

    def countNumbers(self):
        for number in self.numbers:
            self.timesNumberHasAppeared[int(number.label)] += 1
        print(self.timesNumberHasAppeared)

class Number:
    label = ""
    lines = []
    features = {}
    size = 0
    # TODO: calculate the probability of each feature

    def __str__(self):
        stringThing = ""
        for item in self.lines:
            stringThing += str(item)
        return stringThing 

    def __init__(self, lines):
        self.lines = lines

    def printSelf(self):
        for line in self.lines:
            print(line)
        print("I am: " + str(self.label))
        print("Size: " + str(len(self.features)))

    def generateFeatures(self):
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

class WeightContainer:
    weights = []

    def addWeight(self, weight):
        self.weights.append(weight)

    def incrementWeight(self, label, featureNum):
        for weight in self.weights:
            if weight.label == label:
                weight.features[featureNum] += 1

    def generateWeights(self, numberContainer):
        for weight in self.weights:
            newWeightFeatures = {} 
            for weightNum, weightVal in weight.features.items(): 
                indexWeightNum = weightNum -1
                timesNumOccured = numberContainer.timesNumberHasAppeared[int(weight.label)]  
                newVal = weightVal / (2 *.1 + timesNumOccured)
        weight.features = newWeightFeatures 

    def printWeights(self):
        for weight in self.weights:
            weight.printSelf()


class Weight:
    label = ""
    features = {}

    def __str__(self):
        return self.features

    def __init__(self, label):
        self.label = str(label)

        # make sure weights isn't empty -- initialize with counters and zeros
        count = 1
        while count != 785:
            self.features.update({count: 0.1})
            count += 1

    def printSelf(self): 
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.features)

def main():

    
    # read those test numbers and store them
    numberContainer = NumberContainer()
    number = []
    count = 0
    for line in open("testimages").read().split("\n"):
        if count <= 27:
            number.append(line)
            count += 1
        else:
            instance = Number(number)
            instance.generateFeatures()
            numberContainer.addNumber(instance)
            number = []
            number.append(line)
            count = 1

    # do label stuff
    labelCounter = 0
    testlabel = open("testlabels")
    for label in testlabel:
        numberContainer.numbers[labelCounter].label = label
        labelCounter += 1

    # now numbers are labeled we can count occurences
    numberContainer.countNumbers()

    # initialize weights and weight container
    weightContainer = WeightContainer()
    for item in range(0, 9):
        weight = Weight(item)
        weightContainer.addWeight(weight)

    # generate number count
    numberContainer.countNumbers()
    
    # loop through numbers, then loop through their features, for each feature, if it 
    # is a 1, then we need to let weights know to increment current value at that index in weights grid
    for number in numberContainer.numbers:
        for featureNum, featureVal in number.features.items():
            if featureVal == 1:
                weightContainer.incrementWeight(number.label, featureNum)

    # I need to replace the values in the weights, with the weights divided by the
    # timesNumberHasAppeared
    # timesNumberHasAppeared = {0: {},1: {},2: {},3: {},4: {},5: {},6: {},7: {},8: {},9: {},}
    weightContainer.generateWeights(numberContainer)
    weightContainer.printWeights()


# check stuff with printing
#numberContainer.numbers[0].printSelf()
#numberContainer.numbers[0].generateFeatures()
#print(numberContainer.numbers[0].features)
#print(numberContainer.numbers[0].label)

if __name__ == "__main__":
    main()
