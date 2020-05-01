from ROOT import *

# read file and instantiate tree
f = TFile('muons.root', 'read')
tree = f.Get('tnt;1')

muon1 = TLorentzVector()
muon2 = TLorentzVector()

def calculateInvariantMass(muon1, muon2):
    # add the muons
    newParticle = muon1 + muon2

    # return mass of new particle
    return (newParticle.M())

# loop through each value
for event in tree:

	# instantiate values
	pt1 = event.pt1
	phi1 = event.phi1
	eta1 = event.eta1

	pt2 = event.pt2
	phi2 = event.phi2
	eta2 = event.eta2

	# instantitae muons
	muon1.SetPtEtaPhiM(pt1, eta1, phi1, 0.1)
	muon2.SetPtEtaPhiM(pt2, eta2, phi2, 0.1)

	print(calculateInvariantMass(muon1, muon2))

