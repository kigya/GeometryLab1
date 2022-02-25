import matplotlib.pyplot as plt
import random
from Point import Point


def initPoints(xs: list, ys: list) -> list:
    points = []
    for i in range(len(xs)):
        x = Point(xs[i], ys[i])
        points.append(x)
    return points


def det(a, b, c, d):
    return a * d - b * c


def drawPolygon(points: list):
    for i in range(0, len(points)):
        if i + 1 == len(points):
            lastPointIndex = 0
        else:
            lastPointIndex = i + 1
        plt.scatter(points[i].x, points[i].y, color='red')
        plt.text(points[i].x, points[i].y + 0.05, '{}({},{})'.format(i, points[i].x, points[i].y))
        plt.plot([points[i].x, points[lastPointIndex].x], [points[i].y, points[lastPointIndex].y])


def areIntersect(p1: Point, p2: Point, p3: Point, p4: Point) -> bool:
    d1 = det(p4.x - p3.x, p4.y - p3.y, p1.x - p3.x, p1.y - p3.y)
    d2 = det(p4.x - p3.x, p4.y - p3.y, p2.x - p3.x, p2.y - p3.y)
    d3 = det(p2.x - p1.x, p2.y - p1.y, p3.x - p1.x, p3.y - p1.y)
    d4 = det(p2.x - p1.x, p2.y - p1.y, p4.x - p1.x, p4.y - p1.y)

    if d1 * d2 <= 0 and d3 * d4 <= 0:
        return True
    else:
        return False


def isPolygonSimple(points: list) -> bool:
    for i in range(len(points) - 3):
        for j in range(i + 2, len(points)):
            if j + 1 == len(points):
                lastPointIndex = 0
            else:
                lastPointIndex = j + 1
            if lastPointIndex == i:
                continue
            if areIntersect(points[i], points[i + 1], points[j], points[lastPointIndex]):
                print(f"i: {points[i].x},{points[i].y} , i+1: {points[i + 1].x}, {points[i + 1].y}")
                print(
                    f"j: {points[j].x},{points[j].y} , {lastPointIndex}: {points[lastPointIndex].x}, {points[lastPointIndex].y}")
                return False

    return True


def init():
    plt.grid(True)  # линии вспомогательной сетки
    xs = [random.randint(0, 10) for _ in range(5)]
    ys = [random.randint(0, 10) for _ in range(5)]
    points = initPoints(xs, ys)
    # for i in range(len(points)):
    #    print(points[i].x, ' ::: ', points[i].y)
    drawPolygon(points)
    if isPolygonSimple(points):
        plt.suptitle('Polygon is simple', fontsize=14)
    else:
        plt.suptitle('Polygon is not simple', fontsize=14)
    plt.show()


init()
