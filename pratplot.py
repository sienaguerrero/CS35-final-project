
import csv, datetime  

filename = "GlobalLandTemperaturesByCountry.csv"

def getTemps(filename = "GlobalLandTemperaturesByCountry.csv"):

    List_of_rows = [] 
    try:
        csvfile = open( filename , newline='' )  # open for reading
        csvrows = csv.reader( csvfile )              # creates a csvrows object

        for row in csvrows:
            if row[3] == "Chile":
                List_of_rows.append((row[0], row[1]))


    except FileNotFoundError as e:
            print("File not found: ", e)
            return []

    return List_of_rows

def convertDate(tempList):
    newList = []
    for tup in tempList:
        if "-" in tup[0]:
            newDate = datetime.datetime.strptime(tup[0], '%Y-%m-%d').strftime('%m/%d/%Y')
            newList.append((newDate, tup[1]))
        else:
            newDate = datetime.datetime.strptime(tup[0], '%d-%m-%y').strftime('%m/%d/%Y')
            newList.append(tup[0],tup[1])

    return newList


def doAllTheWork(filename = "GlobalLandTemperaturesByCountry.csv"):
    L = getTemps(filename)
    N = convertDate(L)
    dateList = []
    tList = []
    for tup in N:
        dateList.append(tup[0])
        tList.append(tup[1])
    
    return dateList, tList