from ROOT import *

# read file and instantiate tree
f = TFile('tag_1_delphes_events.root', 'read')
tree = f.Delphes
h1 = TH1F('h1', 'Invariant Mass Histogram', 100, 0, 500)

muonCounter = 0
count = 0

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
		count +=1

		if (muonCounter == 1):
			pt1 = event.GetLeaf('Muon.PT').GetValue()
			eta1 = event.GetLeaf('Muon.Eta').GetValue()
			phi1 = event.GetLeaf('Muon.Phi').GetValue()

		else:
			pt2 = event.GetLeaf('Muon.PT').GetValue()
			eta2 = event.GetLeaf('Muon.Eta').GetValue()
			phi2 = event.GetLeaf('Muon.Phi').GetValue()

			#print('Muon 1: pt:', pt1, 'eta:', eta1, 'phi:', phi1)
			#print('Muon 2: pt:', pt2, 'eta:', eta2, 'phi:', phi2)
			#print('\n')


			muon1.SetPtEtaPhiM(pt1, eta1, phi1, 0.1)
			muon2.SetPtEtaPhiM(pt2, eta2, phi2, 0.1)

			muonCounter = 0


	print(event.GetLeaf('Particle.PID').GetValue())

	if event.GetLeaf('Particle.PID').GetValue() == 13 or event.GetLeaf('Particle.PID').GetValue() == -13:
		print('hello')

