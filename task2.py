import matplotlib.pyplot as plt
import numpy
import random
from Point import Point

point1 = Point(random.randint(0, 10), random.randint(0, 10))
point2 = Point(random.randint(0, 10), random.randint(0, 10))
point3 = Point(random.randint(0, 10), random.randint(0, 10))
point4 = Point(random.randint(0, 10), random.randint(0, 10))


def getMatrix(p1: Point, p2: Point, p3: Point):
    return [[p3.x - p2.x, p3.y - p2.y], [p1.x - p2.x, p1.y - p2.y]]


def areIntersect(matrices: list, p1: Point, p2: Point, p3: Point, p4: Point) -> str:
    d1 = numpy.linalg.det(matrices[0])
    d2 = numpy.linalg.det(matrices[1])
    d3 = numpy.linalg.det(matrices[2])
    d4 = numpy.linalg.det(matrices[3])

    if d1 == d2 == d3 == d4 == 0:
        c1 = (p3.x - p1.x) * (p4.x - p1.x) + (p3.y - p1.y) * (p4.y - p1.y)
        c2 = (p3.x - p2.x) * (p4.x - p2.x) + (p3.y - p2.y) * (p4.y - p2.y)
        c3 = (p1.x - p3.x) * (p2.x - p3.x) + (p1.y - p3.y) * (p2.y - p3.y)
        c4 = (p1.x - p4.x) * (p2.x - p4.x) + (p1.y - p4.y) * (p2.y - p4.y)
        if c1 < 0 or c2 < 0 or c3 < 0 or c4 < 0:
            return 'пересекаются'
    elif d1 * d2 <= 0 and d3 * d4 <= 0:
        return 'пересекаются'
    return 'не пересекаются'


def drawPoint(p0: Point):
    plt.scatter(p0.x, p0.y, color='red')


def drawLine(p1: Point, p2: Point):
    plt.plot([p1.x, p2.x], [p1.y, p2.y])


def drawText(text: str, p1: Point, p2: Point, p3: Point, p4: Point):
    plt.suptitle(text, fontsize=14)
    plt.text(p1.x, p1.y + 0.05, 'P1')
    plt.text(p2.x, p2.y + 0.05, 'P2')
    plt.text(p3.x, p3.y + 0.05, 'P3')
    plt.text(p4.x, p4.y + 0.05, 'P4')


def draw(p1: Point, p2: Point, p3: Point, p4: Point):
    matrices = [getMatrix(p1, p3, p4), getMatrix(p2, p3, p4), getMatrix(p1, p2, p3), getMatrix(p1, p2, p4)]
    plt.grid(True)  # линии вспомогательной сетки
    drawPoint(p1)
    drawPoint(p2)
    drawPoint(p3)
    drawPoint(p4)
    drawLine(p1, p2)
    drawLine(p3, p4)
    drawText(areIntersect(matrices, p1, p2, p3, p4), p1, p2, p3, p4)
    plt.show()


draw(point1, point2, point3, point4)
