import abc
import warnings
import matplotlib.pyplot as plt
import numpy as np

class PointSample:
    
    def __init__(self, points, expiry) :
        self.expiry = expiry
        self.points = points        
        
    def size(self):
        return len(self.points)
    
    

class PointProcessBase(metaclass=abc.ABCMeta) :

    def __init__(self):
        self.samples = []
    
    def reset(self):
        self.samples = []
        
    def plot(self, i = 0, print_hazard = False):
        
        if(i > len(self.samples)):
            print("out of bound error")
            pass

        max_bound = 1
        expiry = self.samples[i].expiry
        grid =  np.arange(0.0, expiry, 0.02)
        
        plt.plot(self.samples[i].points, [0] * len(self.samples[i].points), 'ro')

        if print_hazard :
            plt.plot(grid, [self.hazard(i) for i in grid], 'b', lw = 0.5)
            
            if not self.max_hazard(i) == 0:
                max_bound = self.max_hazard(i) + 0.2
            
        plt.axis([0, expiry, -0.2, max_bound])
        plt.axhline(0, color='black', linewidth = 0.5)
        plt.show()
        

    def generate(self, expiry, n = 1):
        self.reset()
        
        for i in range(n) :
            self.sample(expiry)
        
        if n == 1 :
            return self.samples[0]
        else : return self.samples
        
    
    @abc.abstractmethod
    def cumulant(self, time, index = 0):
        warnings.warn('calling abstract BaseProcess method', UserWarning)
        pass
    
    def hazard(self, time, index = 0):
        warnings.warn('calling abstract BaseProcess method', UserWarning)
        pass
    
    def max_hazard(self, index = 0):
        warnings.warn('calling abstract BaseProcess method', UserWarning)
        pass
            
    def sample(self, expiry):
        warnings.warn('calling abstract BaseProcess method', UserWarning)
        pass
    

        
        
        

        
        
