from dash import Dash, html, dcc
import plotly.graph_objs as go 

app = Dash(__name__)

colors = dict(background='#000000', text='#f44336')

app.layout = html.Div(children=[
    html.H1(children='Hello Dashboard !!', style=dict(textAlign='center', color=colors['text'])), # Header tag
    dcc.Graph(id='1',
              figure=dict(                                                  # A dictionary
                  data=[go.Bar(x=[1,2,3],                                   # needs a List 
                               y=[3,4,1],
                               name='1'),
                        go.Bar(x=[1,2,3],
                                y=[2,1,4],
                                name='2')],  
                  layout=dict(title='Grouped Bar Plot',                     #A dictionary
                               barmode='stack',
                               plot_bgcolor=colors['background'],
                               paper_bgcolor=colors['background'],
                               font=dict(
                                   color=colors['text']
                               ))
              ))
    ],
    style=dict(
        backgroundColor=colors['background']
    )
    )


if __name__ == '__main__':
    app.run(debug=True)