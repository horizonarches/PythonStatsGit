import statistics

from Classes.Parents.AnalysisTarget import AnalysisTarget

class Population(AnalysisTarget):

    def __init__(self, min_val, max_val, num_val) -> None:
        super().__init__(min_val, max_val, num_val)
        print("You have chosen to analyze a population!")

    def CalculateVariance(self):
        self.Variance = statistics.pvariance(self.ValuesList)
    
    def CalculateStdDev(self):
        self.StdDev = statistics.pstdev(self.ValuesList)