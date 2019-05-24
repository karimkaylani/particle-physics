class Event:


class Muon:
    def __init__(self, pt, eta, phi, mass):
        self._pt = pt
        self._eta = eta
        self._phi = phi
        self._mass = mass
        self._px = (self._pt * math.cos(self._phi))
        self._py = (self._pt * math.sin(self._phi))
        self._pz = (self._pt * math.sinh(self._eta))

    def getMagnitude(self) -> float:

        magnitude = math.sqrt(self._px ** 2 + self._py ** 2 + self._pz ** 2)
        return magnitude

    def getFourVector(self) -> tuple:

        # calculate energy
        energy = math.sqrt(mass ** 2 + self.getMagnitude() ** 2)

        # create 4-vector
        fourVector = ((energy / SPEED_OF_LIGHT), self._px, self._py, self._pz)

        # return 4-vector
        return (fourVector)