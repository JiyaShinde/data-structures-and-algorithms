class Graph:
    def __init__(self):
        self.vertices = 0
        self.adjacencyMatrix = []
        self.visited = []

    def CreateGraph(self):
        self.vertices = int(input("Enter number of vertices: "))

        self.adjacencyMatrix = []

        for i in range(self.vertices):
            row = []

            for j in range(self.vertices):
                row.append(0)

            self.adjacencyMatrix.append(row)

        edges = int(input("Enter number of edges: "))

        for k in range(edges):
            source = int(input("Enter source vertex: "))
            destination = int(input("Enter destination vertex: "))

            self.adjacencyMatrix[source][destination] = 1
            self.adjacencyMatrix[destination][source] = 1

        self.visited = [False] * self.vertices

    def DisplayGraph(self):
        print("Adjacency Matrix")

        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.adjacencyMatrix[i][j], end=" ")

            print()

    def DFS(self, vertex):
        self.visited[vertex] = True

        print(vertex, end=" ")

        for i in range(self.vertices):
            if self.adjacencyMatrix[vertex][i] == 1 and self.visited[i] == False:
                self.DFS(i)


def Main():
    graph = Graph()

    graph.CreateGraph()

    graph.DisplayGraph()

    startVertex = int(input("Enter starting vertex: "))

    print("DFS Traversal")
    graph.DFS(startVertex)


Main()
