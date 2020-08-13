import pygame

pygame.init()

row = 10
col = 10

class Node():
    def __init__(self, posx: int, posy: int, next):
        self.posx = posx
        self.posy = posy
        self.next = next

class Board():
    def __init__(self):
        self.board = [([0] * col)] * row
        self.board[row/2][col/2] = 1

class Move():
    def __init__(self, vx: int, vy: int):
        self.vx = vx
        self.vy = vy

UP = Move(0,-1)
DOWN = Move(0,1)
RIGHT = Move(1,0)
LEFT = Move(-1,0)

class Snake():
    def __init__(self, first: Node):
        self.first = first

    def move(self, direction: Move, growing: bool):
        first = self.first
        if direction != None:
            posx = direction.vx + first.posx
            posy = direction.vy + first.posy
            node = Node(posx,posy,first)
            self.first = node
            if not growing:
                while(node.next.next != None):
                    node = node.next
                node.next = None
