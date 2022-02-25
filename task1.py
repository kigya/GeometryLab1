import matplotlib.pyplot as plt
import numpy
import random
from Point import Point

p0 = Point(random.randint(0, 10), random.randint(0, 10))
p1 = Point(random.randint(0, 10), random.randint(0, 10))
p2 = Point(random.randint(0, 10), random.randint(0, 10))

def getMatrix(p0: Point, p1: Point, p2: Point):
    return [[p2.x - p1.x, p2.y - p1.y], [p0.x - p1.x, p0.y - p1.y]]


def getPointPosition(matrix: list) -> str:
    d = numpy.linalg.det(matrix)
    if d > 0:
        return 'left'
    elif d < 0:
        return 'right'
    else:
        return 'on the line'

def drawLine(p1: Point, p2: Point):
    arrowprops = {
        'arrowstyle': '<|-',
    }
    plt.annotate('',
                 xy=(p1.x, p1.y),
                 xytext=(p2.x, p2.y),
                 arrowprops=arrowprops)


def drawPoint(p0: Point):
    plt.scatter(p0.x, p0.y, color='red')


def drawText(text: str, p0: Point, p1: Point, p2: Point):
    plt.suptitle(text, fontsize=14)
    plt.text(p0.x, p0.y + 0.05, 'P0')
    plt.text(p1.x, p1.y + 0.05, 'P1')
    plt.text(p2.x, p2.y + 0.05, 'P2')


def draw(p0: Point, p1: Point, p2: Point):
    plt.grid(True)  # линии вспомогательной сетки
    drawLine(p1, p2)
    drawLine(p1, p0)
    drawPoint(p0)
    drawPoint(p1)
    drawPoint(p2)
    drawText(getPointPosition(getMatrix(p0, p1, p2)), p0, p1, p2)
    plt.show()


draw(p0, p1, p2)
