
import csv 

filename = "GlobalLandTemperaturesByCountry.csv"

def getTemps(filename = "GlobalLandTemperaturesByCountry.csv")

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
