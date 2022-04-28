def findIsogram(file):
    f1, f2, f3, f4 = file.readline(), file.readline(), file.readline(), file.readline()
    f1, f2, f3, f4 = str(f1), str(f2), str(f3), str(f4)
    splitedText = f1.split() + f2.split() + f3.split() + f4.split()
    keinIsogram = []

    i = 0
    while i < len(splitedText):
        wort = splitedText[i]
        wort = wort.lower()
        for j in range(0, len(wort)):
            if wort[j] in wort[(j+1):]:
                keinIsogram.append(wort)

        i += 1
    for k in keinIsogram:
        if k in splitedText:
            splitedText.remove(k)
    print("Liste der Wörter, die Isogram sind:",splitedText)

dateiName = open(r"C:\Users\yazan\Desktop\GPT_Aufgaben\gefunden.txt", "r")
findIsogram(dateiName)
















#def findIsogram(file):
 #   keinIsogram = []

  #  f = file.readline()
   # f = str(f)
    #splitedText = f.split()
    #print(splitedText)
    #i = 0
    #while i < len(splitedText):
     #   wort = splitedText[i]
      #  wort = wort.lower()
       # for j in range(0, len(wort)):
        #    if wort[j] in wort[(j+1):]:
         #       keinIsogram.append(wort)
          #      continue
        #i += 1
    #for k in keinIsogram:
     #   if k in splitedText:
      #      istIsogram = splitedText.remove(k)

 #   return istIsogram

#datei = open(r"C:\Users\yazan\Desktop\GPT_Aufgaben\gefunden.txt", "r")
#print(findIsogram(datei))












