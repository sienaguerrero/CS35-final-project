from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter
import csv, datetime 
from bokeh.models import DatetimeTickFormatter, Title, BasicTickFormatter 

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
            newDate = datetime.datetime.strptime(tup[0], '%Y-%m-%d').strftime('%m/%Y')
            datetimeDate = datetime.datetime.strptime(newDate, '%m/%Y')
            if datetimeDate.month == 6 or datetimeDate.month == 7:
                newList.append((datetimeDate.year, tup[1]))
        else:
            newDate = datetime.datetime.strptime(tup[0], '%d/%m/%y').strftime('%m/%Y')
            datetimeDate = datetime.datetime.strptime(newDate, '%m/%Y')
            if datetimeDate.month == 6 or datetimeDate.month == 7:
                newList.append((datetimeDate.year, tup[1]))

    return newList


def doAllTheWork(filename = "GlobalLandTemperaturesByCountry.csv"):
    L = getTemps(filename)
    N = convertDate(L)
    dateList = []
    tList = []
    for tup in N:
        try:
            tList.append(float(tup[1]))
            dateList.append(tup[0])
        except:
            continue
    output_file("pratplot.html")
    p = figure(plot_width=600, plot_height=250, x_axis_type="datetime")

    p.circle(dateList, tList, radius=0.1, alpha=0.5)

    p.xaxis.formatter=BasicTickFormatter()
    show(p)