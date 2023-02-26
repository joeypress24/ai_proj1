from PriQue_p import * # import my custom priority queue
from Board import * 
import copy #only use this for copy.deepcopy(i)

#takes in a scrambled board and a heuristic function
def aStar(initialBoard, heuristic):
    board = initialBoard #keeps track of our progress
    closed = dict() # dictionary is better than list for this purpose
    open = PriQue() # priority queue object to store open nodes
    goal = Board() # goal is always a default board
    totalNodes = 0 # keep track of # of nodes

    while(board.__ne__(goal)): #isNotGoal()
        #generate all possible moves in given state
        #add board to closed

        closed[board.key()] = True
        successors = board.generateMoves()
        #totalNodes += 1 # add to totalNodes when generateMoves() is called

        #loop through the list of generated moves
        for i in successors:
            #make a deep copy of the board
            child = copy.deepcopy(board)
            child.moves.append(i)
            child.makeMove(i) #make the move

            #calc the f-cost and store in child
            # length of moves[] in child == CURRENT DEPTH
            totalCost = len(child.moves) + heuristic(child)
            child.totalCost = totalCost

            if(child.key() not in closed):
                #add successors to open priority queue
                open.insert(child)
                #totalNodes+=1

        board = open.dequeue() #get the next (lowest cost) board

    #once finished, we need to return moves arr and # nodes
    #print("Nodes expanded: ", totalNodes)
    return (board.moves, totalNodes)


#*********** PSEUDOCODE FROM LECTURE **************
# note, for the pseudocode of A*, I got it from the lecture video 
# https://www.youtube.com/watch?v=j2gzK-KOMdk

# A*(Startstate)
#     while(isNotGoal)
#         generate successors to s, calculate f(n)
#         point successors back to s
#         if s is an element of closed 
#             add s to closed 
#             add successors to open p-queue 
#         s = next state from open 