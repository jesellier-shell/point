import numpy as np
import abc

from point.process.poisson import PoissonProcess
from point.process.base_process import PointSample

class SimulationAlgo(metaclass=abc.ABCMeta):
    pass
    
    
class ShedlerLewisThinningAlgo(SimulationAlgo):
    
    def __init__(self, bound = None):
        self.bound = bound
     
    def simulate(self, process, expiry):
           
        M = self.bound
        if self.bound == None :
            M = process.max_hazard()

        p = PoissonProcess(M)
        p.generate(expiry)
        process.samples.append(PointSample([], expiry))
        index = len(process.samples) - 1
        t = 0
        
        while t < expiry :
            t = t - np.log(np.random.uniform())/M
            if(process.hazard(t, index) >= np.random.uniform()*M) :
                process.samples[-1].points.append(t)
    
    
class OgataThinningAlgo(SimulationAlgo):
    
    def __init__(self, epsilon = 10**-5):
        self.epsilon = epsilon
     
    def simulate(self, process, expiry):
        
        process.samples.append(PointSample([], expiry))
        index = len(process.samples) - 1
        t = 0

        while t < expiry :
            M = process.hazard(t + self.epsilon, index)   
            
            t = t - np.log(np.random.uniform())/M

            if process.hazard(t, index) >= np.random.uniform()*M :
                process.samples[-1].points.append(t)
                


    

    
    



