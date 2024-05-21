import time
from read_instance import Read_data
from graph import Graph
from heuristic import Heuristic
from pathlib import Path
script_dir = Path(__file__).resolve().parent.parent


class Colony():
    parameters = {
        "seed": None,  # Random seed internal random number generator
        #"dataset": script_dir / '1_Brandimarte' / 'BrandimarteMk1.fjs',
        "dataset": script_dir / '6_Fattahi' / 'Fattahi13.fjs',
        "pheromone_level": 1,  # Planning Horizon
        "evaporation": 0.3,
        "contribution": 0.5,
        "min_pheromone": 0.00001,
        "time_limit": 600,
        "num_ants": 10,
    }


    def __init__(self):
        self.graph = Graph()
        self.data = Read_data()
        self.h = Heuristic()
        self.data.data_caller(self.parameters['dataset'])
        start_time = time.time()
        self.graph.generate_graph(self.data.all_jobs, self.data.jobs, self.parameters['pheromone_level'])
        end_time = time.time()

        #print(self.data.all_jobs)


    def call_update_ph(self, g, t_s, evo=parameters['evaporation'], con=parameters['contribution'],
                       m_p=parameters['min_pheromone']):
        self.graph.update_pheromone(g, t_s, evo, con, m_p)

    @staticmethod
    def heuristic_worker(graph, start, pro_time, heuristic):
        sequence, edges = heuristic.sequence(graph, start)
        makespan, assignment = heuristic.makespan(graph, sequence, start, pro_time)
        return makespan, assignment, sequence, edges

