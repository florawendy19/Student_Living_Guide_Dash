import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
# Load data into a Pandas DataFrame
df = pd.read_csv("../data/processed_data.csv")
continent_options = [
    {"label": "Chennai", "value": "Chennai"},
    {"label": "Bengaluru", "value": "Bengaluru"},
    {"label": "New Delhi", "value": "New Delhi"},
    {"label": "Kolkata", "value": "Kolkata"},
    {"label": "Patna", "value": "Patna"},
    {"label": "Pune", "value": "Pune"},
    {"label": "Trichy", "value": "Trichy"}
]
# Create the app
app = dash.Dash(__name__)
server = app.server
# Define the layout
app.layout = html.Div(children=[
    html.H1(children='Children Centers'),
    html.Div(children=[
        html.Label('Select a City',style={'font-weight': 'bold',"margin-right": "10px"}),
        dcc.Dropdown(
            id="city-dropdown",
            options=[{'label': i, 'value': i} for i in df['Continent'].unique()],
            #value=city_options[0]["value"],
            style={"width": "150px","fontsize":"1px"}
        )
    ], style={'display': 'flex', 'align-items': 'center', 'margin-top': '10px', 'margin-bottom': '10px'}),
    dcc.Graph(id='map-graph'),
    dcc.Graph(id='bar-graph')
])
# Define the callbacks
@app.callback(
    dash.dependencies.Output('map-graph', 'figure'),
    [dash.dependencies.Input('city-dropdown', 'value')]
)
def update_map(city):
    filtered_df = df[df['Continent'] == Continent]
    fig = px.scatter_mapbox(
        filtered_df,
        lat='latitude',
        lon='longitude',
        hover_name='Groceries Index',
        size='Rent Index',
        color='continent',
        zoom=10,
        title=f"Details of countries in {Continent}"
    )
    fig.update_layout(mapbox_style="open-street-map")
    return fig
@app.callback(
    dash.dependencies.Output('bar-graph', 'figure'),
    [dash.dependencies.Input('city-dropdown', 'value')]
)
def update_bar(city):
    filtered_df = df[df['City'] == city]
    fig = px.bar(
        filtered_df,
        x='Centre Name',
        y='Children Available',
        color='Subject',
        title = f"Number of Children Available Centerwise in {city}"
    )
    return fig
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)