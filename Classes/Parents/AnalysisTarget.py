import random
import statistics

class AnalysisTarget:
    def __init__(self, min_val, max_val, num_val) -> None:
        print(f'Populating {num_val} values from {min_val} to {max_val}')
        self.TotalValues = num_val
        self.ValuesList = []
        self.Variance = 0
        self.StdDev = 0

        for i in range(num_val):
            self.ValuesList.append(random.randint(min_val,max_val))

        self.Mean = statistics.mean(self.ValuesList)
        
        print(f'The values populated are: {self.ValuesList}')

    def DisplayValues(self):
        print(f'Your mean is {self.Mean:.2f}')
        print(f'Your variance is {self.Variance:.2f}')
        print(f'Your std dev is {self.StdDev:.2f}')