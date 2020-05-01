from ROOT import TFile, TH1F, TLorentzVector, TCanvas, TLegend

# read file and instantiate tree
f = TFile('tag_1_delphes_events.root', 'read')
textFile = open('trueAndDetectorFourVectors.txt', 'w')
tree = f.Delphes

ptHistD = TH1F('pt', 'pt Differences Histogram', 100, 0, 100)
ptHistT = TH1F('pt', 'pt Differences Histogram', 100, 0, 100)

ptHistT.SetLineColor(2)
ptHistT.SetAxisRange(0, 3000, 'Y')
ptHistD.SetAxisRange(0, 3000, 'Y')

etaHistD = TH1F('eta', 'eta Differences Histogram', 100, -10, 10)
etaHistT = TH1F('eta', 'eta Differences Histogram', 100, -10, 10)

etaHistT.SetLineColor(2)
etaHistT.SetAxisRange(0, 3000, 'Y')
etaHistD.SetAxisRange(0, 3000, 'Y')

phiHistD = TH1F('phi', 'phi Differences Histogram', 100, -10, 10)
phiHistT = TH1F('phi', 'phi Differences Histogram', 100, -10, 10)

phiHistT.SetLineColor(2)
phiHistT.SetAxisRange(0, 3000, 'Y')
phiHistD.SetAxisRange(0, 3000, 'Y')

c1 = TCanvas('c1', 'ptC')
c2 = TCanvas('c2', 'etaC')
c3 = TCanvas('c3', 'phiC')

muon1 = TLorentzVector()
muon2 = TLorentzVector()

detectorFourVector = list()
trueFourVector = list()

dCount = 0
tCount = 0

def calculateInvariantMass(muon1, muon2):
    # add the muons
    newParticle = muon1 + muon2

    # return mass of new particle
    return (newParticle.M())
	
for event in tree:

	for i, particle in enumerate(event.Particle):

		if abs(event.GetLeaf('Particle.PID').GetValue(i)) == 13.0:

			tCount += 1

			trueFourVector = (event.GetLeaf('Particle.PT').GetValue(i), event.GetLeaf('Particle.Eta').GetValue(i),
				event.GetLeaf('Particle.Phi').GetValue(i), 0.1)

			ptHistT.Fill(trueFourVector[0])
			etaHistT.Fill(trueFourVector[1])
			phiHistT.Fill(trueFourVector[2])


	for i, muon in enumerate(event.Muon):

		if (tree.GetLeaf('Muon_size').GetValue(i) == 2):

			dCount += 1

			detectorFourVector = (event.GetLeaf('Muon.PT').GetValue(i), event.GetLeaf('Muon.Eta').GetValue(i),
				event.GetLeaf('Muon.Phi').GetValue(i), 0.1)

			ptHistD.Fill(detectorFourVector[0])
			etaHistD.Fill(detectorFourVector[1])
			phiHistD.Fill(detectorFourVector[2])


c1.cd()
ptHistD.Draw()
ptHistT.Draw('same')
c1.Update()

c2.cd()
etaHistD.Draw()
etaHistT.Draw('same')
c2.Update()

c3.cd()
phiHistD.Draw()
phiHistT.Draw('same')
c3.Update()