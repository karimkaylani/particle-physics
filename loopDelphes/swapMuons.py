from ROOT import TFile, TH1F, TLorentzVector, TCanvas, TLegend

# read file and instantiate tree
f = TFile('tag_1_delphes_events.root', 'read')
textFile = open('trueAndDetectorFourVectors.txt', 'w')
tree = f.Delphes

ptHist = TH1F('pt', 'pt Differences Histogram', 100, -10, 100)
etaHist = TH1F('eta', 'eta Differences Histogram', 100, -2, 10)
phiHist = TH1F('phi', 'phi Differences Histogram (w/Swapped)', 100, -2, 10)

c1 = TCanvas('c1', 'pt')
c2 = TCanvas('c2', 'eta')
c3 = TCanvas('c3', 'phi')

detectorFourVector = list()
trueFourVector = list()

tMuonCounter = 0
dMuonCounter = 0

pTrueVector = list()
nTrueVector =list()

pDetectorVector = list()
nDetectorVector =list()

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
	
for event in tree:

	for i, particle in enumerate(event.Particle):

		if abs(event.GetLeaf('Particle.PID').GetValue(i)) == 13.0:

			tMuonCounter += 1

			if (tMuonCounter == 1):

				pTrueVector = (event.GetLeaf('Particle.PT').GetValue(i), event.GetLeaf('Particle.Eta').GetValue(i),
				event.GetLeaf('Particle.Phi').GetValue(i), 0.1)

				trueFourVector = pTrueVector

			else:

				nTrueVector = (event.GetLeaf('Particle.PT').GetValue(i), event.GetLeaf('Particle.Eta').GetValue(i),
				event.GetLeaf('Particle.Phi').GetValue(i), 0.1)

				trueFourVector = nTrueVector

				tMuonCounter = 0


	for i, muon in enumerate(event.Muon):

		if (tree.GetLeaf('Muon_size').GetValue(i) == 2):

			dMuonCounter += 1

			if (dMuonCounter == 1):

				pDetectorVector = (event.GetLeaf('Muon.PT').GetValue(i), event.GetLeaf('Muon.Eta').GetValue(i),
				event.GetLeaf('Muon.Phi').GetValue(i), 0.1)

				detectorFourVector = pDetectorVector

			else:

				nDetectorVector = (event.GetLeaf('Muon.PT').GetValue(i), event.GetLeaf('Muon.Eta').GetValue(i),
				event.GetLeaf('Muon.Phi').GetValue(i), 0.1)

				detectorFourVector = nDetectorVector

				dMuonCounter = 0


	if (len(trueFourVector) != 0 and len(detectorFourVector) != 0):
		
		phiDiff = abs(trueFourVector[0] - detectorFourVector[0])

		if phiDiff > 2:

			if (dMuonCounter == 0):
				detectorFourVector = pDetectorVector

			elif (dMuonCounter == 1):
				detectorFourVector = nDetectorVector

			if (tMuonCounter == 0):
				trueFourVector = pTrueVector

			elif (tMuonCounter == 1):
				trueFourVector = nTrueVector

		print(trueFourVector)
		print(detectorFourVector)
		print('\n')

		plotPoints(trueFourVector, detectorFourVector)

drawHistograms()
