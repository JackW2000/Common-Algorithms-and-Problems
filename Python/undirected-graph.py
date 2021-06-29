#   Vertex class will be used to represent each vertex/ node within the graph
class Vertex:
    #   Function will initialise a vertex object
    def __init__(self, vertex_id):
        #   Initialise the vertex/ node using an ID value
        self.id = vertex_id
        #   Initialise a dictionary of neighbouring vertices/ nodes (vertices that are linked by an arc)
        self.neighbours = {}

    #   Function will provide a string output ot replace the default output
    #   Without this, the string output is <__main__.Vertex object at 0x00000>
    def __str__(self):
        #   Return the ID and neighbouring nodes as a string
        return str(self.id) + " neighbours " + str([x.id for x in self.neighbours])

    #   Function will add a neighbour to an existing vertex object
    def add_neighbour(self, neighbour_id, weight=0):
        #   Add a neighbour to the dict and set a weight for the arc between (0 by default)
        self.neighbours[neighbour_id] = weight

    #   Function will return key values for all neighbouring vertices (this will be their ID values)
    def get_neighbours(self):
        #   Return the key values for the neighbour dict
        return self.neighbours.keys()

    #   Function will return the ID for the vertex
    def get_id(self):
        return self.id

    #   Function will return the weighting of an arc between the current node and the neighbour passed
    def get_weight(self, neighbour_id):
        #   Return the weighting of the arc using the key passed as neighbour from the neighbours dict
        #   (this will be the arc weight between the current vertex and the neighbouring vertex)
        return self.neighbours[neighbour_id]


#   Graph class will contain data for all vertices/ nodes within the graph
class Graph:
    #   Function will initialise a graph object
    def __init__(self):
        #   Initialise the graph to hold a dictionary of vertices/ nodes
        self.vertices = {}
        #   Keep a count of the number of vertices/ nodes
        self.vertices_count = 0

    #   Function to allow graph object to be iterable
    def __iter__(self):
        return iter(self.vertices.values())

    #   Function for adding a new vertex to the graph
    def add_vertex(self, vertex_id):
        #   Increment the vertices count
        self.vertices_count += 1
        #   Create a new vertex object using the ID provided
        new_vertex = Vertex(vertex_id)
        #   Add the new vertex to the dictionary using the ID
        self.vertices[vertex_id] = new_vertex

    #   Function will return a vertex's details if a vertex with the given ID exists
    def get_vertex(self, vertex_id):
        #   Check for the vertex ID within the vertices dict
        if vertex_id not in self.vertices:
            #   If not found, return None
            return None
        else:
            #   If found, return the vertex
            return self.vertices[vertex_id]

    #   Function will return key values for all vertices in the graph (this will be their ID values)
    def get_vertices(self):
        #   Return the key values for the vertices dict
        return self.vertices.keys()

    #   Function will add an arc/ edge between two vertices (passed as start_vertex and end_vertex)
    def add_edge(self, start_vertex_id, end_vertex_id, cost=0):
        #   If the vertex is not already in the graph, add it as a new node
        if start_vertex_id not in self.vertices:
            self.add_vertex(start_vertex_id)
        if end_vertex_id not in self.vertices:
            self.add_vertex(end_vertex_id)

        #   Add a neighbour to the start vertex using the end vertex ID and cost
        self.vertices[start_vertex_id].add_neighbour(self.vertices[end_vertex_id], cost)
        #   Add a neighbour to the end vertex using the start vertex ID and cost
        self.vertices[end_vertex_id].add_neighbour(self.vertices[start_vertex_id], cost)


#   Driver code
if __name__ == "__main__":
    #   Initialise a graph object
    graph = Graph()

    #   Add vertices to the graph
    graph.add_vertex("A")
    graph.add_vertex("E")
    graph.add_vertex("I")
    graph.add_vertex("O")
    graph.add_vertex("U")

    #   Add edges/ arcs between vertices
    graph.add_edge("A", "E", 10)
    graph.add_edge("A", "I", 7)
    graph.add_edge("E", "I", 5)
    graph.add_edge("E", "O", 2)
    graph.add_edge("I", "O", 4)
    graph.add_edge("O", "U", 3)

    #   Output all vertices linked to a vertex
    for vertex in graph:
        print("%s" % (graph.vertices[vertex.get_id()]))

    print()

    #   Loop over vertices to output the vertex ID's and weighting of edges/ arcs between them
    for vertex in graph:
        for weighting in vertex.get_neighbours():
            print("%s -> %s Cost: %d" % (vertex.get_id(), weighting.get_id(), vertex.get_weight(weighting)))

    print()

    #   Add a new vertex to an existing graph
    graph.add_vertex("Y")

    #   Add a link for the new vertex
    graph.add_edge("U", "Y", 1)

    #   Output all vertices linked to a vertex
    for vertex in graph:
        print("%s" % (graph.vertices[vertex.get_id()]))

    print()

    #   Loop over vertices to output the vertex ID's and weighting of edges/ arcs between them
    for vertex in graph:
        for weighting in vertex.get_neighbours():
            print("%s -> %s Cost: %d" % (vertex.get_id(), weighting.get_id(), vertex.get_weight(weighting)))

    print()
