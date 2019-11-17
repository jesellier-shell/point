from point.process.inhomogeneous_poisson import InhomogeneousPoissonProcess
from utils import StepFunction1D
from point.algo.simulation import ShedlerLewisThinningAlgo

expiry = 45
time = [1, 10, 20, 40, 100]
value = [0.01, 0.01, 2, 0.2, 0.2]
    
#test
intensisty = StepFunction1D(time, value)
ipp = InhomogeneousPoissonProcess(intensisty)

simulator = ShedlerLewisThinningAlgo()
simulator.simulate(ipp, expiry)
ipp.plot(print_hazard = True)
    
    
    

    
    



