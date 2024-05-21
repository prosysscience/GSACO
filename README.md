# ACO-SMT2020

This repository demonstrates the application of ant colony foraging behavior to optimize the 
scheduling process within large-scale semiconductor manufacturing environments.

## Datasets
For validation purpose, the datasets are available in "benchmark_instances" directory.

An ant colony algorithm implemented in Python using NetworkX for benchmark instances is available in "benchmark_instances/aco_networkX" directory.
The constraint programming (CP) model used for benchmark instances is available in "benchmark_instances/cp" directory. 
It is derived from an open source and can be found here:
[CP/or-tools for FJSP](https://github.com/google/or-tools/blob/stable/examples/python/flexible_job_shop_sat.py)

The large-scale semiconductor instances from SMT2020 is available in "HVLM" and "LVHM" directory.

The example instance used in paper for demonstration of algorithm working is available in "LVHM-ex" directory.

The CP model for SMT2020 instances is available in "cp_SMT2020" directory.

An ant colony algorithm for SMT2020 instances implemented in Python using PyTorch is available in "aco_cpu" directory

## Installation

Install Python interpreter (suggested: 3.9)
```shell
python3 -m pip install -r requirements.txt
```

## Usage

### ACO algorithm:
Reference directory: aco_cpu
#### Execute:
##### For windows:
```shell
main.py
```
##### For linux:
```shell
python main.py
```

For experiments, parameters of model can be adjusted within "get_input.py" file or command-line arguments.

### CP model:
Reference directory: cp_SMT2020
#### Execute:
##### For windows:
```shell
cp_model.py
```
##### For linux:
```shell
python cp_model.py
```
The parameters can be adjusted within "cp_model.py" file (n, dataset). 