
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
# Charts referended from this Doc --> ([highcharts] Documentation = https://www.highcharts.com/demo/highcharts)
import justpy as jp

# Setup data frames
data = pandas.read_csv("./App3_DataAnalysisAndVisualisation-PandasAndMatplotlib/data/reviews.csv", parse_dates = ['Timestamp']) # Assume pathing is not an issue

data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month' , 'Course Name'])['Rating'].mean(numeric_only=True).unstack()

# LOAD CHARTS (will be seen as dict in python (JSON-like))
# Manipulated version of (https://www.highcharts.com/demo/highcharts/areaspline)
chart_def = """ 
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating By Month by Course',
        align: 'center'
    },
    subtitle: {
        text: 'According to Arjin Udemy Rating Data',
        align: 'center'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 10,
        y: 150,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        title: {
            text: 'Time(Years)'
        }
    },
    yAxis: {
        title: {
            text: 'Rating'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Course Ratings {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        series: {
            pointStart: 2000
        },
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{}]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-lg")
    p1= jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-center q-pa-lg")
    
    # Create charts
    hc = jp.HighCharts(a=wp, options=chart_def)

    # Create graph data in proper format
    hc_data = [{"name":v1, "data":[v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns] 

    # Modify charts' data
    hc.options.xAxis.categories = list(month_average_crs.index)
    hc.options.series = hc_data
    
    return wp

jp.justpy(app)

