#
# File created by Leonardo Cencetti on 2/22/2020
#
from math import sqrt


class GaussianFilter:
    def __init__(self, minElement):
        self.std = 0
        self.count = 0
        self.sum = 0
        self.squareSum = 0
        self.mean = 0
        self.minElement = minElement

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def update(self, value):
        if self.count < self.minElement or abs(self.mean - value) <= self.std:
            self.count += 1
            self.sum += value
            self.squareSum += value ** 2
            self.std = sqrt(self.squareSum / self.count - (self.sum / self.count) ** 2)
        self.mean = self.sum / self.count
        # print('\t\t[STD]\t\t', self.std)
        return self.mean
