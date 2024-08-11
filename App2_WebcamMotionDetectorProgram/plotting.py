from motionDetector import df
from bokeh.plotting import figure
from bokeh.io import output_file, show

output_file("time_interval.html")

# Create a figure object
f = figure()

# Create a line plot
f.line(df["Start"], df["End"], color="Green")

# Write the graph in the figure object
show(f)