# Nothing fancy, just a little demonstration of some Python!

from Classes.Children.Population import Population
from Classes.Children.Sample import Sample

MyTarget = Population(1,100,20)
MyTarget.CalculateVariance()
MyTarget.CalculateStdDev()
MyTarget.DisplayValues()

MyTarget = Sample(1,100,20)
MyTarget.CalculateVariance()
MyTarget.CalculateStdDev()
MyTarget.DisplayValues()