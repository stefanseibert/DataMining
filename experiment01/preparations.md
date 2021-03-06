#Fragen zum ersten Versuch

##Allgemein:

**Erklären Sie den Sinn der Transformation innerhalb der Data Mining Prozesskette.**

- Vorbereiten der Daten: Reduktion durch Selection + Normalisierung

> Ziel der Transformation ist es durch Reduktion oder Projektion die Anzahl der Attribute, mit welchen die Datensätze beschrieben werden, zu reduzieren. Abhängig von der jeweiligen Aufgabe und der im folgenden Prozessschritt verwendeten Lernmethode werden Atrribute die keinen oder nur einen geringen Einfluss auf das Modell haben bestimmt und eliminiert. Sinn dieser Aufgabe ist nicht nur eine Reduktion der Komplexität der nachfolgenden Verarbeitungsschritte sondern auch eine bessere Mustererkennung bzw. Modellbestimmung. Neben der Attributreduktion werden zu diesem Prozessschritt auch vorverarbeitende Methoden wie die Normalisierung der Attribute gezählt.

**Worin besteht der Unterschied zwischen überwachtem und unüberwachtem Lernen.**

- überwacht:    Trainingsdaten enthalten sowohl Eingabewerte als auch Sollausgaben--> Klassifizierung, Regression
- unüberwacht:  Trainingsdaten enthalten nur Eingabewerte, es können nur Ähnlichkeiten festgestellt werden --> Clustering

**Beschreiben Sie die Unterschiede zwischen Klassifikation, Regression und Clustering. Nennen Sie für diese 3 verschiedenen Verfahren je ein Anwendungsbeispiel.**

- Klassifikation:

    - überwachtes Lernen: In den Testdaten wird jeder Eingabewert einer Sollausgabe zugeordnet.

    - Der Ausgabewert ist ein diskreter Wert, welcher die Zugehörikeit des Datensatzes zu einer bestimmten Klasse beschreibt.

    - Beispiel:     Videoüberwachung einer Produktionsstraße: Klassifikation in gut und schlechte Qualität der Produkte

- Regression: 
    - überwachtes Lernen: In den Testdaten wird jeder Eingabewert einer Sollausgabe zugeordnet.

    - Das Ausgabeattribut ist eine Funktion, die jedem Eingabewert einen numerischen Ausgabewert zuordnet.

    - Beispiel:     Trainingsdaten: Temperaturverlauf über mehrere Jahre, Ausgabewert: mögliche Temperatur an einem bestimmten Tag. 

- Clustering:
    - unüberwachtes Lernen: Die Testdaten bestehen nur aus eingabewerten. 

    - Das gelernte Clustering partitioniert die Trainingsdaten derart in Untergruppen, dass Datensätze innerhalb einer Untergruppe untereinander sehr ähnlich sind, Datensätze unterschiedlicher Gruppen jedoch nur ein geringes Maÿ an Ähnlichkeit aufweisen.

    - Beispiel: Feststellen der Ähnlichkeit des Surfverhaltens verschiedener Nutzer



##Python

**Was ist eine Python List-Comprehension?**

Methode um Listen zu erstellen: 
statt die Liste über eine Schleife mit den nötigen Daten zu füllen, gibt es eine kompaktere und lesbarere Schreibweise:
    
    >>> list = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    >>> list
    [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

**Wie importiert man Daten aus einem Textfile?**

    results = []
    with open('inputfile.txt') as inputfile:
        for line in inputfile:
            results.append(line.strip().split(','))

**Wie speichert man Daten aus Python in ein Textfile?**

    with open('inputfile.txt') as outputfile:
        outputfile.write("line to append")

**Wie hängt man an eine Python-Liste die Elemente einer zweiten Liste an? - extend Methode**

    >>> l1 = [1, 2, 3]
    >>> l1
    [1,2,3]
    >>> l2 = [4, 5]
    >>> l1.extend(l2)
    >>> l1
    [1,2,3,4,5]


##Numpy

**Nennen Sie zwei verschiedene Möglichkeiten ein Numpy-Array zu erzeugen.**

    >>> from numpy import *
    >>> a = array( [2, 3, 4] )
    >>> print a
    [2 3 4]
    >>> b = arange(10)
    >>> print b 
    [0 1 2 3 4 5 6 7 8 9]

**Wie legt man ein (3, 4)-Array mit ausschließlich 0-Einträgen an?**

    >>> a = zeros( (3,4) ) 
    >>> a 
    [[0.  0.  0.  0.],
     [0.  0.  0.  0.],
     [0.  0.  0.  0.]]

**Wie ruft man die Anzahl der Dimensionen, die Anzahl der Elemente pro Dimension und den Datentyp der Arrayelemente ab?**

- Anzahl der Dimensionen:   

        ndarray.ndim
    
- Anzahl der Elemente pro Dimension:

        ndarray.shape  #(gibt Tupel zurück, das die Anzahl der Elemente in jeder Dimension angibt (z.B. (3,5) ))
    
- Datentyp der Arrayelemente:

        ndarray.dtype

**Wie wandelt man ein (3, 4)-Array in ein (2, 6)-Array um?**

    >>> a = arange(12).reshape(3,4)             # 3x4 Matrix
    >>> print a
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    >>> a = a.reshape(2,6)                      # reshape wandelt die Matrix a in eine 2x6 Matrix um
    >>> print a
    [[ 0  1  2  3  4  5]
     [ 6  7  8  9 10 11]]

**Wie transponiert man ein zweidimensionales Array?**

    >>> a = array([[1,2,3],[4,5,6]])
    >>> print a
    [[1 2 3]
     [4 5 6]]
    >>> b = a.transpose()
    >>> print b
    [[1 4]
     [2 5]
     [3 6]]

**Wie multipliziert man zwei Arrays elementweise?**

    >>> a = array( [[1,1],
    ...             [0,1]] )
    >>> b = array( [[2,0],
    ...             [3,4]] )
    >>> a*b                         # Elementweises Produkt
    array([[2, 0],
           [0, 4]])

**Wie führt man eine Matrixmultiplikation zweier zweidimensionaler Arrays A und B aus? Welche Bedingungen müssen A und B erfüllen, damit überhaupt eine Matrixmultiplikation durchgeführt werden kann?**

    >>> a = array( [[1,1],
    ...             [0,1]] )
    >>> b = array( [[2,0],
    ...             [3,4]] )
    >>> dot(a,b)                    # matrix product
    array([[5, 4],
           [3, 4]])

Damit die Multiplikation möglich ist, muss die Spaltenanzahl in a der Zeilenanzahl in b entsprechen, selbes muss für die Zeilenanzahl in a der Spaltenanzahl in b gelten.

**Wie greift man auf das Element (2, 3) in einem (4, 4)-Array A zu? Wie greift man auf die erste Spalte, wie auf die erste Zeile dieses Arrays zu?**

    >>> a = arange(12).reshape(2,6)
    >>> print a
    [[ 0  1  2  3  4  5]
     [ 6  7  8  9 10 11]]
    >>> print a[1][2]
    8

**Wie berechnet man die Quadratwurzel aller Elemente eines Arrays?**

    >>> a = array( [ (1,4,9), (16,25,36) ] )
    >>> print a
    [[ 1  4  9]
     [16 25 36]]
    >>> print sqrt(a)
    [[ 1.  2.  3.]
     [ 4.  5.  6.]]

**Wie legt man eine flache Kopie, wie eine tiefe Kopie eines Arrays an?**
    
    >>> a = array( [ (1,4,9), (16,25,36) ] )

    Flache Kopie:
    >>> c = a.view()

    Tiefe Kopie: 
    >>> d = a.copy() 

##Pandas

**Wie wird ein Numpy-Array in einen Pandas-Dataframe geschrieben? Wie legt man dabei die Spaltenbezeichnungen und einen Index an?**

    >>> a = arange(24).reshape(6,4)                                                 # legt ein Numpy-Array der Größe 6x4 an und füllt es mit den Zahlen von 0 bis 23
    >>> a
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]
     [12 13 14 15]
     [16 17 18 19]
     [20 21 22 23]]
    >>> dates = pandas.date_range('20130101',periods=6)                             # Legt eine Pandas-Series an, welche die Daten vom 2013-01-01 bis zum 2013-01-06 enthält.

    >>> dataframe = pandas.DataFrame( a , index=dates , columns=list('ABCD') )      # Legt ein Pandas-Dataframe an, dass die Series 'dates' als Index und A, B, C und D als 
                                                                                    # Spaltenbezeicnung erhält. Dem Dataframe wird das Array 'a' als Daten übergeben. 
    >>> dataframe
                 A   B   C   D
    2013-01-01   0   1   2   3
    2013-01-02   4   5   6   7
    2013-01-03   8   9  10  11
    2013-01-04  12  13  14  15
    2013-01-05  16  17  18  19
    2013-01-06  20  21  22  23
    [6 rows x 4 columns]

**Wie kann auf einzelne Spalten, wie auf einzelne Zeilen eines Pandas Dataframes zugegriffen werden?**
    
    >>> dataframe['A']                                                              # Printed nur die Indizes und die selektierte Spalte 'A' des Dataframes.
    2013-01-01     0                                                                # Äquivalent kann auch dataframe.A verwendet werden.
    2013-01-02     4                                                                # Der Rückgabewert ist eine Pandas-Series.
    2013-01-03     8
    2013-01-04    12
    2013-01-05    16
    2013-01-06    20
    Freq: D, Name: A, dtype: int32

    >>> dataframe[1:2]                                                              # Gibt die Zeile mit dem numerischen Index 1 zurück.          
                A  B  C  D                                                          # Der Rückgabewert ist ein Pandas-Dataframe.
    2013-01-02  4  5  6  7
    [1 rows x 4 columns]

    >>> dataframe['20130102':'20130104']                                            # Gibt die Zeilen mit den Indizes zwischen 2013-01-02 und 2013-01-04 zurück
                 A   B   C   D                                                      # Der Rückgabewert ist ein Pandas-Dataframe
    2013-01-02   4   5   6   7
    2013-01-03   8   9  10  11
    2013-01-04  12  13  14  15

    [3 rows x 4 columns]

    >>> dataframe.loc[dates[0]]                                                     # Gibt die Zeile mit dem numerischen Index 0 zurück
    A    0                                                                          # Der Rückgabewert ist eine Panda-Series.
    B    1
    C    2
    D    3
    Name: 2013-01-01 00:00:00, dtype: int32

**Wie können Pandas Dataframes sortiert werden?**

    >>> dataframe.sort_index(axis = 0, ascending = False)                           # Sortiert nach Indizebezeichnung (axis = 0) absteigend
                 A   B   C   D
    2013-01-06  20  21  22  23
    2013-01-05  16  17  18  19
    2013-01-04  12  13  14  15
    2013-01-03   8   9  10  11
    2013-01-02   4   5   6   7
    2013-01-01   0   1   2   3

    [6 rows x 4 columns]

    >>> dataframe.sort_index(axis = 1, ascending = False)                           # Sortiert nach Spaltenbezeichnung (axis = 1) absteigend
                 D   C   B   A
    2013-01-01   3   2   1   0
    2013-01-02   7   6   5   4
    2013-01-03  11  10   9   8
    2013-01-04  15  14  13  12
    2013-01-05  19  18  17  16
    2013-01-06  23  22  21  20

    [6 rows x 4 columns]

    >>> dataframe.sort(columns='C', ascending=False)                                # Sortiert nach den Values in Spalte C absteigend
                 A   B   C   D                                                      # (Macht in diesem Fall nicht viel Sinn, da das Dataframe mit einer kontinuierlichen numerischen reihe 
    2013-01-06  20  21  22  23                                                      # gefüllt ist...)
    2013-01-05  16  17  18  19
    2013-01-04  12  13  14  15
    2013-01-03   8   9  10  11
    2013-01-02   4   5   6   7
    2013-01-01   0   1   2   3

    [6 rows x 4 columns]

**Wie kann zu einem bestehenden Dataframe eine neue Spalte hinzugefügt werden?**

    >>> newCol = pandas.Series([1,2,3,4,5,6],index=pandas.date_range('20130102',periods=6))         # Erstellt neues Dataframe mit den Daten von 2013-01-02 bis 2013-01-07 als Indizes
    >>> newCol
    2013-01-02    1
    2013-01-03    2
    2013-01-04    3
    2013-01-05    4
    2013-01-06    5
    2013-01-07    6
    Freq: D, dtype: int64

    >>> dataframe['newColumn'] = newCol                                                             # Fügt dem alten Dataframe eine neue Spalte 'newColumn' hinzu.
                 A   B   C   D  newColumn                                                           # Da die Spalte keinen Value für den Index 2013-01-01 besitzt, wird hier NaN angegeben
    2013-01-01   0   1   2   3        NaN                                                           # Der letzte Value beim Index 2013-01-07, den nur die neue Spalte besitzt wird 
    2013-01-02   4   5   6   7          1                                                           # abgeschnitten
    2013-01-03   8   9  10  11          2
    2013-01-04  12  13  14  15          3
    2013-01-05  16  17  18  19          4
    2013-01-06  20  21  22  23          5

    [6 rows x 5 columns]

**Wie werden Daten aus einem .csv File in einen Pandas Dataframe geschrieben?**

    >>> pandas.read_csv('filename.csv')

**Wie wird ein Pandas Dataframe in einem .csv File abgelegt?**

    >>> dataframe.to_csv('filedestination.csv')

## Matplotlib

**Wie erzeugt man mit Matplotlib einen Plot, wie er in Abbildung 4 dargestellt ist? ( Sinus function - dashed line)**

    >>> import matplotlib.pyplot as plt         # importiert matplotli.pyplot

    >>> x = numpy.arange(0, 7,0.1)              # setzt Intervall für x von 0 bis 7 in 0.1 Schritten

    >>> plt.plot(x, numpy.sin(x),'ro' )         # zeichnet den Sinus von x in roten (r) punkte (o)
    >>> plt.axis([0,7,-1,1])                    # Die y-Achse geht von -1 bis 1, die x-Achse von 0 bis 7
    >>> plt.title('Sinusfunktion')              
    >>> plt.ylabel('sin(x)')
    >>> plt.xlabel('x')
    >>> plt.grid(True)                          # zeichnet ein Raster
    >>> plt.show()                              # zeigt das Fenster mit dem erzeugten Plot

**Wie kann man mehrere Graphen in einen Plot eintragen?**

Zeichnet zwei Graphen untereinander (in zwei verschiedene Koordinatensysteme):
    
        (... wie oben ...)
        >>> plt.figure(1)

        >>> plt.subplot(2,1,1)                    # oberes Koordinatensystem  (Erklärung des Parameters: siehe unten)
        >>> plt.plot(x, np.sin(x),'ro')

        >>> plt.subplot(2,1,2)                    # unteres Koordinatensystem
        >>> plt.plot(x,'b')
        (... wie oben...)

Die Parameter der subplot-Funktion enthalten folgende Informationen:

die ersten zwei Ziffern beschreiben die Größe des Grids in dem sich der Subplot befindet (im Beispiel 2x1), die letzte Ziffer beschreibt, an welcher Stelle in diesem Grid sich 
der subplot befindet (der obere Subplot an Stelle 1, der untere an Stelle 2) .

Zeichnet zwei Graphen in ein Koordinatensystem: 

Einfach die plot-Funktion mehrmal mit unterschiedlichen parametern aufrufen.
        
        (... wie oben ...)

        >>> plt.plot(x, np.sin(x),'ro')
        >>> plt.plot(x,'b')

        (... wie oben ...)

        ODER: wie oben, nur in das selbe Koordinatensystem

        (... wie oben ...)
        >>> plt.subplot(2,1,2)                    # unteres Koordinatensystem im 2x2 Grid
        >>> plt.plot(x, np.sin(x),'ro')

        >>> plt.subplot(2,1,2)                    # ebenfalls unteres Koordinatensystem im 2x2 Grid
        >>> plt.plot(x,'b')
        (... wie oben...)

**Wie erzeugt man mit Matplotlib ein Bild, das 12 Subplots in 3 Zeilen und 4 Spalten geordnet, enthält.**

        >>> plt.figure(1)
        >>> plt.subplot(3, 4, 1)
        >>> plt.subplot(3, 4, 2)
        >>> plt.subplot(3, 4, 3)
        >>> plt.subplot(3, 4, 4)
        >>> plt.subplot(3, 4, 5)
        >>> plt.subplot(3, 4, 6)
        >>> plt.subplot(3, 4, 7)
        >>> plt.subplot(3, 4, 8)
        >>> plt.subplot(3, 4, 9)
        >>> plt.subplot(3, 4, 10)
        >>> plt.subplot(3, 4, 11)
        >>> plt.subplot(3, 4, 12)
        >>> plt.show()

**Wie erzeugt man mit Matplotlib ein Histogramm?**

        >>> mu, sigma = 100, 0.01
        >>> x = mu + sigma * np.random.randn(5000)          # erstellt numpy.array mit normalverteilten werten

        # the histogram of the data
        >>> plt.hist(x, 100,facecolor='r')                  # zeichnet ein Histogram mit den Werten von x in 100 rotenBalken

        >>> plt.show()                                      # zeigt das Fenster mit dem erzeugten Plot

**Wie erzeugt man mit Matplotlib einen Boxplot?**

    >>> boxplot( data, notch = 0, sym = '+', vert = 0, whis = 0.75 )
    
    parameter:
        data:               Daten, die angezeigt werden sollen
        notch:              Einkerbung am Meridian (default: false)
        sym:                Symbol für Ausreißer (default 'b+')
        vert:               Ausrichtung, 0 = horizontal, 1 = vertikal (default 1)
        whis:               Länge der Whisker (default 1.5)
        positions:          horizontale Position der Boxen (default 1)
        widths:             Breite der Boxen (default 0.5)



##Scipy

**Geben Sie kurz die Schritte an, die für die Durchführung eines hierarchischen Clustering mit Scipy notwendig sind.**

- Daten in ein NumPy Array schreiben

- berechnen der Distanz zwischen allen Einträgen (`scipy.spatial.distance`), dabei können verschiedene Distanzen berechnet werden (bsp.: `euclidean`, `hamming`,...)

- dann erstellt man die Linkage Matrix um die Distanzen der Einträge miteinander zu Clustern zu verknüpfen

- nun wird der ursprüngliche Datensatz entsprechend der Linkage Matrix sortiert

- die Cluster können nun auf unterschiedliche art und weise dargestellt werden (bsp. Heatmap, Dendrogramm)

##Scikit Learn

**Sklearn stellt u.a. eine umfassende Bibliothek von Klassen für das überwachte Lernen bereit. Mit welchem Methodenaufruf werden diese Kassen trainiert?**

    sklearn.svm.libsvm.fit()

Mit welchem Methodenaufruf können die trainierten Modelle auf neue Eingabedaten angewandt werden um den entsprechenden Ausgabewert zu berechnen?
        
    sklearn.svm.libsvm.predict()

**Mit welchem Leistungsmaß kann die Qualität eines Regressionsmodells bewertet werden?**

Leistungsmaß = Mittel zur Bestimmung der Qualität (der Güte) eines gelernten Modells.

Mean Square Error (MSE) oder Mean Absolute Difference (MAD) zwischen Vorhersage und Sollausgabe der Testdaten

**Wie wird dieses Leistungsmaß mit Sklearn berechnet?**

    metrics.mean_squared_error(predictedOutput,targets)

**Mit welchem Leistungsmaß kann die Qualität eines Klassifikationsmodells bewertet werden?**

Leistungsmaß = Mittel zur Bestimmung der Qualität (der Güte) eines gelernten Modells.
    --> Confusion matrix oder Classification report

**Wie wird dieses Leistungsmaß mit Sklearn berechnet?**

    metrics.confusion_matrix(expected, predicted)
    metrics.classification_report(expected, predicted)

**Was versteht man unter x-facher Kreuzvalidierung und wie wird diese mit Sklearn durchgeführt?**

Falls zu wenig Daten zur Verfügung stehen um kann dies durch die x-fache Kreuzvalidierung ausgeglichen werden. Hierbei werden die Daten in x Partitionen unterteilt, die jeweils disjunkt sind (typischerweise liegt x zwischen 4 und 10). Dann wird in x Iterationen ein Datensatz als Testdatensatz und alle weiteren als Trainingsdatensätze verwendet, sodass jeder Datensatz einmal fürs Testen genutzt wurde. Die Performance ergibt sich aus dem Durchschnitt aller Durchläufe.

In Sklearn werden Test und Training in die Funktion cros_val_score gekapselt. Als Parameter müssen der entsprechende Lernalgorithmus, die Anzahl der Partitionen und eine Funktion zur Berechnung der Performance (beispielsweise MSE (mean square error)) angegeben werden.
