from ROOT import TLorentzVector
import math

fp = 'muons.txt'
m1string = ''
m2string = ''
allValuesCorrect = False

def calculateInvariantMass(muon1, muon2):
    #add the muons
    newParticle = muon1 + muon2

    # return mass of new particle
    return (newParticle.M())

def writeInvMassToLine(invMass, iden):
    #create new text file and write identifier and invMass to it
    f = open('invariantMass.txt', 'a')  
    f.write(iden + '\n')
    f.write('Invariant Mass: ' + str(invMass) + '\n')
    f.write('\n')
    f.close()

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

            # create TLorentzObjects
            muon1 = TLorentzVector()
            muon2 = TLorentzVector()

            muon1.SetPtEtaPhiM(m1pt, m1eta, m1phi, m1mass)
            muon2.SetPtEtaPhiM(m2pt, m2eta, m2phi, m2mass)

            writeInvMassToLine(calculateInvariantMass(muon1, muon2), identifier)



