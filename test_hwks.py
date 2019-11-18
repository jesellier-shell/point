
from point.process.hawks_exp import HawksExponentialDecay
from point.algo.simulation import OgataThinningAlgo

expiry = 40
bck_int = 0.1
beta_ = 0.3
alpha_ = 0.2

hwks = HawksExponentialDecay(bck_int, beta = beta_, alpha = alpha_)
simulator = OgataThinningAlgo()
simulator.simulate(hwks, expiry)

print('plot')
hwks.plot(print_hazard = True)
