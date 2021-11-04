import arcade
from vector import Vector2
from constants import *

class Node(object):
    def __init__(self, x, y):
        self.position = Vector2(x*TILEWIDTH, y*TILEHEIGHT)
        self.neighbors = {UP:None, RIGHT:None, DOWN:None, LEFT:None}

    def render(self):
        start = self.position
        arcade.draw_circle_filled(start.x, start.y, 12, RED)
        for d in self.neighbors.keys():
            if self.neighbors[d] is not None:
                end = self.neighbors[d].position
                arcade.draw_line(start.x, start.y, end.x, end.y, WHITE, 4)

    def neighbor(self, direction, other):
        self.neighbors[direction] = other
        other.neighbors[direction*-1] = self


class NodeGroup(object):
    def __init__(self):
        self.nodeList = []
        self.InitTestNodes()

    def render(self):
        for node in self.nodeList:
            node.render()

    def InitTestNodes(self):
        nodeA = Node(5, 5)
        nodeB = Node(10, 5)
        nodeC = Node(5, 10)
        nodeD = Node(10, 10)
        nodeE = Node(13, 10)
        nodeF = Node(5, 20)
        nodeG = Node(13, 20)
        nodeA.neighbor(RIGHT, nodeB)
        nodeA.neighbor(DOWN, nodeC)
        nodeB.neighbor(DOWN, nodeD)
        nodeC.neighbor(RIGHT, nodeD)
        nodeC.neighbor(DOWN, nodeF)
        nodeD.neighbor(RIGHT, nodeE)
        nodeE.neighbor(DOWN, nodeG)
        nodeF.neighbor(RIGHT, nodeG)
        self.nodeList = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG]
