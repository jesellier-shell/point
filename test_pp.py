from point.process.poisson import PoissonProcess
from point.process.hawks_exp import HawksExponentialDecay

intensity = 0.2
expiry = 100

pro = PoissonProcess(intensity)
pro.generate(expiry)

print("Poisson")
print("num.points: " + str(pro.samples[0].size()))
pro.plot(print_hazard = True)

print("Transfered_Hawkes")
hwks = HawksExponentialDecay(0.01, 0.2, 0.2)
hwks.samples = pro.samples
hwks.plot(print_hazard = True)
  