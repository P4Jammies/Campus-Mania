import arcade
from numpy.lib.index_tricks import IndexExpression
from vector import Vector2
from constants import *
import numpy as np

class Node(object):
    def __init__(self, x, y):
        self.position = Vector2(x, y)
        self.neighbors = {UP:None, RIGHT:None, DOWN:None, LEFT:None, PORTAL:None}

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
        self.level1()

    def render(self):
        for node in self.nodeList:
            node.render()

    def getStartNode(self):
        return self.nodeList[0]

    def InitNodes(self):
        self.level1()

    def InitTestNodes(self):
        nodeA = Node(0, 0)
        nodeB = Node(5, 0)
        nodeC = Node(0, 5)
        nodeD = Node(5, 5)
        nodeE = Node(7, 5)
        nodeF = Node(0, 10)
        nodeG = Node(7, 10)
        nodeA.neighbor(RIGHT, nodeB)
        nodeA.neighbor(UP, nodeC)
        nodeB.neighbor(UP, nodeD)
        nodeC.neighbor(RIGHT, nodeD)
        nodeC.neighbor(UP, nodeF)
        nodeD.neighbor(RIGHT, nodeE)
        nodeE.neighbor(UP, nodeG)
        nodeF.neighbor(RIGHT, nodeG)
        self.nodeList = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG]

    def level1(self):
        LDLD = Node(0, 0)
        LDLU = Node(0, 2)
        LDRD = Node(5, 0)
        LDRU = Node(5, 2)
        LDML = Node(1, 2)
        LDMR = Node(3, 2)
        LDLD.neighbor(UP, LDLU)
        LDLD.neighbor(RIGHT, LDRD)
        LDRD.neighbor(UP, LDRU)
        LDLU.neighbor(RIGHT, LDML)
        LDML.neighbor(RIGHT, LDMR)
        LDMR.neighbor(RIGHT, LDRU)
        LULU = Node(0, 8)
        LULD = Node(0, 6)
        LURU = Node(5, 8)
        LURD = Node(5, 6)
        LUML = Node(1, 6)
        LUMR = Node(3, 6)
        LULU.neighbor(DOWN, LULD)
        LULU.neighbor(RIGHT, LURU)
        LURU.neighbor(DOWN, LURD)
        LULD.neighbor(RIGHT, LUML)
        LUML.neighbor(RIGHT, LUMR)
        LUMR.neighbor(RIGHT, LURD)
        LML = Node(1, 4)
        LMRU = Node(5, 5)
        LMRD = Node(5, 3)
        LML.neighbor(UP, LUML)
        LML.neighbor(DOWN, LDML)
        LUMR.neighbor(DOWN, LDMR)
        LMRU.neighbor(UP, LURD)
        LMRU.neighbor(DOWN, LMRD)
        LMRD.neighbor(DOWN, LDRU)
        RDRD = Node(16, 0)
        RDRU = Node(16, 2)
        RDLD = Node(11, 0)
        RDLU = Node(11, 2)
        RDMR = Node(15, 2)
        RDML = Node(13, 2)
        RDRD.neighbor(UP, RDRU)
        RDRD.neighbor(LEFT, RDLD)
        RDLD.neighbor(UP, RDLU)
        RDRU.neighbor(LEFT, RDMR)
        RDMR.neighbor(LEFT, RDML)
        RDML.neighbor(LEFT, RDLU)
        RURU = Node(16, 8)
        RURD = Node(16, 6)
        RULU = Node(11, 8)
        RULD = Node(11, 6)
        RUMR = Node(15, 6)
        RUML = Node(13, 6)
        RURU.neighbor(DOWN, RURD)
        RURU.neighbor(LEFT, RULU)
        RULU.neighbor(DOWN, RULD)
        RURD.neighbor(LEFT, RUMR)
        RUMR.neighbor(LEFT, RUML)
        RUML.neighbor(LEFT, RULD)
        RMR = Node(15, 4)
        RMLU = Node(11, 5)
        RMLD = Node(11, 3)
        RMR.neighbor(UP, RUMR)
        RMR.neighbor(DOWN, RDMR)
        RUML.neighbor(DOWN, RDML)
        RMLU.neighbor(UP, RULD)
        RMLU.neighbor(DOWN, RMLD)
        RMLD.neighbor(DOWN, RDLU)
        MDLD = Node(7, 0)
        MDLU = Node(7, 2)
        MDRD = Node(9, 0)
        MDRU = Node(9, 2)
        MDLD.neighbor(UP, MDLU)
        MDLD.neighbor(RIGHT, MDRD)
        MDRD.neighbor(UP, MDRU)
        MDLU.neighbor(RIGHT, MDRU)
        MULD = Node(7, 6)
        MULU = Node(7, 8)
        MURD = Node(9, 6)
        MURU = Node(9, 8)
        MULD.neighbor(UP, MULU)
        MULD.neighbor(RIGHT, MURD)
        MURD.neighbor(UP, MURU)
        MULU.neighbor(RIGHT, MURU)
        MLD = Node(7, 3)
        MLU = Node(7, 5)
        MRD = Node(9, 3)
        MRU = Node(9, 5)
        MLD.neighbor(LEFT, LMRD)
        MLD.neighbor(DOWN, MDLU)
        MLD.neighbor(UP, MLU)
        MLU.neighbor(LEFT, LMRU)
        MLU.neighbor(UP, MULD)
        MRD.neighbor(RIGHT, RMLD)
        MRD.neighbor(DOWN, MDRU)
        MRD.neighbor(UP, MRU)
        MRU.neighbor(RIGHT, RMLU)
        MRU.neighbor(UP, MURD)
        self.nodeList = [
            LULU,             LURU, MULU, MURU, RULU,             RURU,
            LULD, LUML, LUMR, LURD, MULD, MURD, RULD, RUML, RUMR, RURD,
                              LMRU,  MLU,  MRU, RMLU,
                   LML,                                      RMR,
                              LMRD,  MLD,  MRD, RMLD,
            LDLU, LDML, LDMR, LDRU, MDLU, MDRU, RDLU, RDML, RDMR, RDRU,
            LDLD,             LDRD, MDLD, MDRD, RDLD,             RDRD
        ]
