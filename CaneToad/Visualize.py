from SimulationDriver import SimulationDriver
from Toad import Toad


# After calculating the average, we can see that it took about 10 rounds in order for all Toad to be dead

sim = SimulationDriver()
globalTotal=0
i = 0
while i < 10:
    result = sim.run(False)
    sim = SimulationDriver()
    i+=1
    globalTotal+= result
    Toad.numberDead = 0
    Toad.numberMigrated=0

sim = SimulationDriver()
sim.run(True)
print('On averaege, it took ' + str(globalTotal / 100) + " simulation to end all Toad")