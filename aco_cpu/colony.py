from smt2020 import SMT2020
from graph import Graph

class Colony():

    def __init__(self, parameters):
        self.smt2020 = SMT2020()
        self.graph = Graph()


        self.smt2020.smt_caller(parameters['dataset'], parameters['n'])


        self.job_tensor, self.adjacency_matrix, self.machine_matrix = self.graph.generate_graph(self.smt2020.jobs,
                                                                                   self.smt2020.machines, parameters['pheromone_level'])





        """
        self.smt2020.jobs = [[[2, 10],
                              [3, 2],
                              [0, 6]],

                             [[1, 8],
                              [3, 1],
                              [0, 4]],

                             [[1, 9],
                              [3, 3],
                              [0, 13]]]

        """








