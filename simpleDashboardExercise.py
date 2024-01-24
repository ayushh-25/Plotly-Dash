#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
from dash import Dash, dcc, html
import pandas as pd
import plotly.graph_objs as go



# Launch the application:
app = Dash(__name__)


# Create a DataFrame from the .csv file:
df = pd.read_csv('Data/OldFaithful.csv')

# Create a Dash layout that contains a Graph component:
app.layout = html.Div(
    children=[
        dcc.Graph(
            id='01',
            figure=dict(
                data=[
                    go.Scatter(
                        x=df['X'],
                        y=df['Y'],
                        mode='markers'
                    )
                ],
                layout=dict(
                    title='Old Faithful Erruption intervals vs Duration',
                    xaxis=dict(
                        title='duration of the current eruption (in minutes)'
                    ),
                    yaxis=dict(
                        title='Interval of the next eruption (in minutes)'
                    )
                )
            )
        )
    ]
)


# Add the server clause:
if __name__ == '__main__':
    app.run(debug=True)