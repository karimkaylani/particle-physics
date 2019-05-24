import math

SPEED_OF_LIGHT = 299792458

fp = 'muons.txt'
m1string = ''
m2string = ''
allValuesCorrect = False

def calculate4Vector(pt, eta, phi, mass):

    # calculate px, py, pz
    px = (pt * math.cos(phi))
    py = (pt * math.sin(phi))
    pz = (pt * math.sinh(eta))

    # do pythag theorem to get magnitude of the momentum
    magnitude = math.sqrt(px**2 + py**2 + pz**2)

    # calculate energy
    energy = math.sqrt(mass**2 + magnitude**2)

    # create 4-vector
    fourVector = ((energy/SPEED_OF_LIGHT), px, py, pz)

    # return 4-vector
    return (fourVector, magnitude)

def calculateInvariantMass(m1fourVector, m2fourVector):
    return


# open file
with open(fp) as file:
    # enumerate line-by-line through file
    for i, line in enumerate(file):
        if line.startswith('Run'):      # find identifier line for specific event
            identifier = line.strip()
            currentLine = i
            allValuesCorrect = False
        elif i == currentLine + 2:  # muon 1
            m1string = line
        elif i == currentLine + 3:  # muon 2
            m2string = line
        elif i == currentLine + 4:  # to negate the extra line
            allValuesCorrect = True

        # instantiate values as type float
        if allValuesCorrect :
            split_m1 = m1string.split(' ')
            m1pt = float(split_m1[2])
            m1eta = float(split_m1[3])
            m1phi = float(split_m1[4])
            m1mass = float(split_m1[5])

            split_m2 = m2string.split(' ')
            m2pt = float(split_m2[2])
            m2eta = float(split_m2[3])
            m2phi = float(split_m2[4])
            m2mass = float(split_m2[5])

            # print(calculate4Vector(m1pt, m1eta, m1phi, m1mass))
            # print(calculate4Vector(m2pt, m2eta, m2phi, m2mass))
            # print('')





