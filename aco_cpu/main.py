import time

from get_input import get_user_input
from pyinstrument import Profiler
import torch.multiprocessing as mp
import torch
from colony import Colony
from heuristic import sequence

device=torch.device('cpu')
global_best_makespan = float('inf')
global_best_edges = None
def worker(args):
    job_tensor, adjacency_matrix, pheromone_matrix, machine_matrix, device = args
    job_tensor = job_tensor.to(device)
    adjacency_matrix = adjacency_matrix.to(device)
    pheromone_matrix = pheromone_matrix.to(device)
    machine_matrix = machine_matrix.to(device)
    makespan, edges = sequence(job_tensor, adjacency_matrix, pheromone_matrix, machine_matrix)

    return makespan, edges.tolist()



def initialize_colony_parallel(num_ants, device):
    args_list = [(colony.job_tensor, colony.adjacency_matrix, colony.graph.pheromone_matrix, colony.machine_matrix, device) for _ in range(num_ants)]
    with mp.Pool(processes=num_ants) as pool:
        combined_results = pool.map(worker, args_list)



    results, results_s = zip(*combined_results)
    results_s = [torch.tensor(edges, dtype=torch.long, device=device) for edges in
                 results_s]
    return list(results), list(results_s)



if __name__ == '__main__':
    mp.set_start_method('spawn')
    profiler = Profiler()
    profiler.start()
    parameters = get_user_input()
    colony = Colony(parameters)
    start_time = time.time()
    n_cycles = 1
    while time.time() - start_time < parameters["time_limit"] or n_cycles <= parameters["cycle"]:
        #print(f'cycle {n_cycles}')
        results, results_s = initialize_colony_parallel(parameters["num_ants"], device)
        makespans = torch.tensor(results)
        min_index = torch.argmin(makespans).item()
        current_best_makespan = makespans[min_index].item()
        current_best_edges = results_s[min_index]
        if current_best_makespan < global_best_makespan:
            global_best_makespan = current_best_makespan
            global_best_edges = current_best_edges
            print(f"New best makespan found: {global_best_makespan}")
        else:
            print(f"No improvement, best makespan remains: {global_best_makespan}")

        colony.graph.update_pheromone(colony.graph.pheromone_matrix, global_best_edges, parameters["contribution"],
                                      parameters["rho"], parameters["min_pheromone"])

        print(f'cycle {n_cycles} completed in {time.time() - start_time}')
        n_cycles+=1

    profiler.stop()
    #profiler.open_in_browser()
    #print(profiler.output_text(unicode=True, color=True))






