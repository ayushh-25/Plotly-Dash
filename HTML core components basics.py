from dash import Dash, html

app = Dash()

app.layout = html.Div([
    'This the outer Div !!',
    html.Div([
        'This is inner div 1 !!',
        html.Div([
            'This is inner most div !!'
        ],
        style=dict(
            color='black',
            border='3px black solid'
        )
        )
    ],
    style=dict(
        color='blue',
        border='3px blue solid'
    )
    ),
        html.Div([
        'This is inner div 2 !!'
    ],
    style=dict(
        color='green',
        border='3px green solid'
    )
    )
],
style=dict(
    color='red',
    border='3px red solid'
)
)

if __name__ == '__main__':
    app.run(debug=True)