import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import numpy as np

all_jobs_mac = [(1, 1, 1), (1, 1, 3), (1, 2, 5), (1, 2, 3), (1, 2, 2), (1, 3, 3), (1, 3, 6), (1, 4, 6), (1, 4, 2), (1, 4, 1), (1, 5, 3), (1, 6, 6), (1, 6, 3), (1, 6, 4), (2, 1, 2), (2, 2, 3), (2, 3, 1), (2, 4, 2), (2, 4, 4), (2, 5, 6), (2, 5, 2), (2, 5, 1), (3, 1, 2), (3, 2, 3), (3, 2, 6), (3, 3, 6), (3, 3, 2), (3, 3, 1), (3, 4, 3), (3, 4, 2), (3, 4, 6), (3, 5, 1), (3, 5, 5), (4, 1, 6), (4, 1, 2), (4, 1, 1), (4, 2, 2), (4, 3, 3), (4, 4, 5), (4, 4, 3), (4, 4, 2), (4, 5, 3), (4, 5, 6), (5, 1, 5), (5, 1, 3), (5, 1, 2), (5, 2, 6), (5, 2, 2), (5, 2, 1), (5, 3, 2), (5, 4, 1), (5, 4, 3), (5, 5, 2), (5, 5, 4), (5, 6, 3), (5, 6, 2), (5, 6, 6), (6, 1, 3), (6, 1, 6), (6, 2, 1), (6, 3, 3), (6, 3, 2), (6, 3, 6), (6, 4, 2), (6, 5, 6), (6, 5, 2), (6, 5, 1), (6, 6, 1), (6, 6, 4), (7, 1, 6), (7, 2, 1), (7, 2, 4), (7, 3, 3), (7, 3, 2), (7, 3, 6), (7, 4, 2), (7, 4, 5), (7, 4, 1), (7, 5, 3), (8, 1, 3), (8, 1, 6), (8, 2, 3), (8, 2, 2), (8, 2, 6), (8, 3, 6), (8, 3, 2), (8, 3, 1), (8, 4, 2), (8, 5, 2), (8, 5, 4), (9, 1, 6), (9, 2, 1), (9, 2, 5), (9, 3, 6), (9, 3, 3), (9, 3, 4), (9, 4, 1), (9, 5, 3), (9, 5, 2), (9, 5, 6), (9, 6, 2), (9, 6, 4), (10, 1, 3), (10, 1, 6), (10, 2, 3), (10, 2, 2), (10, 2, 6), (10, 3, 5), (10, 3, 3), (10, 3, 2), (10, 4, 6), (10, 5, 2), (10, 5, 4), (10, 6, 1), (10, 6, 4)]

job_times = {(7, 1): {'start': 0, 'end': 1}, (3, 1): {'start': 0, 'end': 6}, (6, 1): {'start': 0, 'end': 4}, (4, 1): {'start': 0, 'end': 1}, (5, 1): {'start': 0, 'end': 3}, (9, 1): {'start': 1, 'end': 2}, (2, 1): {'start': 6, 'end': 12}, (10, 1): {'start': 2, 'end': 4}, (8, 1): {'start': 4, 'end': 8}, (1, 1): {'start': 1, 'end': 6}, (6, 2): {'start': 6, 'end': 8}, (2, 2): {'start': 12, 'end': 13}, (3, 2): {'start': 6, 'end': 8}, (5, 2): {'start': 8, 'end': 13}, (2, 3): {'start': 13, 'end': 15}, (10, 2): {'start': 12, 'end': 18}, (5, 3): {'start': 18, 'end': 24}, (7, 2): {'start': 1, 'end': 3}, (1, 2): {'start': 6, 'end': 9}, (9, 2): {'start': 9, 'end': 14}, (6, 3): {'start': 13, 'end': 17}, (5, 4): {'start': 24, 'end': 29}, (5, 5): {'start': 29, 'end': 35}, (9, 3): {'start': 14, 'end': 20}, (7, 3): {'start': 17, 'end': 21}, (6, 4): {'start': 24, 'end': 30}, (4, 2): {'start': 30, 'end': 36}, (2, 4): {'start': 35, 'end': 41}, (8, 2): {'start': 20, 'end': 26}, (6, 5): {'start': 30, 'end': 35}, (8, 3): {'start': 29, 'end': 30}, (1, 3): {'start': 21, 'end': 25}, (3, 3): {'start': 30, 'end': 31}, (1, 4): {'start': 31, 'end': 32}, (10, 3): {'start': 18, 'end': 21}, (5, 6): {'start': 35, 'end': 39}, (8, 4): {'start': 36, 'end': 42}, (10, 4): {'start': 35, 'end': 36}, (3, 4): {'start': 36, 'end': 42}, (2, 5): {'start': 41, 'end': 42}, (4, 3): {'start': 39, 'end': 40}, (9, 4): {'start': 42, 'end': 44}, (8, 5): {'start': 42, 'end': 48}, (7, 4): {'start': 21, 'end': 22}, (4, 4): {'start': 40, 'end': 43}, (4, 5): {'start': 43, 'end': 47}, (9, 5): {'start': 44, 'end': 50}, (7, 5): {'start': 47, 'end': 48}, (1, 5): {'start': 48, 'end': 49}, (1, 6): {'start': 49, 'end': 55}, (10, 5): {'start': 48, 'end': 54}, (9, 6): {'start': 50, 'end': 56}, (6, 6): {'start': 44, 'end': 47}, (3, 5): {'start': 43, 'end': 48}, (10, 6): {'start': 54, 'end': 57}}

machine_assignments = {(7, 1): (7, 1, 6), (3, 1): (3, 1, 2), (6, 1): (6, 1, 3), (4, 1): (4, 1, 1), (5, 1): (5, 1, 5), (9, 1): (9, 1, 6), (2, 1): (2, 1, 2), (10, 1): (10, 1, 6), (8, 1): (8, 1, 3), (1, 1): (1, 1, 1), (6, 2): (6, 2, 1), (2, 2): (2, 2, 3), (3, 2): (3, 2, 6), (5, 2): (5, 2, 6), (2, 3): (2, 3, 1), (10, 2): (10, 2, 2), (5, 3): (5, 3, 2), (7, 2): (7, 2, 4), (1, 2): (1, 2, 5), (9, 2): (9, 2, 5), (6, 3): (6, 3, 3), (5, 4): (5, 4, 1), (5, 5): (5, 5, 4), (9, 3): (9, 3, 6), (7, 3): (7, 3, 3), (6, 4): (6, 4, 2), (4, 2): (4, 2, 2), (2, 4): (2, 4, 4), (8, 2): (8, 2, 6), (6, 5): (6, 5, 6), (8, 3): (8, 3, 1), (1, 3): (1, 3, 3), (3, 3): (3, 3, 1), (1, 4): (1, 4, 1), (10, 3): (10, 3, 5), (5, 6): (5, 6, 3), (8, 4): (8, 4, 2), (10, 4): (10, 4, 6), (3, 4): (3, 4, 6), (2, 5): (2, 5, 1), (4, 3): (4, 3, 3), (9, 4): (9, 4, 1), (8, 5): (8, 5, 4), (7, 4): (7, 4, 5), (4, 4): (4, 4, 5), (4, 5): (4, 5, 3), (9, 5): (9, 5, 2), (7, 5): (7, 5, 3), (1, 5): (1, 5, 3), (1, 6): (1, 6, 6), (10, 5): (10, 5, 4), (9, 6): (9, 6, 2), (6, 6): (6, 6, 1), (3, 5): (3, 5, 5), (10, 6): (10, 6, 1)}

def visulaize(job_times, machine_assignments):
    unique_jobs = len(set(job[0] for job in job_times))
    color_map = get_cmap('tab20', unique_jobs)


    job_colors = {job: color_map(i) for i, job in enumerate(sorted(set(job[0] for job in job_times)))}


    fig, ax = plt.subplots(figsize=(15, 10))


    machines = sorted(set(assignment[2] for assignment in machine_assignments.values()))
    machine_yticks = np.arange(len(machines))
    machine_labels = [f'Machine {machine}' for machine in machines]


    for (job, step), timing in job_times.items():
        machine_index = machines.index(machine_assignments[(job, step)][2])
        start = timing['start']
        end = timing['end']
        width = end - start
        rect = ax.barh(machine_index, width, left=start, height=0.8, color=job_colors[job], edgecolor='black')
        label = f'{job},{step}\n{start}-{end}'
        ax.text(start + width / 2, machine_index, label, ha='center', va='center', color='white', fontsize=8)


    ax.set_yticks(machine_yticks)
    ax.set_yticklabels(machine_labels)
    ax.set_xlabel('Time')
    ax.set_ylabel('Machines')
    ax.set_title('Gantt Chart of Job Schedule')

    custom_lines = [plt.Line2D([0], [0], color=color_map(i), lw=4) for i in range(unique_jobs)]
    ax.legend(custom_lines, [f'Job {i+1}' for i in range(unique_jobs)], loc='upper center', bbox_to_anchor=(0.5, -0.05),
              fancybox=True, shadow=True, ncol=5)

    plt.tight_layout()
    plt.savefig('s.png', bbox_inches='tight', dpi=300)


visulaize(job_times, machine_assignments)