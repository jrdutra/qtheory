# About The Library
It is a **Python library** implementing the Queueing theory calculations.
As my term paper, I am developing a library, implementing the calculus of queuing theory. This library has the objective of characterising some queuing theory params as the queue arrival rate of clients, attendance rate and others...
Implementing in python, this library receives a input file with queue data and gives the output answers.
For the undergraduate thesis, I had toke some datas in a real queue and submited to the library as a input, to validate this project.

### Files Organization

```bash
qtheory
├── __init__.py
├── _multiserver.py
├── multiserver.py
├── _singleserver.py
├── singleserver.py
├── _stats.py
├── stats.py
├── _utils.py
├── README.md
└── requirements.txt


```

### The Library Data Flow

![PlantUML model](https://raw.githubusercontent.com/jrdutra/qtheory-suport/master/images/dataflowdiagram.png)

# The Library Usage

It is a **main.py** exemple using the arrivals resources:

### Code

```python
import qtheory as q
import csv
import pandas as pd

def main():
    try:
        #lê a hora chegada do arquivo CSV
        datafile = open('dados.csv')
        df = pd.read_csv(datafile)
        arrival_times = df['horachegada'].values
        #This is the line numbers in the CSV file 
        # of the begnings of the evaluation intervals. 
        intervals_beginning = [0,130,220,385,501]

        #Evaluating arrivals data
        ans = q.arrivals_per_minutes(arrival_times, intervals_beginning)
        print(ans)

        ans = q.real_relative_frequencys(arrival_times, intervals_beginning)
        print(ans)

        ans = q.arrival_theoretical_comparation(arrival_times, intervals_beginning)
        print(ans)

    except ValueError as err:
        print(err.args)

if __name__ == "__main__":
    main()
```
### Result
![PlantUML model](https://raw.githubusercontent.com/jrdutra/qtheory-suport/master/images/usage-exemple.png)

### The data file exemple (dados.csv)

![PlantUML model](https://raw.githubusercontent.com/jrdutra/qtheory-suport/master/images/csvexemple.png)

