from ROOT import TFile, TH1F, TLorentzVector, gSystem

# read file and instantiate tree
f = TFile('tag_1_delphes_events.root', 'read')
tree = f.Delphes

h1 = TH1F('h1', 'Muon Invariant Mass Histogram', 100, 0, 500)

muonCounter = 0

muon1 = TLorentzVector()
muon2 = TLorentzVector()

def calculateInvariantMass(muon1, muon2):
    # add the muons
    newParticle = muon1 + muon2

    # return mass of new particle
    return (newParticle.M())
	
for event in tree:

	for i, muon in enumerate(event.Muon):

		if (tree.GetLeaf('Muon_size').GetValue(i) == 2):

			muonCounter += 1

			if (muonCounter == 1):
				pt1 = event.GetLeaf('Muon.PT').GetValue(i)
				eta1 = event.GetLeaf('Muon.Eta').GetValue(i)
				phi1 = event.GetLeaf('Muon.Phi').GetValue(i)

			else:
				pt2 = event.GetLeaf('Muon.PT').GetValue(i)
				eta2 = event.GetLeaf('Muon.Eta').GetValue(i)
				phi2 = event.GetLeaf('Muon.Phi').GetValue(i)

				# print('Muon 1: pt:', pt1, 'eta:', eta1, 'phi:', phi1)
				# print('Muon 2: pt:', pt2, 'eta:', eta2, 'phi:', phi2)
				# print('\n')

				muon1.SetPtEtaPhiM(pt1, eta1, phi1, 0.1)
				muon2.SetPtEtaPhiM(pt2, eta2, phi2, 0.1)

				h1.Fill(calculateInvariantMass(muon1, muon2))

				muonCounter = 0

h1.Draw()

		