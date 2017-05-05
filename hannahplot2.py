import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter, Title
nan = float('nan')

HoleData = [1.09, 3.27, 3.15, 10.8, 12.24, 14.65, 18.79, 14.37, 22.45, 13.76, 21.73,
    21.05, 22.6, 24.9, 24.017, 23.429, nan, 26.96, 25.13, 28.21, 26.09, 29.4, 26.52,
    21.74, 28.51, 22.76, 26.77, 29.46, 25.02, 27.1, 24.1, 22.2, 26, 21.2, 24, 24.1]

CFCData = [272.5,292.3,308.8,325.5,342.6,359.4,378.2,396.5,416.3,435.8,454.4,472.7,
    487.3,498.3,507,514.8,521,526.5,530.8,534.3,537.2,539,540.6,541.3,541.6,541.5,
    540.7,539.8,538.1,536.2,533.53,530.9,528.47,525.88,523.48,521.08]

output_file("hannahplot2.html")

p = figure(title="Ozone Hole Size vs CFC Concentration", plot_width=400, plot_height=400)

p.add_layout(Title(text="Ozone Hole Size (million km squared)", align="center"), "left")
p.add_layout(Title(text="CFC Mixing Ratio", align="center"), "below")
# add a circle renderer with a size, color, and alpha
p.circle(CFCData, HoleData, size=20, color="navy", alpha=0.5)

# show the results
show(p)