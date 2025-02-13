class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start not in self.graph_dict:
            return []
        
        if start == end:
            return [path]
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths
    
    def shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start not in self.graph_dict:
            return None
        
        if start == end:
            return path
        
        shortest = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.shortest_path(node, end, path)
                if sp:
                    if shortest is None or len(sp) < len(shortest):
                        shortest = sp
        return shortest


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(edges=routes)
    print(route_graph.graph_dict)

    start = "Mumbai"
    end = start
    print(f"Paths between {start} and {end}:", route_graph.get_paths(start, end))
