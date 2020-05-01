from ROOT import *

# read file and instantiate tree
f = TFile('tag_1_delphes_events.root', 'read')
tree = f.Get('Delphes;1')
h1 = TH1F('h1', 'Invariant Mass Histogram', 100, 0, 500)

muonCounter = 0

muon1 = TLorentzVector()
muon2 = TLorentzVector()

def calculateInvariantMass(muon1, muon2):
    # add the muons
    newParticle = muon1 + muon2

    # return mass of new particle
    return (newParticle.M())


# loop through each value
for event in tree:

	# if event generates 2 muons
	if event.Muon_size == 2:
		muonCounter += 1

		if (muonCounter == 1):
			pt1 = event.GetLeaf('Muon.PT').GetValue()
			eta1 = event.GetLeaf('Muon.Eta').GetValue()
			phi1 = event.GetLeaf('Muon.Phi').GetValue()

		else:
			pt2 = event.GetLeaf('Muon.PT').GetValue()
			eta2 = event.GetLeaf('Muon.Eta').GetValue()
			phi2 = event.GetLeaf('Muon.Phi').GetValue()

			muon1.SetPtEtaPhiM(pt1, eta1, phi1, 0.1)
			muon2.SetPtEtaPhiM(pt2, eta2, phi2, 0.1)

			h1.Fill(calculateInvariantMass(muon1, muon2))
			print(calculateInvariantMass(muon1, muon2))

			muonCounter = 0
h1.Draw()