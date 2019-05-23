fp = 'muons.txt'
m1string = ''
m2string = ''
allValuesSet = False

with open(fp) as file:
    for i, line in enumerate(file):
        if line.startswith('Run'):
            identifier = line.strip()
            currentLine = i
            allValuesSet = False
        elif i == currentLine + 2:
            m1string = line
        elif i == currentLine + 3:
            m2string = line
        elif i == currentLine + 4:
            allValuesSet = True

        if allValuesSet :
            split_m1 = m1string.split(' ')
            m1pt = split_m1[2]
            m1eta = split_m1[3]
            m1phi = split_m1[4]
            m1mass = split_m1[5]

            split_m2 = m2string.split(' ')
            m2pt = split_m2[2]
            m2eta = split_m2[3]
            m2phi = split_m2[4]
            m2mass = split_m2[5]

            print(identifier)
            print(m1pt, m1eta, m1phi, m1mass)
            print(m2pt, m2eta, m2phi, m2mass)






