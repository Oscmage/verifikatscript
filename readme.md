1.  Ladda ner en excel fil från fortnox med alla verifikat.

    1.  När du är inloggad på bokföringssidan, klicka på ”rapporter” i övre högra hörnet, ![se fig](https://i.imgur.com/UF91b3S.png)

    2.  Klicka på ”verifikationslista”, ![se fig](https://i.imgur.com/zBlvf3m.png)
    3.  Klicka i ”en serie”, välj er och klicka på ”export excel”, <img src="https://i.imgur.com/hJwIQ0u.png" alt="Drawing" style="max-width: 200px;"/>

2.  Konvertera den till CSV (genom att använda numbers i mac, eller google sheets) med ett passande namn och titta vilken delimeter(vad som är emellan varje fält, '\t', ';'...) som används.
3.  Kör programmet med "python remakecsv.py” och följ instruktionerna
4.  Detta genererar en ny csv fil med namnet "report_remake.csv"
5.  Ladda upp report_remake.csv till google sheets.
6.  Välj hela kolumnen bokföringsdatum (genom att klicka ovanför). (Se gif)
7.  Klicka på ”Format” (Se gif)
8.  Välj ”Number” och sedan klicka i ”Plaintext” (Se gif)
    ![magic gif](https://media.giphy.com/media/5T05wrxI4QvpBhBI6Z/giphy.gif "Magic gif")
9.  Ladda nu ner filen i formatet ”.xlsx” (Excel) "File" -> "Download as" -> "Microsoft Excel (.xlsx)"
10. [Ladda ner](https://bulkpdf.de/en) och starta Bulkpdf, Om du har mac se A)
11. ”Load from config”
12. Kör!
13. Done

## A)

Bulkpdf finns bara för windows vilket gör att du har ett flertal alternativ.

1.  Hitta en windows dator (typ datorerna på Chalmers)
2.  Installera "wine" vilket gör att du kan köra windows program utan installera windows ([Guide här](https://www.davidbaumgold.com/tutorials/wine-mac/)
3.  Be en kompis som har windows köra programmet åt dig
4.  Installera/använd en windows partition på din mac (finns gratis windows från chalmers)
