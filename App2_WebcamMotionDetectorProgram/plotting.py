# from motionDetector import df
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import FixedTicker, HoverTool, ColumnDataSource

#for testing only delete after
import pandas
df = pandas.read_csv("./App2_WebcamMotionDetectorProgram/motion_capture_times.csv", parse_dates=["Start", "End"])


# Convert to string for proper hover text
df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

# Create ColumnDataSource object from given data frame 
cds = ColumnDataSource(df)

# Create a figure object
f = figure(x_axis_type='datetime', height=300, width=1000, sizing_mode="stretch_width", title="Motion Graph")

# Configure figure object
f.yaxis.minor_tick_line_color = None
f.ygrid[0].ticker = FixedTicker(ticks=[0, 1])

# Creat hover tool feature with Hover object
hover = HoverTool(tooltips = [("Start: ", "@Start_string"), ("End: ", "@End_string")]) # A COLOR FOR START AND END

# Add the Hover object tool to the figure object
f.add_tools(hover)

# Create a line glot
q = f.quad(left = "Start", right = "End", bottom = 0, top = 1, color="green", source = cds)

# Display and save figure object
output_file("time_interval.html")
show(f)
