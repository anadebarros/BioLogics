class Organism:
    def __init__(self, genome, energy=10):
        self.genome = genome
        self.energy = energy
        self.alive = True

    def consume_energy(self, amount=1):
        self.energy -= amount
        if self.energy <= 0:
            self.alive = False
