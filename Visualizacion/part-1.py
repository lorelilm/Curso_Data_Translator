import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Img(
        src='assets\\coca-cola.jpg',
        style={'width': '50%', 'border': '1px solid red'},
        alt='image'),

    html.H1(children="Loreli Lozada", style={'color': 'black'}),
    html.P('Data Translator Lead at Arca Continental', style={'color': 'maroon', 'border': '2px solid red'})
])

if __name__ == '__main__':
    app.run_server(debug=True)
