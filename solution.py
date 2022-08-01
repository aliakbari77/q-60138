from math import pi
from multiprocessing.sharedctypes import Value
from turtle import pos


class Piece:
    def __init__(self, sort: chr, color: str, position: tuple) -> None:
        self.sort = sort
        self.color = color
        self.position = position
    
class Board:
    def __init__(self) -> None:
        kingWhite = Piece("K", "white", (-10, -10))
        kingBlack = Piece("K", "black", (10, 10))
        
        self.position = {
            "KW": kingWhite,
            "KB": kingBlack
            }
        
    def add(self, piece: Piece):
        if (piece.sort == "K"):
            print("invalid query")
            return

        for i in self.position:
            if (self.position[i].position == piece.position):
                print("invalid query")
                return
        
        key = piece.sort + piece.color[0] + str(piece.position[0]) + str(piece.position[1])
        
        self.position.update({
            key: piece
        })

        for i in self.position:
            print(i, self.position[i].sort + self.position[i].color + str(self.position[i].position))

    def remove(self, position):
        for i in self.position:
            if (self.position[i].position == position):
                if (self.position[i].sort == "K"):
                    print("invalid query")
                    return
                del self.position[i]
                
    def move(self, piece: Piece, position):
        key = piece.sort + piece.color[0] + str(piece.position[0]) + str(piece.position[1])

        if (self.position[key].position != piece.position):
            print("invalid query")
            return

        # check cell filled or not
        for i in self.position:
            if (self.position[i].position == position):
                if (self.position[i].sort == "K"):
                    print("invalid query")
                    return
                del self.position[i]
                self.position.update({key: piece})
                return

        # empty cell
        self.position.update({key: piece})
            
    def isMate(self, color):
        currentPosition = ()
        if (color == "white"):
            currentPosition = self.position["KW"].position
        if (color == "black"):
            currentPosition = self.position["KB"].position
        
        self.checkAroundCell(currentPosition)
    
    def checkAroundCell(self, position):
        pass
        

s = Piece("P", "white", (10, 10))
b = Board()
b.add(s)