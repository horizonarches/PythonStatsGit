import statistics

from Classes.Parents.AnalysisTarget import AnalysisTarget

class Sample(AnalysisTarget):

    def __init__(self, min_val, max_val, num_val) -> None:
        super().__init__(min_val, max_val, num_val)
        print(f'You have chosen to analyze a sample of size {self.TotalValues}!')

    def CalculateVariance(self):
        self.Variance = statistics.variance(self.ValuesList)
    
    def CalculateStdDev(self):
        self.StdDev = statistics.stdev(self.ValuesList)