# This Python file uses the following encoding: utf-8

import csv
import colnames
import sys

def main(file_name, delim):

    with open(file_name, 'rb') as f:
        reader = csv.reader(f, delimiter=delim)
        out = csv.writer(open("report_remake.csv","w"), delimiter='\t', lineterminator='\r\n')
        writeHeaders(out)

        cVrNumb = ''
        cVrLine = {}
        totalSum = 0
        countVrWithSame = 1
        passedHeaders = False
        numberOfVers = 0                
        for rowNbr, row in enumerate(reader):
            if not passedHeaders: # Data comes after header so read lines until we find header.
                if row[0].find('Vern') != -1:
                    passedHeaders = True
            else:
                for i, val in enumerate(row):
                    if i == 0: #Vernum
                        if val != cVrNumb:
                            if numberOfVers != 0:
                                write(totalSum, cVrLine, out)
                            cVrNumb = val
                            cVrLine = {}
                            cVrLine[colnames.vernr] = val
                            totalSum = 0
                            countVrWithSame = 1
                            numberOfVers += 1
                        else:
                            countVrWithSame += 1
                    if i == 1 and countVrWithSame == 1: #Bokföringsdatum
                        cVrLine[colnames.bok] = val
                    if i == 2 and countVrWithSame == 1: #Registreringsdatum
                        cVrLine[colnames.reg] = val
                    if i == 3: #Konto
                        cVrLine[colnames.konto + str(countVrWithSame)] = val
                    if i == 4: #kontonamn
                        cVrLine[colnames.kontonamn + str(countVrWithSame)] = val                
                    if i == 5: #Kostnadsställe (Ks)
                        cVrLine[colnames.ks + str(countVrWithSame)] = val
                    if i == 6 and countVrWithSame == 1: #Projnr
                        cVrLine[colnames.projnr] = val
                    if i == 7 and countVrWithSame == 1: #Verifikationstext
                        cVrLine[colnames.vertext] = val
                    if i == 8 and countVrWithSame == 1: #Transaktionsinfo
                        cVrLine[colnames.traninf] = val
                    if i == 9: #Debet
                        if val != '':
                            totalSum += float(val.replace(',','.'))
                        cVrLine[colnames.debet + str(countVrWithSame)] = val
                    if i == 10: #Kredit
                        cVrLine[colnames.kredit + str(countVrWithSame)] = val
        write(totalSum, cVrLine, out)

def write(totalSum, cVrLine, out):
    array = []
    array.append(cVrLine.get(colnames.vernr) if cVrLine.get(colnames.vernr) else '')
    array.append(cVrLine.get(colnames.vertext) if cVrLine.get(colnames.vertext) else '')
    array.append(cVrLine.get(colnames.traninf) if cVrLine.get(colnames.traninf) else '')
    array.append(cVrLine.get(colnames.bok) if cVrLine.get(colnames.bok) else '')
    array.append(cVrLine.get(colnames.reg) if cVrLine.get(colnames.reg) else '')
    array.append(cVrLine.get(colnames.projnr) if cVrLine.get(colnames.projnr) else '')

    for name in [colnames.konto, colnames.kontonamn, colnames.ks, colnames.debet, colnames.kredit]:
        for j in range(1,7):
            array.append(cVrLine.get(name + str(j)) if cVrLine.get(name + str(j)) else '')
    array.append(str(totalSum).replace('.',','))
    out.writerow(array)

def writeHeaders(out):
    ret = [colnames.vernr, colnames.vertext, colnames.traninf, colnames.bok, colnames.reg, colnames.projnr]
    for name in [colnames.konto, colnames.kontonamn, colnames.ks, colnames.debet, colnames.kredit]:
        for j in range(1,7):
            ret.append(name + str(j))
    ret.append(colnames.total)

    out.writerow(ret)

def getUserInput():
    file_name = input('Please enter the csv filename that you want to convert (eg. "myfile.csv"): \n')
    delimeter = input('Please enter the delimeter used for the csv file (eg. ";", if the file uses tab write backslash t) \n')
    return file_name, delimeter

if __name__ == '__main__':
    #main()
    f_name, delim = getUserInput()
    main(f_name, delim)
