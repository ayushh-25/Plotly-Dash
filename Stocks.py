from dash import dcc, html, Dash
from dash.dependencies import Input, Output, State
import yfinance as yf
from datetime import datetime
import pandas as pd 

data = pd.read_csv('Data/NASDAQcompanylist.csv', index_col='Symbol')

options = []
for sym in data.index:
    options.append({'label': data.loc[sym]['Name'] + " " + sym, 'value': sym})


app = Dash()

app.layout = html.Div([
                html.H1('Stock Ticker Dashboard'),

                html.Div([
                    html.Div([
                        html.H3('Enter a stock symbol'),
                        dcc.Dropdown(
                                id='search',
                                options=options,  
                                value=['TSLA'],
                                multi=True
                        )
                    ], style={'display':'inline-block', 'padding':30,'verticalAlign':'top', 'width':'30%'}),

                    html.Div([
                        html.H3('Pick Date'),
                        dcc.DatePickerRange(
                            id='calender',
                            min_date_allowed=datetime(2015, 1, 1),
                            max_date_allowed=datetime.today(),
                            start_date=datetime(2022,1,1),
                            end_date=datetime.today()
                        )                   
                    ], style={'display':'inline-block', 'padding':30}),

                    html.Div([
                        html.Button(
                            id='submit',
                            n_clicks=0,
                            children='Submit',
                            style={'fontSize':20, 'marginLeft':'30px'}
                        )
                    ], style={'display':'inline-block', 'padding':30} )

                ]),



                dcc.Graph(id='plot',
                          figure=dict(
                              data=[dict(
                                  x=[1,2],
                                  y=[2,1]
                              )],
                              layout=dict(
                                  title='Default title'
                              )
                          )
                )

])


@app.callback(Output(component_id='plot', component_property='figure'),
              [Input(component_id='submit', component_property='n_clicks')],
              [State(component_id='search', component_property='value'),
               State(component_id='calender', component_property='start_date'),
               State(component_id='calender', component_property='end_date')])

def update_plot(click, stocks, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')

    end = datetime.strptime(end_date[:10], '%Y-%m-%d')

    

    traces = []
    for stock in stocks:
        df = yf.download(stock, start, end=end)
        traces.append(dict(
                    x=df.index,
                    y=df['Close'],
                    name=stock
                ))


    fig = dict(
                data=traces,
                layout=dict(
                    title=", ".join(stocks)
                )
            )
    return fig


if __name__ == '__main__':
    app.run(debug=True)