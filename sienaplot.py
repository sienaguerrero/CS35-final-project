import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter, Title, BasicTickFormatter
nan = float('nan')

Date = [1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 
1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 
    1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 
    2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]

Data = [1.75304482, 1.838272896, 2.076588315, 2.106925052, 2.080412635, 2.062989124, 
2.134900941, 2.140990127, 2.310136976, 2.405428706, 2.579437616, 2.781424141, 2.842911421, 
2.741331765, 2.530944779, 2.208521015, 2.277272419, 2.150449344, 2.103804022, 2.245873109, 
2.248964336, 2.153787614, 1.781971945, 1.77477941, 1.862197809, 1.775872572, 1.808137349, 
1.812758965, 2.117466603, 2.505083076, 2.535133011, 2.345618342, 2.393682526, 2.513121072,
2.724034867, 2.94104334, 3.368968784, 3.864226566, 3.897700791, 4.10553651, 3.876961939, 3.473025803, 
3.54868213, 3.534984654, 3.756382831, 3.84046304, 3.98128427, 4.35156491, 4.316439805, 3.969434147, 
4.24629428, 4.606852213, 4.656812685, 4.732135712]


output_file("sienaplot.html")

# create a new plot with a datetime axis type
p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")


p = figure(title="CO2 Emissions in Chile Over Time", plot_width=600, plot_height=250, x_axis_type="datetime")
p.add_layout(Title(text="CO2 Emissions (metric tons per capita)", align="center"), "left")
p.add_layout(Title(text="Date (Years)", align="center"), "below")
p.line(Date, Data, color='navy', alpha=0.5)


#p.xaxis.formatter=DatetimeTickFormatter( years = ['%Y'] )
p.xaxis.formatter=BasicTickFormatter()
show(p)