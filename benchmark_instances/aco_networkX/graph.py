import networkx as nx
class Graph():
    start = (0, 0)
    G = nx.DiGraph()

    track_makespan = []
    all_t_s = []

    def generate_graph(self, all_jobs, jobs, pheromone_level):
        if not self.G:
            self.G.add_node(self.start, level=1)

            for job_key in jobs:
                self.G.add_node(job_key, level=1)
            for job in all_jobs:
                self.G.add_node(job, level=2)

            for node1, data1 in self.G.nodes(data=True):
                if data1['level'] == 1:
                    j1, s1 = node1
                    if s1 == 1:
                        self.G.add_edge(self.start, node1, type='conjunctive')

            for node1, data1 in self.G.nodes(data=True):
                if data1['level'] == 1 and node1!=self.start:
                    j1, s1 = node1
                    for node2, data2 in self.G.nodes(data=True):
                        if data2['level'] == 1 and node2!=self.start:
                            j2, s2 = node2
                            if j1 == j2 and s1 < s2:
                                self.G.add_edge(node1, node2, type='conjunctive')
                            elif j1 != j2:
                                self.G.add_edge(node1, node2, type='disjunctive')

            for node1, data1 in self.G.nodes(data=True):
                if data1['level'] == 1 and node1!=self.start:
                    j1, s1 = node1
                    for node2, data2 in self.G.nodes(data=True):
                        if data2['level'] == 2:
                            j2, s2, m2 = node2
                            if j1==j2 and s1==s2:
                                self.G.add_edge(node1, node2, type='conjunctive')
            nx.set_edge_attributes(self.G, pheromone_level, 'pheromone')
        pass

    def update_pheromone(self, g, t_s, rho, delta_pheromone, min_pheromone):

        self.all_t_s.append(t_s)

        boost = delta_pheromone + 0.3
        for s in t_s:
            best_makespan, best_assignment, best_sequence, best_edges = s
            # print(best_assignment)
            # Decay existing pheromone on all edges
            for u, v, data in g.edges(data=True):
                updated_pheromone = (1 - rho) * data.get('pheromone', 0)
                # Ensure pheromone does not fall below the minimum
                data['pheromone'] = max(round(updated_pheromone, 8), min_pheromone)

            # increment part
            for node, next_node in best_assignment.items():
                if g.has_edge(node, next_node):
                    g[node][next_node]['pheromone'] = max(g[node][next_node].get('pheromone', 0) + boost,
                                                          min_pheromone)
            for edge in best_edges:
                current_node, next_node = edge
                if g.has_edge(current_node, next_node):
                    g[current_node][next_node]['pheromone'] = max(
                        g[current_node][next_node].get('pheromone', 0) + boost, min_pheromone)
        pass




