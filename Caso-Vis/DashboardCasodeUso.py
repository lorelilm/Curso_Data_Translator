import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('C:\\Users\\ellomo19\\Documents\\Curso_Data_Translator\\Caso-Vis\\DFparte7.csv')

df["likes"] = df["likes"].astype(int)
df["dislikes"] = df["dislikes"].astype(int)
df["category"] = df["category_title"].astype(str)

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="Correlation between likes and dislikes", style={"color":"black", "margin-left": "auto", "margin-right": "auto", "display": "block"}),
    html.Img(
        src="https://cdn.vox-cdn.com/thumbor/vpdLqZ7JLEvo7p_3StlqdGUZ2Os=/0x0:2040x1360/1200x628/filters:focal(1020x680:1021x681)/cdn.vox-cdn.com/uploads/chorus_asset/file/10480479/acastro_180321_1777_youtube_0002.jpg",
        style = {"width": "50%", "margin-left": "auto", "margin-right": "auto", "display": "block"}),
    dcc.Graph(id="graph_ld"),
    dcc.Dropdown(
        id="category_dropdown",
        options=[
            {"label": "Entertainment", "value": "Entertainment"},
            {"label": "Music", "value": "Music"},
            {"label": "Howto & Style", "value": "Howto & Style"},
            {"label": "Comedy", "value": "Comedy"},
            {"label": "People & Blogs", "value": "People & Blogs"},
            {"label": "News & Politics", "value": "News & Politics"},
            {"label": "Science & Technology ", "value": "Science & Technology "},
            {"label": "Film & Animation ", "value": "Film & Animation"},
            {"label": "Sports", "value": "Sports"},
            {"label": "Education", "value": "Education"},
            {"label": "Pets & Animals", "value": "Pets & Animals"},
            {"label": "Gaming", "value": "Gaming"},
            {"label": "Travel & Events", "value": "Travel & Events"},
            {"label": "Autos & Vehicles", "value": "Autos & Vehicles"},
            {"label": "Nonprofits & Activism", "value": "Nonprofits & Activism"},
            {"label": "Shows", "value": "Shows"},

            #options= [{"label": x, "value": x} for x in np.sort(dfv["category_title"].unique())],

        ],
        value= 'Entertainment'
        ),
])

@app.callback(
    Output('graph_ld', 'figure'),
    Input('category_dropdown', 'value')
)
def update_figure(selected_category):
    filtered_df = df[df.category == selected_category]
    
    fig= px.scatter(filtered_df, x="likes", y="dislikes", log_x=True, log_y=True, trendline="ols", opacity=0.5, color="dislikes")

    fig.update_layout(transition_duration=500)
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)