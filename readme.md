1.  Ladda ner en excel fil från fortnox med alla verifikat.
    a. När du är inloggad på bokföringssidan, klicka på ”rapporter” i övre högra hörnet, [se fig](https://imgur.com/UF91b3S)
    b. Klicka på ”verifikationslista”, [se fig](https://imgur.com/zBlvf3m)
    c. Klicka i ”en serie”, välj er och klicka på ”export excel”, [se fig](https://imgur.com/hJwIQ0u)
2.  Konvertera den till CSV med ett passande namn och titta vilken delimeter(vad som är emellan varje fält, '\t', ';'...) som används.
3.  Kör programmet med "python remakecsv.py” och följ instruktionerna
4.  Detta genererar en ny csv fil med namnet "report_remake.csv"
5.  Ladda upp report_remake.csv till google sheets.
6.  Välj hela kolumnen bokföringsdatum (genom att klicka ovanför). (Se gif)
7.  Klicka på ”Format” (Se gif)
8.  Välj ”Number” och sedan klicka i ”Plaintext” (Se gif)
    ![magic gif](https://imgur.com/f8fc0d60-6350-4b43-b5f8-ec8a369bb68a "Magic gif")

9)  Ladda nu ner filen i formatet ”.xlsx” (Excel)
10) Ladda ner och starta Bulkpdf, Om du har mac se A)
11) ”Load from config”
12) Kör!
13) Done

## A)

Bulkpdf finns bara för windows vilket gör att du har ett flertal alternativ.

1.  Hitta en windows dator (typ datorerna på Chalmers)
2.  installera "wine" vilket gör att du kan köra windows program utan installera windows ([Guide här](https://www.davidbaumgold.com/tutorials/wine-mac/)
3.  Be en kompis som har windows köra programmet åt dig
4.  Installera/använd en windows partition på din mac (finns gratis windows från chalmers)
