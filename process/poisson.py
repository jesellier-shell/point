import numpy as np

from point.process.base_process import  PointProcessBase, PointSample


class PoissonProcess( PointProcessBase) :

    def __init__(self, intensity):
        super().__init__()
        self.intensity = intensity
        
    def cumulant(self, time, index = 0):   
        return time * self.intensity
    
    def hazard(self, time , index = 0):   
        return self.intensity
    
    def max_hazard(self, index = 0):
        return self.intensity

    def sample(self, expiry):
        t = 0
        points = []
        
        while (t < expiry) :
            points.append(t)
            t = t + -(1/self.intensity)*np.log(1-np.random.uniform())
            
        points.pop(0)
        self.samples.append(PointSample(points, expiry))


        
        
        

        
        
