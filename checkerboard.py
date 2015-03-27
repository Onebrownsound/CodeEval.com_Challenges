import random, copy

class State:
    def __init__(self, board, parent, cost):
        self.board = board
        self.parent = parent
        self.cost = cost
        
    def heuristic(self, goal):
        result = 0
        for i in xrange(0,9):
            #if self.board[i] != goal[i]:
            #    result += 1
            n = self.board.index(i)
            m = goal.index(i)
            result += abs((n - m) / 3) + abs(((n / 3) % 3) - ((m / 3) % 3))
        return result
        
    def getNeighbours(self):
        i = self.board.index(0)
        neighbours = []
        if (i % 3) != 2:
            t = self.board[:]
            t[i], t[i+1] = t[i+1],t[i]
            neighbours.append(State(t, self, self.cost + 1))
        if (i % 3) != 0:
            t = self.board[:]
            t[i], t[i-1] = t[i-1],t[i]
            neighbours.append(State(t, self, self.cost + 1))
        if not i in [0,1,2]:
            t = self.board[:]
            t[i], t[i-3] = t[i-3],t[i]
            neighbours.append(State(t, self, self.cost + 1))
        if not i in [6,7,8]:
            t = self.board[:]
            t[i], t[i+3] = t[i+3],t[i]
            neighbours.append(State(t, self, self.cost + 1))
        return neighbours
        
    def printBoard(self):
        for i in xrange(0,9,3):
            print(str(self.board[i]) + str(self.board[i+1]) + str(self.board[i+2]))
            
    def isGoal(self, goal):
        return self.board == goal
        
    def f(self,goal):
        return self.cost + self.heuristic(goal)
        
    def cycles(self):
        path = self.parent
        while path != None:
            if path.board == self.board:
                return True
            path = path.parent
        return False

def removeDuplicates(frontier, goal):
    d = dict()
    for x in frontier:
        s = str(x.board)
        if s not in d:
            d[s] = x
        else:
            d[s] = min(d[s], x, key = lambda x: x.f(goal))
    return d.values()

def pathFinder(start, goal):
    frontier = [start]
    s = frontier.pop()
    while not s.isGoal(goal):
        frontier.extend(s.getNeighbours())
        frontier = [x for x in frontier if not x.cycles()]
        frontier = removeDuplicates(frontier, goal)
        frontier.sort(key=lambda x: x.f(goal), reverse = True)
        s = frontier.pop()
    print("Done")
    return s

goal = [0,1,2,3,4,5,6,7,8]
start = State(goal[:], None, 0)
random.shuffle(start.board)
path = pathFinder(start,goal)
