import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
# Charts referended from this Doc --> ([highcharts] Documentation = https://www.highcharts.com/demo/highcharts)
import justpy as jp

# Setup data frames
data = pandas.read_csv("./App3_DataAnalysisAndVisualisation-PandasAndMatplotlib/data/reviews.csv", parse_dates = ['Timestamp']) # Assume pathing is not an issue

share = data.groupby(['Course Name'])['Rating'].count()

# LOAD CHARTS (will be seen as dict in python (JSON-like))
# Manipulated version of (https://www.highcharts.com/demo/highcharts/pie-chart)
chart_def = """ 
{
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Number of Ratings by Course'
    },
    tooltip: {
        valueSuffix: '%'
    },
    subtitle: {
        text:
        'According to Arjin Udemy Rating Data'
    },
    plotOptions: {
        series: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: [{
                enabled: true,
                distance: 20
            }, {
                enabled: true,
                distance: -40,
                format: '{point.percentage:.1f}%',
                style: {
                    fontSize: '1.2em',
                    textOutline: 'none',
                    opacity: 0.7
                },
                filter: {
                    operator: '>',
                    property: 'percentage',
                    value: 10
                }
            }]
        }
    },
    series: [
        {
            name: 'Percentage',
            colorByPoint: true,
            data: [
                {
                    name: 'Water',
                    y: 55.02
                },
                {
                    name: 'Fat',
                    sliced: true,
                    selected: true,
                    y: 26.71
                },
                {
                    name: 'Carbohydrates',
                    y: 1.09
                },
                {
                    name: 'Protein',
                    y: 15.5
                },
                {
                    name: 'Ash',
                    y: 1.68
                }
            ]
        }
    ]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-lg")
    p1= jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-center q-pa-lg")
    
    # Create charts
    hc = jp.HighCharts(a=wp, options=chart_def, classes="text-center q-pa-lg")
    
    # Create graph data in proper format
    hc_data = [{"name":v1, "y":v2} for v1, v2 in zip(share.index, share)]
    
    # Modify charts' data
    hc.options.series[0].data = hc_data
    
    return wp

jp.justpy(app)

