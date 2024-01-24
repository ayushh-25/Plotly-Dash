from dash import Dash, html, dcc 
from dash.dependencies import Input, Output

app = Dash()

app.layout = html.Div([

    html.Div(
    dcc.RangeSlider(
        id='rangeSlider',
        min= -10,
        max= 10, 
        step= 1,
        value=[-1,1]
    ), 
    style=dict(width='50%')),

    html.Hr(),

    html.H3(id='text')
])


@app.callback(Output(component_id='text', component_property='children'),
              [Input(component_id='rangeSlider', component_property='value')])
def multiply(range_list):
    return range_list[0]*range_list[1]



if __name__ == '__main__':
    app.run(debug=True)