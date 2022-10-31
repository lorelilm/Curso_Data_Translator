import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('C:\\Users\\ellomo19\\Documents\\Curso_Data_Translator\\Visualizacion\\datasets\\auto-mpg.csv')

app = dash.Dash(__name__)

fig = px.scatter(df, x="displ", y="weight",
                    log_x=True, size_max=55, trendline="ols")

app.layout = html.Div(children=[
    html.H1("Displacement vs Weight"),
    html.Img(
        src="https://img.remediosdigitales.com/4bf55b/aston-martin-f1-2021/450_1000.jfif",
        style = {'width': '40%'}),
    dcc.Graph(
        figure=fig
    )
])
    

if __name__ == '__main__':
    app.run_server(debug=True)