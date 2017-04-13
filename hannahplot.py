import pandas as pd
from bokeh.plotting import figure, output_file, show

nan = float('nan')

Date = [1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 
    1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 
    2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]

Data = [1.09, 3.27, 3.15, 10.8, 12.24, 14.65, 18.79, 14.37, 22.45, 13.76, 21.73,
    21.05, 22.6, 24.9, 24.017, 23.429, nan, 26.96, 25.13, 28.21, 26.09, 29.4, 26.52,
    21.74, 28.51, 22.76, 26.77, 29.46, 25.02, 27.1, 24.1, 22.2, 26, 21.2, 24, 24.1]

output_file("hannahplot.html")

# create a new plot with a datetime axis type
p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")

p.line(Date, Data, color='navy', alpha=0.5)

show(p)