from Board import *
#don't need PriQue because ida* uses a stack, modeled as a list in this case
import sys
import copy


#helper function for ida*, performing limited DFS
def FLimitDFS(initialBoard, limit, heuristic):
    done = False
    # start with gigantic min
    min = sys.maxsize
    board = initialBoard
    list = [] #model of the stack
    goal = Board()
    global totalNodes
    totalNodes = 0 # keep track of # of nodes

    while(done is False):
        if(board.totalCost <= limit):
            if(board.__eq__(goal)): #isGoal(s)
                return board.moves
            successors = board.generateMoves()
            totalNodes +=1 # add to totalNodes when generateMoves() is called
            for i in successors: #loop through moves and add children to list
                #point successors back to board
                #make a deep copy of the board
                child = copy.deepcopy(board)
                child.moves.append(i)
                child.makeMove(i) #make the move
                #calculate the f-cost and store in child
                totalCost = len(child.moves) + heuristic(child)
                child.totalCost = totalCost

                #add this child to the list
                list.append(child)
        else:
            if(board.totalCost < min): 
                min = board.totalCost #update the min if cost > limit

        try:
            board = list.pop()
            #totalNodes += 1
        except:
            done = True

    return min

#bulk logic of ida*
def idaStar(initialBoard, heuristic):
    limit = initialBoard.totalCost
    r = None # any number works here
    while(isinstance(r, list) == False): #if r is not a Board object
        r = FLimitDFS(initialBoard, limit, heuristic)
        if(isinstance(r, int) == True): # if r is an integer
            limit = r
    
    return r, totalNodes



#*********** PSEUDOCODE FROM COURSE WEBSITE **************#
#link: https://www.usna.edu/Users/cs/crabbe/SI420/current/index.html

#start with f limit DFS
# FLimitDFS(StartState s, Limit l)
#   done = false
#   min = gigantic
#   while (!done)
#     if (f(s) ≤ l) # f(s) is my heuristic
#       if(isGoal(s))
#         return path to s
#       generate successors to s
#       point successors back to s
#       push successors on open stack
#     else
#       if (f(s) < min)
#         min ← f(s)
#     s ←  pop next state from open
#     if pop failed, done  ← true
#   return min
#
# DFS(StartState s)
#
# #then do IDA* (calls FLimit)
#   IDA*(StartState s)
#   l ← f(s)
#   r ← ⌀
#   while (isNotPath(r))
#     r ← FLimitDFS(s,l)
#     if (isNumber(r)) l ← r
#   return r
