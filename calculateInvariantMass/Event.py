from Muon import Muon
import math

class Event:
    def __init__(self, muon1:Muon, muon2:Muon, identifier):
        self.muon1 = muon1
        self.muon2 = muon2

        self.identifier = identifier

    def getInvariantMass(self):
        # adding x,y,z values of two muons
        pxSum = self.muon1.px + self.muon2.px
        pySum = self.muon1.py + self.muon2.py
        pzSum = self.muon1.pz + self.muon2.pz
        # find magnitude of resulting vector
        magnitude = math.sqrt(pxSum**2 + pySum**2 + pzSum**2)
        # add two energy values together, then square
        sumEnergy = self.muon1.getEnergy() + self.muon2.getEnergy()
        # put everything together
        invMass = math.sqrt((sumEnergy**2 - magnitude**2))

        return invMass