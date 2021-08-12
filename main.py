from random import randint
from pathfinder import *

path = "assets/maze.png"
size = 10
(gx, gy) = (20 * randint(0, 5), 20 * randint(0, 19))
(rx, ry) = (20 * randint(15, 19), 20 * randint(0, 19))


# Thanks Jvi for the generation spoon feed
def run():
    for x in range(400 // size):
        for y in range(400 // size):
            if 100 // size <= x <= 300 // size:
                Node(Rect(x * size, y * size, size, size, fill='white' if randint(0, 1) == 1 else 'gray'))
            else:
                Node(Rect(x * size, y * size, size, size, fill='white'))

    Node.size = size
    start = Node(Rect(gx, gy, size, size, fill='green'))
    target = Node(Rect(rx, ry, size, size, fill='red'))
    pf = PathFinder(size, target, True)
    pf.open[start.position] = start
    pf.start()


run()