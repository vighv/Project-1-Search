# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    "*** YOUR CODE HERE ***"


    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    """


    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # Structure of getsuccessors: [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
    #Initialization of variables

    dfs_tree = list()
    dfs_start = problem.getStartState()
    dfs_frontier = [x[0] for x in problem.getSuccessors(dfs_start)]
    dfs_visited = set()
    sol_path = list()

    print "Is Stack empty? - ", not dfs_tree
    print "Successors of Start are:",  dfs_frontier
    #util.raiseNotDefined()

    if problem.isGoalState(dfs_start):
        print "Trivial problem! Started at the goal state"
        return sol_path

    dfs_tree.append(dfs_start)
    current_node = dfs_start
    dfs_visited.add(dfs_start)

    while dfs_tree:

        dfs_frontier = problem.getSuccessors(current_node)
        print "\nCurrent Frontier: ", dfs_frontier
        print "Current Solution Path:", sol_path
        print "Visited nodes are:", dfs_visited

        if not dfs_frontier:
            if len(dfs_visited) == 1 :
                print "No Solution! No frontier at the very start!"
                return sol_path
            else:
                sol_path.pop()
                dfs_tree.pop()
                current_node = dfs_tree[-1]

        else:
            visit_flag = 1
            for child in dfs_frontier:
                if child[0] not in dfs_visited:
                    dfs_tree.append(child[0])
                    sol_path.append(child[1])
                    dfs_visited.add(child[0])
                    visit_flag = 0
                    if problem.isGoalState(child[0]):
                        print "Solution found using DFS!"
                        print "Final Solution Path:", sol_path
                        return sol_path
                    else:
                        current_node = child[0]
                        break
            if visit_flag:
                sol_path.pop()
                dfs_tree.pop()
                current_node = dfs_tree[-1]






def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
