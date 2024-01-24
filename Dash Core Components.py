from dash import Dash, html, dcc 

app = Dash()

app.layout = html.Div([

    html.Label('Dropdown 1'),
    dcc.Dropdown(options=[
                        dict(
                            label='AAAAA',
                            value='A'
                        ),
                        dict(
                            label='BBBBB',
                            value='B'
                        ),
                        dict(
                            label='CCCCC',
                            value='C'
                        )
                    ],
                 value='B'),

    html.Label('Dropdown 2'),
    dcc.Dropdown(options=[
                        dict(
                            label='AAAAA',
                            value='A'
                        ),
                        dict(
                            label='BBBBB',
                            value='B'
                        ),
                        dict(
                            label='CCCCC',
                            value='C'
                        )
                    ],
                 value='B',
                 multi=True),

    html.Label('Slider'),
    dcc.Slider(min=0,
               max=10,
               step=1,
               value=3),

    html.Label('Checklist'),
        dcc.Checklist(['New York City', 'Montréal', 'San Francisco'],
                  ['Montréal', 'San Francisco'])

])


if __name__ == '__main__':
    app.run(debug=True)