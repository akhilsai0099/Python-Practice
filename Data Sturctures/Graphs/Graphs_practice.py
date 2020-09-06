class Graph:
    def __init__(self , edges):
        self.edges = edges
        self.graph_dict = {}
        for start , end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print(f"Graph dict is {self.graph_dict} ")
    

    def get_path(self , start , end , path=[]):
        path = path + [start]
        if start == end:
            return path
        
        if start not in self.graph_dict or end not in self.graph_dict :
            return
        
        paths = []
        try:
            for node in self.graph_dict[start]:
                if node not in path:
                    new_paths = self.get_path(node , end , path)
                
                    for p in new_paths:
                        paths.append(p)
            return paths
                    
        except Exception as e:
            print(f"there are no paths from {start} to {end} ,{e}")
            

    def get_shortest_path(self , start , end , path =[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return
        
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node , end , path)
                if shortest_path is None or len(sp) < len(shortest_path):
                    shortest_path = sp
        return shortest_path



if __name__ == '__main__':

    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]


    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)
    start = "Dubai"
    end = "chennoa"
    print(route_graph.get_shortest_path(start , end))