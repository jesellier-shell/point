from point.process.base_process import  PointProcessBase
from point.algo.simulation import ShedlerLewisThinningAlgo

class InhomogeneousPoissonProcess(PointProcessBase) :

    def __init__(self, hazard_rates):
        super().__init__()
        self.hazard_stepfunc = hazard_rates

    def cumulant(self, time, index = 0):
        return self.hazard_stepfunc.integral(time)
    
    def hazard(self, time, index = 0):
        return self.hazard_stepfunc.value(time)
    
    def max_hazard(self, index = 0):
        return max(self.hazard_stepfunc.values)
            
    def sample(self, expiry):
        simulator = ShedlerLewisThinningAlgo()
        simulator.simulate(self, expiry)
    


        
        
        

        
        
