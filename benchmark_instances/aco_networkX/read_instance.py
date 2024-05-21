
class Read_data():
    all_jobs = []
    pro_time = {}
    jobs = []


    def process_data(self, file_path):
        unique_job_step_set = set()
        with open(file_path, 'r') as file:
            lines = file.readlines()

        for job_id, line in enumerate(lines[1:], start=1):
            parts = line.split()
            num_operations = int(parts[0])

            idx = 1


            for step in range(1, num_operations + 1):
                num_machines = int(parts[idx])
                idx += 1
                unique_job_step_set.add((job_id, step))



                for _ in range(num_machines):
                    machine_number = int(parts[idx])
                    processing_time = int(parts[idx + 1])

                    idx += 2


                    job = (job_id,step,machine_number)
                    self.all_jobs.append(job)

                    if (job_id,step) not in self.pro_time:
                        self.pro_time[(job_id,step,machine_number)] = processing_time


        self.jobs = list(unique_job_step_set)
        self.jobs.sort()

        pass


    def data_caller(self, d):
        self.process_data(d)
        pass


