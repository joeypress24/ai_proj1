 # priority queue using a unsorted list because there's more inserts
from Board import *

#MIN PRIORITY QUEUE OF BOARDS
class PriQue(list): #list parameter specifies that this is a list
    def __init__(self):
        self.size = 0 #size initialized at 0

    #insert an element into the priority queue, increments size
    #takes in a board and inserts it into the unsorted queue --> O(1) insert
    def insert(self, val):
        self.size += 1
        #print("INSERTING: Size = " + str(self.size))
        self.append(val)

    #return True if empty, False if not
    def empty(self):
        if(self.size == 0):
            return True
        else:
            return False

    # remove the element with the lowest priority, decrease size
    def dequeue(self):
        self.size -= 1
        #find the smallest value and store it for remove/return
        elem = min(self, key = lambda x : x.totalCost)
        #remove the element from the list
        self.remove(elem)
        return elem #return the element that was dequeue()'d

    #prints the current size of the priority queue, useful for debugging
    def getSize(self):
        return self.size


# test main
if __name__ == "__main__":
    queue = PriQue()

    b1 = Board()
    b1.scramble(5)
    b2 = Board()
    b2.scramble(11)
    b2.totalCost = 11

    queue.insert(b1)
    queue.insert(b2)
    queue.insert(Board()) #insert empty board

    print(queue.dequeue())

    b3 = Board()
    b3.totalCost = 20000
    queue.insert(b3)
    print("size: ")
    print(queue.getSize())
