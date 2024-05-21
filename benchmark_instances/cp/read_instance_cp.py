


def read_and_convert_benchmark_data(file_path):
    converted_jobs = []

    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            job_data = [int(value) for value in line.strip().split()]
            job = []
            i = 0

            while i < len(job_data):
                num_operations = job_data[i]
                i += 1
                for _ in range(num_operations):
                    num_machines = job_data[i]
                    i += 1
                    operation_machines = []

                    for _ in range(num_machines):
                        machine_id = job_data[i]
                        i += 1
                        processing_time = job_data[i]
                        i += 1
                        operation_machines.append((processing_time, machine_id))

                    job.append(operation_machines)

            converted_jobs.append(job)


    return converted_jobs


