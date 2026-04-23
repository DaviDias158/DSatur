class DSatur:
    def __init__(self, graph):
        self.graph = graph
        self.V = graph.V
        self.colors = [-1] * self.V  
        self.coloring_order = []

    def get_saturation_degree(self, v):
        """Retorna o número de cores distintas nos vizinhos de v."""
        neighbor_colors = set()
        for w in self.graph.adj[v]:
            if self.colors[w] != -1:
                neighbor_colors.add(self.colors[w])
        return len(neighbor_colors)

    def solve(self):
        v_start = -1
        max_deg = -1
        for v in range(self.V):
            deg = self.graph.degree(v)
            if deg > max_deg:
                max_deg = deg
                v_start = v
        
        self._assign_color(v_start, 0)
        uncolored = set(range(self.V))
        uncolored.remove(v_start)

        while uncolored:
            best_v = -1
            max_ds = -1
            max_deg_tie = -1

            for v in uncolored:
                ds = self.get_saturation_degree(v)
                deg = self.graph.degree(v)
                
                if ds > max_ds:
                    max_ds = ds
                    max_deg_tie = deg
                    best_v = v
                elif ds == max_ds:
                    if deg > max_deg_tie:
                        max_deg_tie = deg
                        best_v = v
            
            forbidden_colors = set()
            for w in self.graph.adj[best_v]:
                if self.colors[w] != -1:
                    forbidden_colors.add(self.colors[w])
            
            color = 0
            while color in forbidden_colors:
                color += 1
                
            self._assign_color(best_v, color)
            uncolored.remove(best_v)

        return self.colors

    def _assign_color(self, v, color):
        self.colors[v] = color
        self.coloring_order.append(v)

    def is_valid(self):
        """Valida se nenhum vizinho compartilha a mesma cor."""
        for v in range(self.V):
            if self.colors[v] == -1: return False
            for w in self.graph.adj[v]:
                if self.colors[v] == self.colors[w]:
                    return False
        return True
    
