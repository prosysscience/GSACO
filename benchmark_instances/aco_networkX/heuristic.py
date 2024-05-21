import random

class Heuristic():

    predecessors = {}

    def sequence(self, graph, start):
        for node1, data1 in graph.nodes(data=True):
            if data1['level'] == 1:
                j1, step1 = node1
                for node2, data2 in graph.nodes(data=True):
                    if data2['level'] == 1:
                        j2, step2 = node2
                        if j1 == j2 and step1 - 1 == step2:
                            self.predecessors[node1] = node2


        next_nodes_dict = {}
        for s, e, data in graph.edges(data=True):
            if len(e) < 3:
                if s in next_nodes_dict:
                    next_nodes_dict[s].append((e, data['pheromone']))  # Store pheromone with node
                else:
                    next_nodes_dict[s] = [(e, data['pheromone'])]

        selected_edges = []
        sequence = [start]
        visited = set()
        i = 0
        while i < len(sequence):
            job = sequence[i]
            possible_nodes = next_nodes_dict.get(job, [])
            #print(possible_nodes)
            while possible_nodes:
                total_pheromone = sum(pheromone for _, pheromone in possible_nodes)
                probabilities = [pheromone / total_pheromone for _, pheromone in
                                 possible_nodes]
                selected_node, _ = random.choices(possible_nodes, weights=probabilities, k=1)[0]
                if selected_node not in visited:
                    predecessor = self.predecessors.get(selected_node)
                    if predecessor is None or predecessor in visited:
                        sequence.append(selected_node)
                        visited.add(selected_node)
                        selected_edge = (job, selected_node)
                        selected_edges.append(selected_edge)
                possible_nodes = [node for node in possible_nodes if node[0] != selected_node]
            i += 1

        return sequence, selected_edges


    def makespan(self, graph, sequence, start, pro_time):
        machine_end_times = {}
        job_end_times = {}
        predecessor_end_time = {}
        assignment = {}

        for job in sequence:
            if job == start:
                continue

            for st, end, data in graph.edges(data=True):
                if st==job and len(end)==3:
                    possible_machines = end
                    j, s, mac = possible_machines
                    if mac not in machine_end_times:
                        machine_end_times[mac] = 0

        for job in sequence:
            if job == start:
                continue

            available_machines = []
            for s, end, data in graph.edges(data=True):
                if s == job and len(end) == 3:
                    j, s, machine = end
                    available_machines.append(machine)
            predecessor = self.predecessors.get(job)
            predecessor_completion_time = predecessor_end_time.get(predecessor, 0)

            # add here if the machine_end_time >= predecessor_end_time
            # chose between remaining machine # exclude one which is free later then predecessor ends
            select_machine = min(available_machines, key=lambda m: machine_end_times[m])
            #select_machine = random.choice(available_machines)
            job_with_mac = job + (select_machine,)

            process_time = pro_time[job_with_mac]
            start_time = max(machine_end_times[select_machine], predecessor_completion_time)
            end_time = start_time + process_time

            assignment[job] = job_with_mac
            job_end_times[job] = {'start': start_time, 'end': end_time}
            machine_end_times[select_machine] = end_time
            predecessor_end_time[job] = end_time

        machine_with_max_time = max(machine_end_times, key=machine_end_times.get)
        makespan = machine_end_times[machine_with_max_time]

        return makespan, assignment





