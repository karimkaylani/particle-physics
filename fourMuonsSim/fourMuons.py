from ROOT import TFile, TH1F, TLorentzVector, TCanvas

f = TFile('tag_1_delphes_events.root', 'read')
tree = f.Delphes

muon1 = TLorentzVector()
muon2 = TLorentzVector()
muon3 = TLorentzVector()
muon4 = TLorentzVector()

zBoson1 = TLorentzVector()
zBoson2 = TLorentzVector()

vectList = list()

def getFourVector(zBoson):

	return [zBoson.Pt(), zBoson.Eta(), zBoson.Phi(), zBoson.M()]

def reconstruct(muon1, muon2, muon3, muon4):

	zBoson1 = muon1 + muon2
	zBoson2 = muon3 + muon4

	print('zBoson1: ' + str(getFourVector(zBoson1)))
	print('zBoson2: ' + str(getFourVector(zBoson2)))
	print('\n')


for event in tree:

	for i, particle in enumerate(event.Particle):

		if abs(event.GetLeaf('Particle.PID').GetValue(i)) == 13.0:

			vectList.append([event.GetLeaf('Particle.PT').GetValue(i), event.GetLeaf('Particle.Eta').GetValue(i),
			event.GetLeaf('Particle.Phi').GetValue(i), 0.1])

		if (len(vectList) == 4):

			sortedList = sorted(vectList)
			vectList[:] = []

	muon1.SetPtEtaPhiM(sortedList[0][0], sortedList[0][1], sortedList[0][2], sortedList[0][3])
	muon2.SetPtEtaPhiM(sortedList[1][0], sortedList[1][1], sortedList[1][2], sortedList[1][3])
	muon3.SetPtEtaPhiM(sortedList[2][0], sortedList[2][1], sortedList[2][2], sortedList[2][3])
	muon4.SetPtEtaPhiM(sortedList[3][0], sortedList[3][1], sortedList[3][2], sortedList[3][3])

	reconstruct(muon1, muon2, muon3, muon4)