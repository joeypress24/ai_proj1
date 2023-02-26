import random

class Board(object):
    # A board is just a 2-d list, plus a location of the blank, fo easier move generation.

    def __init__(self):
        self.b = [['b', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        self.lb = [0, 0]
        self.totalCost = 1 #stores the f-cost, can be updated in copies
        self.moves=[] #class variable to store list of moves

    #Returns a list of places the blank can be moved to.  Note the use of map and filter.  Good tools for AI
    #programming
    def generateMoves(self):
        delta = [[-1,0],[1,0],[0,-1],[0,1]]
        result = list(map(lambda x: pairAdd(x,self.lb), delta))
        result = list(filter(lambda x: inRange(x), result))
        return result

    #Takes a move location, and actually changes the board.
    def makeMove(self,m):
        # It had better be next to the current location.
        if (manhattan(m,self.lb) > 1):
            raise RuntimeError('Bad move executed on board: ' + str(m) + 'lb: ' + str(self.lb))
        self.b[self.lb[0]][self.lb[1]] = self.b[m[0]][m[1]]
        self.b[m[0]][m[1]] = 'b'
        self.lb = m

    #Mix up the board.
    def scramble(self,n,s=2018):
        random.seed(s)
        for i in range(n):
            moves = self.generateMoves()
            self.makeMove(moves[random.randint(0,len(moves)-1)])

    #are boards equal?
    def __eq__(self,other):
        return self.b == other.b
    def __ne__(self,other):
        return self.b != other.b
    def key(self):
        return str(self.b)
#---------------------------------
#End of Board class


#apply a list of moves to the board.
def applyMoves(board,moveList):
    for m in moveList:
        board.makeMove(m)


#Some utility functions
def pairAdd(a,b):
    return [a[0]+b[0],a[1]+b[1]]

def inRange(p):
    return p[0] >= 0 and p[0] < 4 and p[1] >=0 and p[1] < 4


#The heuristics go here

#returns the # of tiles that are not where they should be
def misplacedTiles(board):
    numTilesMisplaced = 0 #increment this every time we find a tile where it shouldn't be
    if(board.b[0],[0] != 'b'):
        numTilesMisplaced += 1

    i = 1
    while(i <= 15):
        targRow = int(i/4) #divide to get the row
        targCol = i%4 #mod to get the column

        if(i != board.b[targRow][targCol]): #if(bad tile):
            numTilesMisplaced += 1 
        i += 1

    return numTilesMisplaced

#calculates the distance of a board from the goal
def manhattanDistance(board):
    totalDistance = 0
    #loop through each tile on the board
    #nested for loops treats board as a 2-D array
    for r in range(4):
        for c in range(4):
            tileVal = board.b[r][c]
            if(tileVal == 'b'): #check for blank tile
                totalDistance += manhattan((0,0),(r,c))
            else: #not blank tile
                #find where tileVal should be
                #ex: 6 should be at r = 1 c = 2
                #use integer math to find the goal rows and cols
                targRow = int(tileVal/4) #divide to get the row
                targCol = tileVal%4 #mod to get the column
                #compute the manhattan distance and add to total
                totalDistance += manhattan((r,c), (targRow, targCol))
    return totalDistance

# This is not the actual manhattan distance heuristic, but may
# be helpful
def manhattan(a,b):
    #takes two locations on the board and returns the difference
    return abs(a[0]-b[0])+abs(a[1]-b[1])
