import math

class Muon:
    def __init__(self, pt, eta, phi, mass):
        self.pt = pt
        self.eta = eta
        self.phi = phi
        self.mass = mass
        # find momentum of x,y,z
        self.px = (self.pt * math.cos(self.phi))
        self.py = (self.pt * math.sin(self.phi))
        self.pz = (self.pt * math.sinh(self.eta))

    def getMagnitude(self) -> float:
        # calculate magnitude
        magnitude = math.sqrt(self.px ** 2 + self.py ** 2 + self.pz ** 2)
        return magnitude

    def getEnergy(self) -> float:
        # calculate energy
        energy = math.sqrt(self.mass ** 2 + self.getMagnitude() ** 2)
        return energy

    def getFourVector(self) -> tuple:
        # create 4-vector
        fourVector = (self.getEnergy(), self.px, self.py, self.pz)
        return fourVector
