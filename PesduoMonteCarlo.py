import matplotlib.pyplot as plt
import random

PointsInShape = 0
PointsOutofShape = 0
plt.axes()
line = plt.Line2D((0,20), (0,20), lw=1.25)
plt.gca().add_line(line)
shape = plt.Rectangle((0,0), 20, 20, fc='black', ec='white')
plt.gca().add_patch(shape)
plt.axis('scaled')

def BelowORAbove(x, y):
    equationY = 1*(x) + 0
    if equationY > y:
        global PointsInShape
        PointsInShape += 1
        print("Plotted below")
        plt.plot(x, y, 'go')
    else:
        global PointsOutofShape
        PointsOutofShape += 1
        print("Plotted above")
        plt.plot(x, y, 'yo')


def ComputeRatio():
    '''Ratio --> Take the points in shape/Total Points'''
    TotalPoints = PointsInShape + PointsOutofShape
    return print(PointsInShape/TotalPoints)

x = 0
num_samples = 50
while x in range(num_samples):
    randomY = random.randint(0,20)
    randomX = random.randint(0,20)
    BelowORAbove(randomX, randomY)
    x = x + 1

ComputeRatio()
plt.show()
