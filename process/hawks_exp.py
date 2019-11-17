import numpy as np

from point.process.base_process import  PointProcessBase
from point.algo.simulation import OgataThinningAlgo


class HawksExponentialDecay(PointProcessBase) :

    def __init__(self, background_intensity, beta, alpha):
        super().__init__()
        self.background_intensity = background_intensity
        self.alpha = alpha
        self.beta = beta
        
    def cumulant(self, time, index = 0): 
        if index > len(self.samples) - 1 :
              raise ValueError("index call out of bound")
        pass

  
    def hazard(self, time, index = 0):   
        if index > len(self.samples) - 1 :
              raise ValueError("index call out of bound")
        
        s = self.samples[index]
        hz = self.background_intensity
        
        for t in s.points :
            if t > time :
                break
            hz = hz + self.alpha * np.exp(- self.beta * (time - t))

        return hz
        
    
    def max_hazard(self, index = 0):
        return 0
    
    def sample(self, expiry):
        simulator = OgataThinningAlgo()
        simulator.simulate(self, expiry)


        
        
        

        
        
