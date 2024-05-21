import time

from pyinstrument import Profiler
from colony import Colony
from multiprocessing import Pool


best_global_makespan = float('inf')
best_global_assignment = None
best_global_sequence = None
best_global_edges = None


def initialize_colony():
    colony = Colony()
    return colony

def run_heuristic_worker(args):
    graph, start, pro_time, heuristic = args
    makespan, assignment, sequence, edges = Colony.heuristic_worker(graph, start, pro_time, heuristic)
    return makespan, assignment, sequence, edges


if __name__ == '__main__':
    start_time = time.time()


    p = Profiler()
    p.start()
    colony = initialize_colony()
    graph = colony.graph.G



    start = colony.graph.start
    pro_time = colony.data.pro_time
    heuristic = colony.h


    #global best_global_makespan, best_global_assignment, best_global_sequence
    worker_args = [(graph, start, pro_time, heuristic) for _ in range(colony.parameters['num_ants'])]
    cycle = 1
    while time.time() - start_time < colony.parameters['time_limit']:
        print("cycle", cycle)
        with Pool() as pool:
            results = pool.map(run_heuristic_worker, worker_args)
        sorted_solutions = sorted(results, key=lambda x: x[0])
        num_solutions_to_keep = len(sorted_solutions) // 2
        top_solutions = sorted_solutions[:num_solutions_to_keep]
        #print(top_solutions)
        current_best_makespan, current_best_assignment, current_best_sequence, current_best_edges = min(results, key=lambda x: x[0])
        if current_best_makespan < best_global_makespan:
            best_global_makespan = current_best_makespan
            best_global_assignment = current_best_assignment
            best_global_sequence = current_best_sequence
            best_global_edges = current_best_edges
            print(f"New best makespan found: {best_global_makespan}")
            #print("best_global_assignment", best_global_assignment)
            #print("best_global_sequence", best_global_sequence)
        else:
            print(f"No improvement, best makespan remains: {best_global_makespan}")
        colony.call_update_ph(graph, top_solutions)
        cycle += 1
    p.stop()
    #print("Total cycles completed:", cycle)
    #p.open_in_browser()