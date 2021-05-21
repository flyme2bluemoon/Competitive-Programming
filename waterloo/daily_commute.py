class Node():
    def __init__(self, state, parent, time):
        self.state = state
        self.parent = parent
        self.time = time

class QueueFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

n, w, d = [int(_) for _ in input().split(" ")]

walkways = {}

for i in range(w):
    a, b = [int(_) for _ in input().split(" ")]
    walkways[a] = b # can one station have multiple walkways?

route = [int(_) for _ in input().split(" ")]

swaps = []

for i in range(d):
    swaps.append([int(_) for _ in input().split(" ")])

SOURCE = 1
GOAL = n

def solve(path, walkways):
    source_node = Node(state=SOURCE, parent=None, time=0)
    frontier = QueueFrontier()
    frontier.add(source_node)

    explored = set()

    while True:
        if frontier.empty():
            raise Exception("frontier is empty")

        node = frontier.remove()

        if node.state == GOAL:
            minutes = 0
            while node.parent is not None:
                minutes += 1
                node = node.parent
            print(minutes)
            return

        explored.add(node.state)
        
        neighbors = []

        # add subway neighbors
        path_position = path.index(node.state)
        if path_position == node.time:
            if path_position != (len(path) - 1):
                neighbors.append(path[path_position + 1])
        else:
            print(f"ELSE: {node.state}, {path}, {node.time}")
            neighbors.append(node.state)
        
        # add walkway neighbors
        if node.state in walkways:
            neighbors.append(walkways[node.state])

        print(node.state, neighbors, path, walkways)
        for state in neighbors:
            if not frontier.contains_state(state) and state not in explored: # is this ok?
                child = Node(state=state, parent=node, time=(node.time + 1))
                frontier.add(child)
            else:
                print("state", state)

for i in swaps:
    x = i[0] - 1
    y = i[1] - 1
    route[x], route[y] = route[y], route[x]
    solve(route, walkways)
