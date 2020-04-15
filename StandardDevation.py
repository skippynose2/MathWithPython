import math
data = []

def calculations():
    #Calculate mean code
    mean = sum(data)/len(data)
    print("Your mean is: " + str(mean))
    #calculate standard deviation Code
    stdList = []
    for i in range(len(data)):
        std1 = (data[i] - mean)**2
        stdList.append(std1)
        final = sum(stdList)/len(stdList)
        final = round(math.sqrt(final), 5)
        print(stdList)
    print("Your standard Deviation: " + str(final))


def main():
    acceptable_inputs = ["Done", 'done', 'd', 'D']
    while(1):
        Inputs = input("Enter your number right here one at a time and hit enter, hit D when done")
        if Inputs in acceptable_inputs:
            calculations()
            del data[0:len(data)]
            print("data discarded")
        else:
            data.append(float(Inputs))

if __name__ == "__main__":
    main()
