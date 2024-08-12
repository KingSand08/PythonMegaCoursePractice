import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
# Charts referended from this Doc --> ([highcharts] Documentation = https://www.highcharts.com/demo/highcharts)
import justpy as jp

# Setup data frames
data = pandas.read_csv("./App3_DataAnalysisAndVisualisation-PandasAndMatplotlib/data/reviews.csv", parse_dates = ['Timestamp']) # Assume pathing is not an issue

data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean(numeric_only=True)

# LOAD CHARTS (will be seen as dict in python (JSON-like))
# Manipulated version of (https://www.highcharts.com/demo/highcharts/spline-inverted)
chart_def = """ 
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Day',
        align: 'center'
    },
    subtitle: {
        text: 'According to Arjin Udemy Rating Data',
        align: 'center'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date(Day)'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Day Range: 2018-01-01 to 2021-04-02.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Rating Range: 0 to 5.0.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: 'Day {point.x}: {point.y} stars'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Rating',
        data: [
            [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]
        ]

    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analyssis of Course Reviews", classes="text-h3 text-center q-pa-lg")
    p1= jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-center q-pa-lg")
    
    # Create charts
    hc = jp.HighCharts(a=wp, options=chart_def, classes="text-center q-pa-lg")
    
    # Modify charts' data   
    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average['Rating'])
    
    return wp

jp.justpy(app)

