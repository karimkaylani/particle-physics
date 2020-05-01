from ROOT import TFile, TH1F, TLorentzVector, TCanvas, TLegend

# read file and instantiate tree
f = TFile('tag_1_delphes_events.root', 'read')
textFile = open('trueAndDetectorFourVectors.txt', 'w')
tree = f.Delphes

ptHist = TH1F('pt', 'pt Differences Histogram', 100, -10, 100)
etaHist = TH1F('eta', 'eta Differences Histogram', 100, -2, 10)
phiHist = TH1F('phi', 'phi Differences Histogram', 100, -2, 10)

c1 = TCanvas('c1', 'pt')
c2 = TCanvas('c2', 'eta')
c3 = TCanvas('c3', 'phi')

muon1 = TLorentzVector()
muon2 = TLorentzVector()

detectorFourVector = list()
trueFourVector = list()

def plotPoints(t4vect, d4vect):
	#make sure values are not null
	if (len(t4vect) != 0 and len(d4vect) != 0):

		#fill with differences
		ptHist.Fill(abs(t4vect[0] - d4vect[0]))
		etaHist.Fill(abs(t4vect[1] - d4vect[1]))
		phiHist.Fill(abs(t4vect[2] - d4vect[2]))

def drawHistograms():

	c1.cd()
	ptHist.Draw()
	c1.Update()

	c2.cd()
	etaHist.Draw()
	c2.Update()

	c3.cd()
	phiHist.Draw()
	c3.Update()
	
for x, event in enumerate(tree):

	for i, particle in enumerate(event.Particle):

		if abs(event.GetLeaf('Particle.PID').GetValue(i)) == 13.0:

			trueFourVector = (event.GetLeaf('Particle.PT').GetValue(i), event.GetLeaf('Particle.Eta').GetValue(i),
				event.GetLeaf('Particle.Phi').GetValue(i), 0.1)


	for i, muon in enumerate(event.Muon):

		if (tree.GetLeaf('Muon_size').GetValue(i) == 2):

			detectorFourVector = (event.GetLeaf('Muon.PT').GetValue(i), event.GetLeaf('Muon.Eta').GetValue(i),
				event.GetLeaf('Muon.Phi').GetValue(i), 0.1)

	if (len(trueFourVector) != 0 and len(detectorFourVector) != 0):
	
		plotPoints(trueFourVector, detectorFourVector)

drawHistograms()
