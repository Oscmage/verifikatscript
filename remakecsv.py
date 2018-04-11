# This Python file uses the following encoding: utf-8


import csv
with open('work.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    cVrNumb = ''
    cVrLine = ''
    currentTotalSum = 0
    countVrWithSame = 1
    allLines = []
    allLines.append('Vernr;Bokföringsdatum;Registreringsdatum;Konto;Benämning;Ks;Projnr;Verifikationstext;Transaktionsinfo;Debet;Kredit\r\n')
    for rowNbr, row in enumerate(reader):
        if rowNbr >= 2 :
            '''
            print ''
            print row
            for v in row:
                print v,

            print ''
            print 'After'
            print ''
            '''
            # Do we have same ver number?, if yes continue adding info to the string and the total sum
            # If not, change currentVrLine, create new string and currentTotalSum to zero
            for i, val in enumerate(row):
                if i == 0: #Vernum
                    if val != cVrNumb and cVrNumb != '':
                        allLines.append(cVrLine +  '\r\n')
                        cVrNumb = val # Update the current vr number
                        cVrLine = val # Update the current string to empty it
                        currentTotalSum = 0
                        countVrWithSame = 1
                    else:
                        countVrWithSame += 1
                if i == 1: #Bokföringsdatum
                    cVrLine += ';' + val
                if i == 2: #Registreringsdatum
                    cVrLine += ';' + val
                if i == 3: #Konto
                    cVrLine += ';' + val
                if i == 4: #Benämning
                    cVrLine += ';' + val
                if i == 5: #Kostnadsställe (Ks)
                    cVrLine += ';' + val
                if i == 6: #Projnr
                    cVrLine += ';' + val
                if i == 7: #Verifikationstext
                    cVrLine += ';' + val
                if i == 8: #Transaktionsinfo
                    cVrLine += ';' + val
                if i == 9: #Debet
                    val = val.replace(',','.')
                    if val != '':
                        currentTotalSum += float(val)
                    cVrLine += ';' + val
                if i == 10: #Kredit
                    cVrLine += ';' + val   
    allLines.append(cVrLine)
    out = csv.writer(open("myfile.csv","w"), delimiter=';',quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    out.writerow(allLines)


                                



